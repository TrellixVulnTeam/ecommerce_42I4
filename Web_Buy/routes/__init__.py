from .communications_routes import com_routes
from .automotive_routes import aut_routes
from .fashion_routes import fas_routes
from .health_routes import hea_routes
from .finance_routes import fin_routes

def register_blueprint(app):
    app.register_blueprint(com_routes)
    app.register_blueprint(aut_routes)
    app.register_blueprint(fas_routes)
    app.register_blueprint(hea_routes)
    app.register_blueprint(fin_routes)
    return app