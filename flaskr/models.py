from flaskr import db, Bcrypt, login
from flask_login import UserMixin
from sqlalchemy.orm.attributes import flag_modified

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_pfp = db.Column(db.String(16), nullable=False, default='images/default_pfp.jpeg')
    password = db.Column(db.String(60), nullable=False)
    pc_build = db.relationship('PCBuild', back_populates='user')

    def get_build(self):
        return self.pc_build
    
    #for debugging
    # def removeBuild(self):
    #     self.pc_build = None
    #     flag_modified(self, 'pc_build')
    #     db.session.commit()

    def set_pass(self, password):
        self.password = Bcrypt.generate_password_hash(password).decode('utf-8')

    def check_pass(self, password):
        return Bcrypt.check_password_hash(self.password, password)
   
    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, pc_build={self.pc_build})"

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

build_cpu = db.Table('build_cpu',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('cpu_id', db.Integer, db.ForeignKey('cpu.id', ondelete='CASCADE'), primary_key=True)
                     )
build_cpucooler = db.Table('build_cpucooler',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('cpucooler_id', db.Integer, db.ForeignKey('cpucooler.id', ondelete='CASCADE'), primary_key=True)
                     )
build_mobo = db.Table('build_mobo',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('mobo_id', db.Integer, db.ForeignKey('mobo.id', ondelete='CASCADE'), primary_key=True)
                     )
build_gpu = db.Table('build_gpu',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('gpu_id', db.Integer, db.ForeignKey('gpu.id', ondelete='CASCADE'), primary_key=True)
                     )
build_ram = db.Table('build_ram',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('ram_id', db.Integer, db.ForeignKey('ram.id', ondelete='CASCADE'), primary_key=True)
                     )
build_drive = db.Table('build_drive',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('drive_id', db.Integer, db.ForeignKey('drive.id', ondelete='CASCADE'), primary_key=True)
                     )
build_psu = db.Table('build_psu',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('psu_id', db.Integer, db.ForeignKey('psu.id', ondelete='CASCADE'), primary_key=True)
                     )
build_case = db.Table('build_case',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('case_id', db.Integer, db.ForeignKey('case.id', ondelete='CASCADE'), primary_key=True)
                     )
build_fans = db.Table('build_fans',
                     db.Column('build_id', db.Integer, db.ForeignKey('pcbuild.id', ondelete='CASCADE'), primary_key=True),
                     db.Column('fans_id', db.Integer, db.ForeignKey('fans.id', ondelete='CASCADE'), primary_key=True)
                     )



class PCBuild(db.Model):
    __tablename__ = 'pcbuild'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    # title = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates = 'pc_build')

    cpu = db.relationship('CPU', secondary=build_cpu, back_populates='build', cascade="all, delete")
    cpucooler = db.relationship('CPUCOOLER', secondary=build_cpucooler, back_populates='build', cascade="all, delete")
    mobo = db.relationship('MOBO', secondary=build_mobo, back_populates='build', cascade="all, delete")
    gpu = db.relationship('GPU', secondary=build_gpu, back_populates='build', cascade="all, delete")
    ram = db.relationship('RAM', secondary=build_ram, back_populates='build', cascade="all, delete")
    drive = db.relationship('DRIVE', secondary=build_drive, back_populates='build', cascade="all, delete")
    psu = db.relationship('PSU', secondary=build_psu, back_populates='build', cascade="all, delete")
    case = db.relationship('CASE', secondary=build_case, back_populates='build', cascade="all, delete")
    fans = db.relationship('FANS', secondary=build_fans, back_populates='build', cascade="all, delete")

    def add_part(self, item):
        part_type = type(item)

        if part_type.__name__ == "CPU":
            self.cpu.append(item)
        elif part_type.__name__ == "CPUCOOLER":
            self.cpucooler.append(item)
        elif part_type.__name__ == "MOBO":
            self.mobo.append(item)
        elif part_type.__name__ == "GPU":
            self.gpu.append(item)
        elif part_type.__name__ == "RAM":
            self.ram.append(item)
        elif part_type.__name__ == "DRIVE":
            self.drive.append(item)
        elif part_type.__name__ == "PSU":
            self.psu.append(item)
        elif part_type.__name__ == "CASE":
            self.case.append(item)
        elif part_type.__name__ == "FANS":
            self.fans.append(item)
        
        return

    def __repr__(self):
        return f'PCBuild(cpu={self.cpu}, cpucooler={self.cpucooler}, mobo={self.mobo}, gpu={self.gpu}, ram={self.ram}, drive={self.drive}, psu={self.psu}, case={self.case}, fans={self.fans})'

