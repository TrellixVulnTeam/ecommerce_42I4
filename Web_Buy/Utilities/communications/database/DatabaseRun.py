from orator import DatabaseManager
from orator import Model
import os,sys
from pathlib import Path
db_path = Path(os.getcwd())/"Utilities/communications/database/communications.db"

# sys.exit()
config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': str(db_path),
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)
