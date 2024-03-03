import json
from flaskr import db, app
from flaskr.models import CPU, CPUCOOLER, MOBO, GPU, RAM, DRIVE, PSU, CASE, FANS

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

            if CPUCOOLER.query.filter_by(model=model).first() is None: #get rid of dupes
                cpucooler_item = CPUCOOLER(model=model, price=price, size=size, rpm=rpm_str)
                db.session.add(cpucooler_item)


    with open('flaskr/parts_json/motherboard.json', "r") as f:
    
        data = json.load(f)
        
        for mobo in data:
            model = mobo['name']
            price = mobo['price']
            mem_slot = mobo['memory_slots']
            socket_type = mobo['socket']
            form_factor = mobo['form_factor']

            if MOBO.query.filter_by(model=model).first() is None: #get rid of dupes
                mobo_item = MOBO(model=model, price=price,mem_slot=mem_slot, socket_type=socket_type, form_factor=form_factor)
                db.session.add(mobo_item)


    with open('flaskr/parts_json/video-card.json', "r") as f:
    
        data = json.load(f)
        
        for gpu in data:
            name = gpu['name']
            price = gpu['price']
            chipset = gpu['chipset']
            mem = gpu['memory']
            core_clock = gpu['core_clock']
            gpu_len = gpu['length']

            model = name + " " + chipset 

            if GPU.query.filter_by(model=model).first() is None: #get rid of dupes
                gpu_item = GPU(model=model, price=price, chipset=chipset, mem=mem, core_clock=core_clock, gpu_len=gpu_len)
                db.session.add(gpu_item)


    with open('flaskr/parts_json/memory.json', "r") as f:
    
        data = json.load(f)
        
        for ram in data:
            model = ram['name']
            price = ram['price']
            speed = ram['speed']
            modules = ram['modules']
            cas_latency = ram['cas_latency']

            if isinstance(speed, list):
                for i in range(len(speed)):
                    
                    speed[i] = str(speed[i])
                    
                
                speed_str = ','.join(speed)
            else:
                speed_str = str(speed)
            
            if isinstance(modules, list):
                for i in range(len(modules)):
                    
                    modules[i] = str(modules[i])
                    
                
                modules_str = ','.join(modules)
            else:
                modules_str = str(modules)



            if RAM.query.filter_by(model=model).first() is None: #get rid of dupes
                ram_item = RAM(model=model, price=price, speed=speed_str, modules=modules_str, cas_latency=cas_latency)
                db.session.add(ram_item)


    with open('flaskr/parts_json/internal-hard-drive.json', "r") as f:
    
        data = json.load(f)
        
        for drive_item in data:
            model = drive_item['name']
            price = drive_item['price']
            capacity = drive_item['capacity']
            drive_type = drive_item['type']
            interface = drive_item['interface']

            if DRIVE.query.filter_by(model=model).first() is None: #get rid of dupes
                drive_item = DRIVE(model=model, price=price, capacity=capacity, drive_type=drive_type, interface=interface)
                db.session.add(drive_item)


    with open('flaskr/parts_json/power-supply.json', "r") as f:
    
        data = json.load(f)
        
        for psu in data:
            model = psu['name']
            price = psu['price']
            form_factor = psu['type']
            effi = psu['efficiency']
            wattage = psu['wattage']
            mod = psu['modular']

            if PSU.query.filter_by(model=model).first() is None: #get rid of dupes
                psu_item = PSU(model=model, price=price, form_factor=form_factor, effi=effi, wattage=wattage, mod=mod)
                db.session.add(psu_item)


    with open('flaskr/parts_json/case.json', "r") as f:
    
        data = json.load(f)
        
        for case_item in data:
            model = case_item['name']
            price = case_item['price']
            type = case_item['type']
            color = case_item['color']
            side_panel = case_item['side_panel']

            if CASE.query.filter_by(model=model).first() is None: #get rid of dupes
                case_item = CASE(model=model, price=price, type=type, color=color, side_panel=side_panel)
                db.session.add(case_item)

        
    with open('flaskr/parts_json/case-fan.json', "r") as f:
    
        data = json.load(f)
        
        for fan in data:
            model = fan['name']
            price = fan['price']
            size = fan['size']
            rpm = fan['rpm']

            if isinstance(rpm, list):
                for i in range(len(rpm)):
                    
                    rpm[i] = str(rpm[i])
                    
                
                rpm_str = ','.join(rpm)
            else:
                rpm_str = str(rpm)

            if FANS.query.filter_by(model=model).first() is None: #get rid of dupes
                fan_item = FANS(model=model, price=price, size=size, rpm = rpm_str)
                db.session.add(fan_item)

    db.session.commit()
