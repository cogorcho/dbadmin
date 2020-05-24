import sys
import os

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from mysql.connector import FieldType
from mysql.connector import FieldFlag

import logging
import modulos.Config as cfg
import modulos.util as utl

logger = logging.getLogger(__name__)
logger.info("Creando DB Pool. %s" % (__name__))

cfg = None

cnx = None

intentos_de_conexion = None

def create_pool():
    global cnx
    global intentos_de_conexion 
        
    try:
        # Inicializador
        intentos_de_conexion = get_config('INTENTOS_DE_CONEXION')

        dbconfig = {
            "host" : get_config('DBHOST'),
            "database" : get_config('DBNAMEROOT'),
            "user":     get_config('DBROOTUSER'),
            "password" : get_config('DBROOTPWD'),
            "charset" : get_config('DBCHARSET'),
            "use_unicode" : get_config('DBUSE_UNICODE')
        }

        if cnx is None:

            cnx = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = get_config('POOLNAME'), 
                pool_size = get_config('POOLSIZE'), 
                **dbconfig)

        logger.info("%s: Connection Pool OK" % (__name__))
    except Exception as e:
        print("Exception ", str(e))
        logger.critical("Connection Pool: %s" % (str(e)))

def get_connection():
    msg = ""
    for i in range(intentos_de_conexion):
        try:
            return cnx.get_connection()
        except Exception as e:
            msg = "%s get_connection(%d) %s" % (__name__, i, str(e))
            logger.error(msg)
    return None
    
def gen_data(rows, cols):
    data = []
    encoding = "utf-8"
    on_errors = "replace"

    for row in rows:
        d = {}
        for i in range(len(row)):
            d[cols[i][0]] = row[i]
        data.append(d)
    return data #utl.gen_json(data)

def get_data(storedproc, args=()):
    print('get_data', args, type(args))
    
    try:
        data = ""
        conn = get_connection()
        cursor = conn.cursor()  
        cursor.callproc(storedproc, (args))
        results = cursor.stored_results()   

        for result in results:       
            description = result.description        
            rows = result.fetchall()           

        cursor.close()
        conn.close()
        data = gen_data(rows, description)
        return data
    except Exception as e:
        msg = "Excepcion procesando %s.[%s]" % (storedproc, str(e))
        logger.error(msg)
        return msg

def get_cursor_description(tabla):        
    try:
        data = []
        sql = "select * from " + tabla + " limit 1"
        conn = get_connection()
        cursor = conn.cursor()  
        cursor.execute(sql)     
        row = cursor.fetchone()

        for col in cursor.description:
            nombre =  col[0]
            tipo = FieldType.get_info(col[1])
            flags = FieldFlag.get_bit_info(col[7])
            data.append({"nombre": nombre, "tipo":tipo, "flags": flags})

        cursor.close() 
        conn.close()
        return data                  
    except Exception as e:
        msg = "Excepcion procesando %s" % (tabla, str(e))
        conn.close()
        logger.error(msg)
        

def get_combo_data(tabla):
    try:
        sql = "select id, nombre from " + tabla + " limit 50"
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        description = cursor.description 
        rows = cursor.fetchall()
        return gen_data(rows, description)
    except Exception as e:
        msg = "Excepcion generando combo para %s" % (tabla, str(e))
        logger.error(msg)
        conn.close()
    finally:
        conn.close()

def get_version():
    try:
        conn = get_connection()
        cursor = conn.cursor() 
        cursor.execute("SELECT VERSION()") 
        data = cursor.fetchone() 
        if data is not None:
            return "Database version : {0}".format(data[0].encode('utf8'))
        else:
            return "Imposible obtener version de la DB"
    except Exception as e:
        msg = "Excepcion obteniendo version de ls BD: %s" % (str(e))
        logger.error(msg)
    finally:
        conn.close()

def get_proc_params(proc):
    print('db.get_proc_params', proc, database_name)
    data = get_data('GETPARAMS',(proc, database_name))
    return data

def get_config(key):
    return cfg[key]

def get_status():
    print('Database get_status', get_connection().is_connected() )
    return 'DB Ok' if get_connection().is_connected() else 'DB KO' 

#create_pool()
#status = get_connection().is_connected()