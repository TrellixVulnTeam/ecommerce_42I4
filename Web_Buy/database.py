from orator import DatabaseManager
from orator import Model

config = {
    'postgres': {
        'driver': 'pgsql',
        'host': 'localhost',
        'database': 'webbuy',
        'user': 'webbuy_user',
        'password': 'webbuy12890',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)
