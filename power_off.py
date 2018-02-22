#!/usr/bin/python3

class misMatchFlagError(Exception):
    """Raised when flag did not match"""
    pass


def shutOff():
    import dbus
    sys_bus = dbus.SystemBus()
    lg = sys_bus.get_object('org.freedesktop.login1','/org/freedesktop/login1')
    pwr_mgmt =  dbus.Interface(lg,'org.freedesktop.login1.Manager')
    shutdown_method = pwr_mgmt.get_dbus_method("PowerOff")
    shutdown_method(True)


def power_flag(flag):
    """Set Your Flag loose, follow, strict"""
    try:
        if flag == 'loose':
            return 30
        elif flag == 'follow':
            return 15
        elif flag == 'strict':
            return 3
        else :
            raise misMatchFlagError
    except misMatchFlagError as me:
        return "Flag Did not match give any one from this 'loose' or 'follow' or 'strict'"


def activity(*args,**kwargs):
    s= args
    return list(set([x for x in s[0] if s[0].count(x) > s[1]-1]))


