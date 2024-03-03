from flaskr import app, db
from flaskr.models import User, CPU, CPUCOOLER, MOBO, GPU, RAM, DRIVE, PSU, CASE, FANS

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'CPU': CPU, 'CPUCOOLER': CPUCOOLER, 'MOBO': MOBO, 'GPU': GPU,
            'RAM': RAM, 'DRIVE': DRIVE, 'PSU': PSU, 'CASE': CASE, 'FANS': FANS}