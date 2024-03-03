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

    def to_dict(cpu):
        return {
            'model': cpu.model,
            'price': cpu.price,
        }

    def __repr__(self):
        return f"CPU(model={self.model}, price={self.price}, clockSpeed={self.clockSpeed})"

class CPUCOOLER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    size = db.Column(db.Integer, nullable=True, default=None)
    rpm = db.Column(db.String(20))

class MOBO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    mem_slot = db.Column(db.Integer, nullable=True, default=None)
    socket_type = db.Column(db.String(20), nullable=True, default=None)#am4, am5, LGA1700 etc
    form_factor = db.Column(db.String(10), nullable=True, default=None)#atx, matx, etc

class GPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    chipset = db.Column(db.String(50), nullable=True)
    mem = db.Column(db.Integer, nullable=True, default=None)
    core_clock = db.Column(db.Integer, nullable=True, default=None)
    gpu_len = db.Column(db.Integer, nullable=True, default=None)
    
    def __repr__(self):
        return f"GPU(model={self.model}, price={self.price}, chipset={self.chipset})"



class RAM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    speed = db.Column(db.String(20), nullable=True, default=None) #ddr4-3600
    modules = db.Column(db.String(20), nullable=True, default=None) # 2 x 8, 16
    cas_latency = db.Column(db.Integer, nullable=True, default=None)

class DRIVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    capacity = db.Column(db.Integer, nullable=True, default=None)
    drive_type = db.Column(db.String(10), nullable=True, default=None)
    interface = db.Column(db.String(20), nullable=True, default=None) #M.2 PCIe 4.0x4

class PSU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    form_factor = db.Column(db.String(5))
    effi = db.Column(db.String(10), nullable=True, default=None)
    wattage = db.Column(db.Integer, nullable=True, default=None)
    mod = db.Column(db.String(10), nullable=True, default=None)

class CASE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2))
    type = db.Column(db.String(20), nullable=True, default=None)
    color = db.Column(db.String(20), nullable=True, default=None)
    side_panel = db.Column(db.String(25), nullable=True, default=None)

class FANS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=True, default=None)
    size = db.Column(db.Integer, nullable=True, default=None)
    rpm = db.Column(db.String(20), nullable=True, default=None)