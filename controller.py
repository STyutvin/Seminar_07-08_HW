import inp
import imp
import exp

def start():
    if inp.choosing_mode() == '1':
        info = inp.choose_invitation()
        exp.read_info(info)
    else:
        info = inp.record_invitation()
        imp.record_data(info)