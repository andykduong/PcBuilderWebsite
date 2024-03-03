from flask import redirect, url_for, render_template, flash, request
from flaskr import app, db
from flaskr.forms import RegistrationForm, LoginForm
from flaskr.models import User, CPU, CPUCOOLER, MOBO, GPU, RAM, DRIVE, PSU, CASE, FANS
from flask_login import current_user, login_user, logout_user

chosen_parts = {
    'selected_cpu':None,
    'selected_cpucooler':None,
    'selected_mobo':None,
    'selected_gpu':None,
    'selected_ram':None,
    'selected_drive':None,
    'selected_psu':None,
    'selected_case':None,
    'selected_fans':None,
}

@app.route('/')

@app.route('/index')
def index():

    parts = [
        {'name': 'CPU', 'chosen': chosen_parts['selected_cpu'], 'add_url': 'cpu'},
        {'name': 'CPU Cooler', 'chosen': chosen_parts['selected_cpucooler'], 'add_url': 'cpucooler'},
        {'name': 'Motherboard', 'chosen': chosen_parts['selected_mobo'], 'add_url': 'mobo'},
        {'name': 'Graphic Card', 'chosen': chosen_parts['selected_gpu'], 'add_url': 'gpu'},
        {'name': 'Memory', 'chosen': chosen_parts['selected_ram'], 'add_url': 'ram'},
        {'name': 'Storage', 'chosen': chosen_parts['selected_drive'], 'add_url': 'drive'},
        {'name': 'Power Supply', 'chosen': chosen_parts['selected_psu'], 'add_url': 'psu'},
        {'name': 'Case', 'chosen': chosen_parts['selected_case'], 'add_url': 'case'},
        {'name': 'Fans', 'chosen': chosen_parts['selected_fans'], 'add_url': 'fans'},
    ]

    return render_template("index.html", parts=parts)

@app.route('/pick_<pc_part>', methods=['GET', "POST"])
def part_picker(pc_part):
    

    if request.method == 'POST':
        min_value = float(request.form.get('minSlider', default=0))
        manufacturer = request.form.get('manuDropdown', default='')
    else:
        min_value = float(request.args.get('min', default=0))
        manufacturer = request.args.get('manuDropdown', default='')



    if pc_part == 'cpu':
        cpu_entries = CPU.query

        if min_value:
            cpu_entries = cpu_entries.filter(CPU.price >= min_value) 

        if manufacturer:
            manufacturer_pattern = f"%{manufacturer}%"
            cpu_entries = cpu_entries.filter(CPU.model.like(manufacturer_pattern))

        cpu_entries = cpu_entries.all()
        return render_template('parts/cpu.html', cpu_entries=cpu_entries, min_value=min_value, manufacturer=manufacturer, part=CPU, part_name='a CPU')
    if pc_part == 'cpucooler':
        cpucooler_entries = CPUCOOLER.query

        if min_value:
            cpucooler_entries = cpucooler_entries.filter(CPUCOOLER.price >= min_value) 
        return render_template('parts/cpucooler.html', cpucooler_entries=cpucooler_entries, min_value=min_value, part=CPUCOOLER, part_name='a CPU Cooler')
    if pc_part == 'mobo':
        mobo_entries = MOBO.query

        if min_value:
            mobo_entries = mobo_entries.filter(MOBO.price >= min_value) 
        return render_template('parts/mobo.html', mobo_entries=mobo_entries, min_value=min_value, part=MOBO, part_name='a Motherboard')
    if pc_part == 'gpu':
        gpu_entries = GPU.query

        if min_value:
            gpu_entries = gpu_entries.filter(GPU.price >= min_value)
        return render_template('parts/gpu.html', gpu_entries=gpu_entries, min_value=min_value, part=GPU, part_name='a GPU')
    if pc_part == 'ram':
        ram_entries = RAM.query

        if min_value:
            ram_entries = ram_entries.filter(RAM.price >= min_value)
        return render_template('parts/ram.html', ram_entries=ram_entries, min_value=min_value, part=RAM, part_name='RAM')
    if pc_part == 'drive':
        drive_entries = DRIVE.query

        if min_value:
            drive_entries = drive_entries.filter(DRIVE.price >= min_value)
        return render_template('parts/drive.html', drive_entries=drive_entries, min_value=min_value, part=DRIVE, part_name='a Drive')
    if pc_part == 'psu':
        psu_entries = PSU.query

        if min_value:
            psu_entries = psu_entries.filter(PSU.price >= min_value)
        return render_template('parts/psu.html', psu_entries=psu_entries, min_value=min_value, part=PSU, part_name='a PSU')
    if pc_part == 'case':
        case_entries = CASE.query

        if min_value:
            case_entries = case_entries.filter(CASE.price >= min_value)
        return render_template('parts/case.html', case_entries=case_entries, min_value=min_value, part=CASE, part_name='a Case')
    if pc_part == 'fans':
        fans_entries = FANS.query

        if min_value:
            fans_entries = fans_entries.filter(FANS.price >= min_value)
        return render_template('parts/fans.html', fans_entries=fans_entries, min_value=min_value, part=FANS, part_name='fans')
    
    return "Invalid PC Component", 404

@app.route('/add_part/<part_type>', methods = ['POST'])
def add_part(part_type):
    
    part_id = request.form[part_type + '_id']
    # part_id = request.form['cpu_id']
    # cpu = CPU.query.get(part_id)
    
    part_dict = { 
        'User': User, 'CPU': CPU, 'CPUCOOLER': CPUCOOLER, 'MOBO': MOBO, 'GPU': GPU,
            'RAM': RAM, 'DRIVE': DRIVE, 'PSU': PSU, 'CASE': CASE, 'FANS': FANS
    }

    part_model = part_dict[part_type.upper()]

    #cannot pass string 'CPU' in directly so use dict
    part = part_model.query.get(part_id)

    chosen_parts['selected_' + part_type] = part

    flash(part_type.upper() + ' added successfully!')

    return redirect(url_for('index'))
        

@app.route('/about')
def about():
    return render_template('about.html', title="About the Developer")

@app.route('/register', methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_pass(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_pass(form.password.data):
            flash('Invalid Email or Password', 'error')
            return redirect(request.url)

        login_user(user, remember=form.remember.data)
        flash('You have been logged in successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
