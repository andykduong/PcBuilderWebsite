from flask import redirect, url_for, render_template, flash, request, session, jsonify
from flaskr import app, db
from flaskr.forms import RegistrationForm, LoginForm
from flaskr.models import User, CPU, CPUCOOLER, MOBO, GPU, RAM, DRIVE, PSU, CASE, FANS, PCBuild
from flask_login import current_user, login_user, logout_user



@app.route('/')

@app.route('/index')
def index():
    part_dict = { 
        'CPU': CPU, 'CPU Cooler': CPUCOOLER, 'Motherboard': MOBO, 'Graphics Card': GPU,
            'Memory': RAM, 'Storage': DRIVE, 'Power Supply': PSU, 'Case': CASE, 'Fans': FANS
    }
    parts = [
        {'name': 'CPU', 'chosen': None, 'add_url': 'cpu'},
        {'name': 'CPU Cooler', 'chosen':None, 'add_url': 'cpucooler'},
        {'name': 'Motherboard', 'chosen':None, 'add_url': 'mobo'},
        {'name': 'Graphics Card', 'chosen':None, 'add_url': 'gpu'},
        {'name': 'Memory', 'chosen':None, 'add_url': 'ram'},
        {'name': 'Storage', 'chosen':None, 'add_url': 'drive'},
        {'name': 'Power Supply', 'chosen':None, 'add_url': 'psu'},
        {'name': 'Case', 'chosen':None, 'add_url': 'case'},
        {'name': 'Fans', 'chosen':None, 'add_url': 'fans'},
    ]

    if 'pc_build' not in session:
        session['pc_build'] = {"cpu":None,"cpucooler":None,"mobo":None,"gpu":None,"ram":None,"drive":None,"psu":None, "case":None,"fans":None}

    for part in parts:
        part_model = part_dict[part['name']]
        part['chosen'] = part_model.query.get(session['pc_build'][part['add_url']])

    return render_template("index.html", parts=parts)

#For each individual picking page
@app.route('/pick_<part_type>', methods=['GET', "POST"])
def part_picker(part_type):
    

    if request.method == 'POST':
        min_value = float(request.form.get('minSlider', default=0))
        manufacturer = request.form.get('manuDropdown', default='')
    else:
        min_value = float(request.args.get('min', default=0))
        manufacturer = request.args.get('manuDropdown', default='')

    # part_dict = { 
    #     'cpu': CPU, 'cpucooler': CPUCOOLER, 'mobo': MOBO, 'gpu': GPU,
    #         'ram': RAM, 'drive': DRIVE, 'psu': PSU, 'case': CASE, 'fans': FANS
    # }

    # part = part_dict[part_type]
    # part_entries = part.query

    # if min_value:
    #     part_entries = part_entries.filter(part.price >= min_value)
    
    # if manufacturer:
    #     manufacturer_pattern = f"%{manufacturer}%"
    #     part_entries = part_entries.filter(part.model.like(manufacturer_pattern))

    # part_entries = part_entries.all()

    # template = f'parts/{part_type}.html'
    # part_var = f'{part_type}_entries'
    # part_name = part.toString()
    # print(f'Template: {template}, part_var: {part_var}, part: {part}, part_name: a {part}')

    # return render_template(template, part_var=part_entries, min_value=min_value, manufacturer=manufacturer, part=part, part_name=f'a {part_name}' )

    if part_type == 'cpu':
        cpu_entries = CPU.query

        if min_value:
            cpu_entries = cpu_entries.filter(CPU.price >= min_value) 

        if manufacturer:
            manufacturer_pattern = f"%{manufacturer}%"
            cpu_entries = cpu_entries.filter(CPU.model.like(manufacturer_pattern))

        cpu_entries = cpu_entries.all()
        return render_template('parts/cpu.html', cpu_entries=cpu_entries, min_value=min_value, manufacturer=manufacturer, part=CPU, part_name='a CPU')
    if part_type == 'cpucooler':
        cpucooler_entries = CPUCOOLER.query

        if min_value:
            cpucooler_entries = cpucooler_entries.filter(CPUCOOLER.price >= min_value) 
        return render_template('parts/cpucooler.html', cpucooler_entries=cpucooler_entries, min_value=min_value, part=CPUCOOLER, part_name='a CPU Cooler')
    if part_type == 'mobo':
        mobo_entries = MOBO.query

        if min_value:
            mobo_entries = mobo_entries.filter(MOBO.price >= min_value) 
        return render_template('parts/mobo.html', mobo_entries=mobo_entries, min_value=min_value, part=MOBO, part_name='a Motherboard')
    if part_type == 'gpu':
        gpu_entries = GPU.query

        if min_value:
            gpu_entries = gpu_entries.filter(GPU.price >= min_value)
        return render_template('parts/gpu.html', gpu_entries=gpu_entries, min_value=min_value, part=GPU, part_name='a GPU')
    if part_type == 'ram':
        ram_entries = RAM.query

        if min_value:
            ram_entries = ram_entries.filter(RAM.price >= min_value)
        return render_template('parts/ram.html', ram_entries=ram_entries, min_value=min_value, part=RAM, part_name='RAM')
    if part_type == 'drive':
        drive_entries = DRIVE.query

        if min_value:
            drive_entries = drive_entries.filter(DRIVE.price >= min_value)
        return render_template('parts/drive.html', drive_entries=drive_entries, min_value=min_value, part=DRIVE, part_name='a Drive')
    if part_type == 'psu':
        psu_entries = PSU.query

        if min_value:
            psu_entries = psu_entries.filter(PSU.price >= min_value)
        return render_template('parts/psu.html', psu_entries=psu_entries, min_value=min_value, part=PSU, part_name='a PSU')
    if part_type == 'case':
        case_entries = CASE.query

        if min_value:
            case_entries = case_entries.filter(CASE.price >= min_value)
        return render_template('parts/case.html', case_entries=case_entries, min_value=min_value, part=CASE, part_name='a Case')
    if part_type == 'fans':
        fans_entries = FANS.query

        if min_value:
            fans_entries = fans_entries.filter(FANS.price >= min_value)
        return render_template('parts/fans.html', fans_entries=fans_entries, min_value=min_value, part=FANS, part_name='fans')
    
    return "Invalid PC Component", 404

