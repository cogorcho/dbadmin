import os

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
    cmd = "mysqladmin -u root -pneheik extended-status  | grep -v '+---' | sed 's/ //g;  s/^|//; s/|$//'"
    data = os.popen(cmd).read().split('\n')
    return armar(data,'|')

def variables():
    cmd = "mysqladmin -u root -pneheik variables | grep -v '+---' | sed 's/ //g;  s/^|//; s/|$//'"
    data = os.popen(cmd).read().split('\n')
    return armar(data,'|')

def ping():
    cmd = "mysqladmin -u root -pneheik ping 2> /dev/null"
    data = os.popen(cmd).read()
    return data

def status():
    cmd = "mysqladmin -u root -pneheik status 2> /dev/null | sed 's/  /|/g' "
    data = os.popen(cmd).read().split('|')
    return armar(data,':')

def version():
    cmd = 'mysqladmin -u root -pneheik version  2> /dev/null | grep "Server version" | sed "s/\t/|/"'
    data = os.popen(cmd).read()
    return armar((data.strip().replace('\t',''),),'|')

def processes():
    return db.get_data('GETPROCESSES', ())
    #cmd = "mysqladmin -u root -pneheik processlist  2> /dev/null "
    #data = os.popen(cmd).read().split('\n')
    #return data

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
    print('get_privs', username)
    rows = db.get_data('GETPRIVS', (username,))
    print(rows)
    return rows