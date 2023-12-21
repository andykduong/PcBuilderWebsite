from flask import redirect, url_for, render_template, flash, request
from flaskr import app, db
from flaskr.forms import RegistrationForm, LoginForm
from flaskr.models import User, CPU, CPUCooler, Mobo, GPU, RAM, drive, PSU, case, fans
from flask_login import current_user, login_user, logout_user



@app.route('/')

@app.route('/index')
def index():
    return render_template("index.html",)

@app.route('/pick_<pc_part>')
def part_picker(pc_part):
    if pc_part == 'cpu':
        cpu_entries = CPU.query.all()
        return render_template('parts/cpu.html', cpu_entries=cpu_entries)
    if pc_part == 'cpucooler':
        cpucooler_entries = CPUCooler.query.all()
        return render_template('parts/cpucooler.html', cpucooler_entries=cpucooler_entries)
    if pc_part == 'mobo':
        mobo_entries = Mobo.query.all()
        return render_template('parts/mobo.html', mobo_entries=mobo_entries)
    if pc_part == 'gpu':
        gpu_entries = GPU.query.all()
        return render_template('parts/gpu.html', gpu_entries=gpu_entries)
    if pc_part == 'ram':
        ram_entries = RAM.query.all()
        return render_template('parts/ram.html', ram_entries=ram_entries)
    if pc_part == 'drive':
        drive_entries = drive.query.all()
        return render_template('parts/drive.html', drive_entries=drive_entries)
    if pc_part == 'psu':
        psu_entries = PSU.query.all()
        return render_template('parts/psu.html', psu_entries=psu_entries)
    if pc_part == 'case':
        case_entries = case.query.all()
        return render_template('parts/case.html', case_entries=case_entries)
    if pc_part == 'fans':
        fans_entries = fans.query.all()
        return render_template('parts/fans.html', fans_entries=fans_entries)
    
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