class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    clockSpeed = db.Column(db.Float(precision=1), nullable=False)
    build = db.relationship('PCBuild', secondary=build_cpu, back_populates='cpu', cascade="all, delete")

    def __repr__(self):
        return f"CPU(id={self.id}, model={self.model}, price={self.price}, clockSpeed={self.clockSpeed})"

class CPUCOOLER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    size = db.Column(db.Integer, nullable=True, default=None)
    rpm = db.Column(db.String(20))
    build = db.relationship('PCBuild', secondary=build_cpucooler, back_populates='cpucooler', cascade="all, delete")

    def __repr__(self):
        return f"CPUCOOLER(id={self.id}, model={self.model}, price={self.price})"

class MOBO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    mem_slot = db.Column(db.Integer, nullable=True, default=None)
    socket_type = db.Column(db.String(20), nullable=True, default=None)#am4, am5, LGA1700 etc
    form_factor = db.Column(db.String(10), nullable=True, default=None)#atx, matx, 
    build = db.relationship('PCBuild', secondary=build_mobo, back_populates='mobo', cascade="all, delete")

    def __repr__(self):
        return f"MOBO(id={self.id}, model={self.model}, price={self.price})"

class GPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    chipset = db.Column(db.String(50), nullable=True)
    mem = db.Column(db.Integer, nullable=True, default=None)
    core_clock = db.Column(db.Integer, nullable=True, default=None)
    gpu_len = db.Column(db.Integer, nullable=True, default=None)
    build = db.relationship('PCBuild', secondary=build_gpu, back_populates='gpu', cascade="all, delete")
    
    def __repr__(self):
        return f"GPU(id={self.id}, model={self.model}, price={self.price}, chipset={self.chipset})"

class RAM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    speed = db.Column(db.String(20), nullable=True, default=None) #ddr4-3600
    modules = db.Column(db.String(20), nullable=True, default=None) # 2 x 8, 16
    cas_latency = db.Column(db.Integer, nullable=True, default=None)
    build = db.relationship('PCBuild', secondary=build_ram, back_populates='ram', cascade="all, delete")

    def __repr__(self):
        return f"RAM(id={self.id}, model={self.model}, price={self.price})"

class DRIVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    capacity = db.Column(db.Integer, nullable=True, default=None)
    drive_type = db.Column(db.String(10), nullable=True, default=None)
    interface = db.Column(db.String(20), nullable=True, default=None) #M.2 PCIe 4.0x4
    build = db.relationship('PCBuild', secondary=build_drive, back_populates='drive', cascade="all, delete")

    def __repr__(self):
        return f"DRIVE(id={self.id}, model={self.model}, price={self.price})"


class PSU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    form_factor = db.Column(db.String(5))
    effi = db.Column(db.String(10), nullable=True, default=None)
    wattage = db.Column(db.Integer, nullable=True, default=None)
    mod = db.Column(db.String(10), nullable=True, default=None)
    build = db.relationship('PCBuild', secondary=build_psu, back_populates='psu', cascade="all, delete")
    
    def __repr__(self):
        return f"PSU(id={self.id}, model={self.model}, price={self.price})"


class CASE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    type = db.Column(db.String(20), nullable=True, default=None)
    color = db.Column(db.String(20), nullable=True, default=None)
    side_panel = db.Column(db.String(25), nullable=True, default=None)
    build = db.relationship('PCBuild', secondary=build_case, back_populates='case', cascade="all, delete")

    def __repr__(self):
        return f"CASE(id={self.id}, model={self.model}, price={self.price})"

class FANS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=True, default=None)
    size = db.Column(db.Integer, nullable=True, default=None)
    rpm = db.Column(db.String(20), nullable=True, default=None)
    build = db.relationship('PCBuild', secondary=build_fans, back_populates='fans', cascade="all, delete")

    def __repr__(self):
        return f"FANS(id={self.id}, model={self.model}, price={self.price})"