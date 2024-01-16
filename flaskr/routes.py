from flask import redirect, url_for, render_template, flash, request
from flaskr import app, db
from flaskr.forms import RegistrationForm, LoginForm
from flaskr.models import User, CPU, CPUCooler, Mobo, GPU, RAM, drive, PSU, case, fans
from flask_login import current_user, login_user, logout_user



@app.route('/')

@app.route('/index')
def index():
    return render_template("index.html",)

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
        cpucooler_entries = CPUCooler.query

        if min_value:
            cpucooler_entries = cpucooler_entries.filter(CPUCooler.price >= min_value) 
        return render_template('parts/cpucooler.html', cpucooler_entries=cpucooler_entries, min_value=min_value, part=CPUCooler, part_name='a CPU Cooler')
    if pc_part == 'mobo':
        mobo_entries = Mobo.query

        if min_value:
            mobo_entries = mobo_entries.filter(Mobo.price >= min_value) 
        return render_template('parts/mobo.html', mobo_entries=mobo_entries, min_value=min_value, part=Mobo, part_name='a Motherboard')
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
        drive_entries = drive.query

        if min_value:
            drive_entries = drive_entries.filter(drive.price >= min_value)
        return render_template('parts/drive.html', drive_entries=drive_entries, min_value=min_value, part=drive, part_name='a Drive')
    if pc_part == 'psu':
        psu_entries = PSU.query

        if min_value:
            psu_entries = psu_entries.filter(PSU.price >= min_value)
        return render_template('parts/psu.html', psu_entries=psu_entries, min_value=min_value, part=PSU, part_name='a PSU')
    if pc_part == 'case':
        case_entries = case.query

        if min_value:
            case_entries = case_entries.filter(case.price >= min_value)
        return render_template('parts/case.html', case_entries=case_entries, min_value=min_value, part=case, part_name='a Case')
    if pc_part == 'fans':
        fans_entries = fans.query

        if min_value:
            fans_entries = fans_entries.filter(fans.price >= min_value)
        return render_template('parts/fans.html', fans_entries=fans_entries, min_value=min_value, part=fans, part_name='fans')
    
    return "Invalid PC Component", 404

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
