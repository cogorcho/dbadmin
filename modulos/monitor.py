import os
import modulos.Config as cfg

cfg = None
db = None

def armar(data, sep):
    dout = {}
    for e in data:
        if len(e) == 0:
            continue
        ea = e.split(sep)
        if len(ea) == 2:
            dout[ea[0]] = ea[1]
    return [dout]

def extended_status():
    cmd = "mysqladmin -u %s -p%s extended-status  | grep -v '+---' | sed 's/ //g;  s/^|//; s/|$//'" % ( 
get_config('DBROOTUSER'), get_config('DBROOTPWD'))
    data = os.popen(cmd).read().split('\n')
    return armar(data,'|')

def variables():
    cmd = "mysqladmin -u %s -p%s variables | grep -v '+---' | sed 's/ //g;  s/^|//; s/|$//'" % (get_config('DBROOTUSER'), get_config('DBROOTPWD'))
    data = os.popen(cmd).read().split('\n')
    return armar(data,'|')

def ping():
    cmd = "mysqladmin -u %s -p%s ping 2> /dev/null" % (get_config('DBROOTUSER'), get_config('DBROOTPWD'))
    data = os.popen(cmd).read()
    return data

def status():
    cmd = "mysqladmin -u %s -p%s status 2> /dev/null | sed 's/  /|/g'" % (get_config('DBROOTUSER'), get_config('DBROOTPWD'))
    data = os.popen(cmd).read().split('|')
    return armar(data,':')

def version():
    cmd = 'mysqladmin -u %s -p%s version  2> /dev/null | grep "Server version" | sed "s/\t/|/"' % (get_config('DBROOTUSER'), get_config('DBROOTPWD'))
    data = os.popen(cmd).read()
    return armar((data.strip().replace('\t',''),),'|')

def processes():
    return db.get_data('GETPROCESSES', ())

def get_config(key):
    return cfg[key]

def db_status():
    return db.get_status()

def get_schemas():
    return db.get_data('GETSCHEMAS', ())

def get_tablas(schema):
    return db.get_data('GETTABLES', (schema,))

def get_columns(schema, tabla):
    return db.get_data('GETCOLUMNS', (schema,tabla))

def get_files():
    return db.get_data('GETFILES', ())

def get_users():
    return db.get_data('GETUSERS', ())

def get_privs(username):
    rows = db.get_data('GETPRIVS', (username,))
    return rows