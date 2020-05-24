import modulos.monitor as monitor
import modulos.Config as cfg
import modulos.Database as db
from flask import Flask, render_template
import json

app = Flask(__name__)

cfg.init(app)

monitor.cfg = app.config
db.cfg = app.config
db.create_pool()
monitor.db = db

@app.route('/')
def index():
    return render_template('index.html', data={})

@app.route('/favicon.ico')
def favico():
    return 'OK'

@app.errorhandler(404) 
def not_found(e): 
# defining function 
  return render_template("404.html") 

@app.route('/version')
def version():
    rows = monitor.version()
    data = {
        "titulo":"Mysql DB Version",
        "campos":rows[0]
    }
    return render_template('keyvalue.html', data=data)

@app.route('/ping')
def ping():
    row = {"ping" : monitor.ping()}
    data = {
        "titulo":"Mysql DB Ping",
        "campos":row
    }
    return render_template('keyvalue.html', data=data)

@app.route('/status')
def status():
    rows = monitor.status()
    data = {
        "titulo":"Mysql DB Status",
        "campos":rows[0]
    }
    return render_template('keyvalue.html', data=data)

@app.route('/extendedstatus')
def extended_status():
    rows = monitor.extended_status()
    data = {
        "titulo":"Mysql DB Extended Status",
        "campos":rows[0]
    }
    return render_template('keyvalue.html', data=data)

@app.route('/variables')
def variables():
    rows = monitor.variables()
    data = {
        "titulo":"Mysql Variables",
        "campos":rows[0]
    }
    return render_template('keyvalue.html', data=data)


@app.route('/procesos')
def procesos():
    data = {
        "titulo":"Procesos de la BD",
        "campos" : monitor.processes()
    }
    return render_template('procesos.html', data=data)

@app.route('/db')
def db():
    return monitor.db_status()

@app.route('/schemas')
def schemas():
    rows = monitor.get_schemas()
    data = {
        "titulo":"Schemas de la BD",
        "metodo":"GET",
        "campos": rows
    }
    return render_template('schemas.html', data=data)

@app.route('/tablas/<schema>')
def tablas(schema):
    rows = monitor.get_tablas(schema)
    data = {
        "titulo":"Tablas del schema %s" %(schema),
        "metodo":"GET",
        'schema':schema,
        "campos": rows
    }
    return render_template('tablas.html', data=data)

@app.route('/tabla/<schema>/<nombre>/<tipo>')
def tabla(schema, nombre, tipo):
    rows = monitor.get_columns(schema, nombre)
    data = {
        "titulo": "Estructura de la %s %s" % (tipo.lower(), nombre),
        "metodo":"GET",
        "campos":rows
    }
    return render_template('columnas.html', data=data)

@app.route('/files')
def files():
    rows = monitor.get_files()
    data = {
        "titulo": "Archivos de la BD",
        "campos": rows
    }
    return render_template('files.html', data=data)

@app.route('/users')
def users():
    rows = monitor.get_users()
    data = {
        "titulo": "Usuarios de la BD",
        "campos": rows
    }
    return render_template('users.html', data=data)

@app.route('/privs/<username>')
def privs(username):
    print('privs',username)
    rows = monitor.get_privs(username)
    #print(rows)
    data = {
        "titulo": "Privilegios del usuario %s de la BD" % (username),
        "campos": rows
    }
    return render_template('privs.html', data=data)
