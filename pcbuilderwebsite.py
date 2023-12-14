from flaskr import app, db
from flaskr.models import User, CPU, CPUCooler, Mobo, GPU, RAM, drive, PSU, case, fans

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'CPU': CPU, 'CPUCooler': CPUCooler, 'Mobo': Mobo, 'GPU': GPU,
            'RAM': RAM, 'drive': drive, 'PSU': PSU, 'case': case, 'fans': fans}