import json
from flaskr import db, app
from flaskr.models import CPU, CPUCooler, Mobo, GPU, RAM, drive, PSU, case, fans

def reset_db(table):
    with app.app_context():
        db.session.query(table).delete()
        db.session.commit()

def repopulate_db():
    with open('flaskr/parts_json/cpu.json', "r") as f:
        
        data = json.load(f)
        
        for cpu in data:
            model = cpu['name']
            price = cpu['price']
            clockSpeed = cpu['core_clock']

            if CPU.query.filter_by(model=model).first() is None: #get rid of dupes
                cpu_item = CPU(model=model, price=price, clockSpeed=clockSpeed)
                db.session.add(cpu_item)
    with open('flaskr/parts_json/cpu-cooler.json', "r") as f:
    
        data = json.load(f)
        
        for cpucooler in data:
            model = cpucooler['name']
            price = cpucooler['price']
            size = cpucooler['size']
            rpm = cpucooler['rpm']

            if isinstance(rpm, list):
                for i in range(len(rpm)):
                    
                    rpm[i] = str(rpm[i])
                    
                
                rpm_str = ','.join(rpm)
            else:
                rpm_str = str(rpm)

            if CPUCooler.query.filter_by(model=model).first() is None: #get rid of dupes
                cpucooler_item = CPUCooler(model=model, price=price, size=size, rpm=rpm_str)
                db.session.add(cpucooler_item)


    db.session.commit()
# with open('flaskr/parts_json/cpu_cooler.json', "r") as f:
    
#     data = json.load(f)
    
#     for cpu_cooler in data:
#         model = cpu_cooler['name']
#         price = cpu_cooler['price']
#         size = cpu_cooler['size']
#         rpm = cpu_cooler['rpm']
    
#         cpu_cooler_item = CPUCooler(model=model, price=price, size=size, rpm=rpm)
#         db.session.add(cpu_cooler_item)

# with open('flaskr/parts_json/motherboard.json', "r") as f:
    
#     data = json.load(f)
    
#     for mobo in data:
#         model = mobo['name']
#         price = mobo['price']
#         mem_slot = mobo['memory_slots']
#         mem_speed = mobo['max_memory']
#         socket_type = mobo['socket']
#         form_factor = mobo['form_factor']

#         mobo_item = Mobo(model=model, price=price, mem_slot=mem_slot, mem_speed=mem_speed, socket_type=socket_type, form_factor=form_factor)
#         db.session.add(mobo_item)

# with open('flaskr/parts_json/video-card.json', "r") as f:
    
#     data = json.load(f)
    
#     for gpu in data:
#         model = gpu['name'] + gpu['chipset']
#         price = gpu['price']
#         mem = gpu['memory']
#         core_clock = gpu['core_clock']
#         len = gpu['length']
    
#         gpu_item = GPU(model=model, price=price, mem=mem, core_clock=core_clock, gpu_len=len)
#         db.session.add(gpu_item)

# with open('flaskr/parts_json/memory.json', "r") as f:
    
#     data = json.load(f)
    
#     for ram in data:
#         model = ram['name']
#         price = ram['price']
#         speed = ram['speed']
#         modules = ram['modules']
#         cas_latency = ram['cas_latency']
    
#         gpu_item = GPU(model=model, price=price, mem=mem, core_clock=core_clock, gpu_len=len)
#         db.session.add(gpu_item)