@app.route('/build_gallery')
def build_gallery():
    u = User.query.get(1)

    return render_template("build_gallery.html", userBuilds=u.pc_build)

@app.route('/save_build', methods=['POST'])
def save_build():
    if current_user.is_authenticated:
        part_dict = {"cpu":CPU,"cpucooler":CPUCOOLER,"mobo":MOBO,"gpu":GPU,"ram":RAM,"drive":DRIVE,"psu":PSU, "case":CASE,"fans":FANS}
        user_build = PCBuild(title='temp')
        if 'loadedBuild_id' in session:
            user_build = PCBuild.query.get(session['loadedBuild_id'])

        for part_name in session['pc_build']:

            curr_part = getattr(user_build, part_name, None)
            print(curr_part)
            curr_part.clear()
            item_id = session['pc_build'][part_name]
            actual_item = part_dict[part_name].query.get(item_id)
            curr_part.append(actual_item)
        
        db.session.commit()
        return redirect(url_for('build_gallery'))
    else:
        flash('Please create an account to save a build.', 'danger')
        return redirect(url_for('register'))
    

@app.route('/load', methods=['POST'])
def load_Build(build_id):
    part_dict = [
        {'name': 'CPU', 'add_url': 'cpu'},
        {'name': 'CPU Cooler','add_url': 'cpucooler'},
        {'name': 'Motherboard','add_url': 'mobo'},
        {'name': 'Graphics Card', 'add_url': 'gpu'},
        {'name': 'Memory', 'add_url': 'ram'},
        {'name': 'Storage', 'add_url': 'drive'},
        {'name': 'Power Supply', 'add_url': 'psu'},
        {'name': 'Case', 'add_url': 'case'},
        {'name': 'Fans', 'add_url': 'fans'},
    ]

    user_build = PCBuild.query.get(build_id)

    for part_column in user_build:
        part = part_column[0]
        print(part)
        # current_type = part_dict[]
        # session['pc_build'][] = part
    return redirect(url_for('index'))

#inside picking page, add button
@app.route('/add_part/<part_type>', methods = ['POST'])
def add_part(part_type):
    print(part_type)
    part_id = request.form[part_type + '_id']
    session['pc_build'][part_type] = part_id
    session.modified = True
    print(session['pc_build'])
    return redirect(url_for('index'))

@app.route('/remove_part/<part_type>', methods = ['POST'])
def remove_part(part_type):
    session['pc_build'][part_type] = None
    session.modified = True
    print(session['pc_build'])
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, pc_build={"cpu":None,"cpucooler":None,"mobo":None,"gpu":None,"ram":None,"drive":None,"psu":None, "case":None,"fans":None})
        user.set_pass(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.get_build() is None: #just to initalize their table
            current_user.add_part('cpu', None)
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
