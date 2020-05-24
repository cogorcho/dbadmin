import datetime

def init(app): 
    print("Inicializacion")
    app.config['ENV'] = 'desarrollo'
    app.config['SECRET_KEY'] = 'Pisculichi'
    app.config['DEBUG'] = 'True' 
    app.config['TESTING'] = 'False' 
    app.config['PROPAGATE_EXCEPTIONS'] = None 
    app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = None 
    app.config['PERMANENT_SESSION_LIFETIME'] = 'datetime.timedelta(31)' 
    app.config['USE_X_SENDFILE'] = 'False' 
    app.config['SERVER_NAME'] = None 
    app.config['APPLICATION_ROOT'] = '/' 
    app.config['SESSION_COOKIE_NAME'] = 'session' 
    app.config['SESSION_COOKIE_DOMAIN'] = None 
    app.config['SESSION_COOKIE_PATH'] = None 
    app.config['SESSION_COOKIE_HTTPONLY'] = 'True' 
    app.config['SESSION_COOKIE_SECURE'] = 'False' 
    app.config['SESSION_COOKIE_SAMESITE'] = None 
    app.config['SESSION_REFRESH_EACH_REQUEST'] = 'True' 
    app.config['MAX_CONTENT_LENGTH'] = None 
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(0, 43200) 
    app.config['TRAP_BAD_REQUEST_ERRORS'] = None 
    app.config['TRAP_HTTP_EXCEPTIONS'] = 'False' 
    app.config['EXPLAIN_TEMPLATE_LOADING'] = 'False' 
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    app.config['JSON_AS_ASCII'] = 'True' 
    app.config['JSON_SORT_KEYS'] = 'True' 
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = 'False' 
    app.config['JSONIFY_MIMETYPE'] = 'application/json' 
    app.config['TEMPLATES_AUTO_RELOAD'] = None 
    app.config['MAX_COOKIE_SIZE'] = '4093' 
    app.config['LOGLEVEL'] = 'INFO'
    app.config['LOGDIR'] = 'log'
    app.config['CLIENTE'] = 'MySQL'
    app.config['TEMA'] = 'Dark'
    app.config['LOGFMT'] = '%(asctime)s %(message)s'
    app.config['LOGDATEFMT'] = '%Y/%m/%d-%I%M%S-%p'
    app.config['DBHOST'] = 'localhost'
    app.config['DBAPPUSER'] = 'tusi3'
    app.config['DBAPPPWD'] = 'tusi3-2020'
    app.config['DBAPPDB'] = 'tusi3'
    app.config['DBCHARSET'] = 'utf8'
    app.config['DBUSE_UNICODE'] = 'True'
    app.config['INTENTOS_DE_CONEXION'] = 5
    app.config['DBROOTUSER'] = 'root'
    app.config['DBROOTPWD'] = 'neheik'
    app.config['DBNAMEROOT'] = 'mysql'
    app.config['POOLNAME'] = 'adminpool'
    app.config['POOLSIZE'] = 5

