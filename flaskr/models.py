from flaskr import db, Bcrypt, login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_pfp = db.Column(db.String(16), nullable=False, default='images/default_pfp.jpeg')
    password = db.Column(db.String(60), nullable=False)

    def set_pass(self, password):
        self.password = Bcrypt.generate_password_hash(password).decode('utf-8')

    def check_pass(self, password):
        return Bcrypt.check_password_hash(self.password, password)
   
    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, image_pfp={self.image_pfp}, password={self.password})"

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    clockSpeed = db.Column(db.Float(precision=1), nullable=False)

    def __repr__(self):
        return f"CPU(model={self.model}, price={self.price}, clockSpeed={self.clockSpeed})"

class CPUCooler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    size = db.Column(db.Integer, nullable=True, default=None)
    rpm = db.Column(db.String(20))

class Mobo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    mem_slot = db.Column(db.Integer, nullable=False)
    mem_speed = db.Column(db.Integer, nullable=False)
    socket_type = db.Column(db.String(20), nullable=False)#am4, am5, LGA1700 etc
    form_factor = db.Column(db.String(10), nullable=False)#atx, matx, etc

class GPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    #pcie_gen = db.Column(db.String(10), nullable=False)
    mem = db.Column(db.Integer, nullable=False)
    core_clock = db.Column(db.Integer, nullable=False)
    gpu_len = db.Column(db.Integer, nullable=False)


class RAM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    speed = db.Column(db.String(20)) #ddr4-3600
    modules = db.Column(db.String(20)) # 2 x 8, 16
    cas_latency = db.Column(db.Integer)

class drive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    capacity = db.Column(db.Integer)
    drive_type = db.Column(db.String(10))
    interface = db.Column(db.String(20)) #M.2 PCIe 4.0x4

class PSU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    form_factor = db.Column(db.String(5))
    effi = db.Column(db.String(10))
    wattage = db.Column(db.Integer)
    mod = db.Column(db.String(10))

class case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    type = db.Column(db.String(20))
    color = db.Column(db.String(20))
    side_panel = db.Column(db.String(25))

class fans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    size = db.Column(db.Integer)
    rpm = db.Column(db.String(20))