from .communications.address import com_address
from .communications.admin import com_admin
from .communications.authentication import com_auth
from .communications.cart import com_cart
from .communications.deliveries import com_del
from .communications.invetory import com_inv
from .communications.orders import com_ord
from .communications.payments import com_pay
from .communications.products import com_prod
from .communications.user import com_user

from .automobile_routes import aut_routes
from .fashion_routes import fas_routes
from .health_routes import hea_routes
from .finance_routes import fin_routes

def register_blueprint(app):
    """
    This function registers all blueprints
    """
    #Blueprint registration for all IT& Communications related routes
    app.register_blueprint(com_address,url_prefix="/communications/address")
    app.register_blueprint(com_admin,url_prefix="/communications/admin")
    app.register_blueprint(com_auth,url_prefix="/communications/auth")
    app.register_blueprint(com_cart,url_prefix="/communications/cart")
    app.register_blueprint(com_del,url_prefix="/communications/delivery")
    app.register_blueprint(com_inv,url_prefix="/communications/inventory")
    app.register_blueprint(com_ord,url_prefix="/communications/orders")
    app.register_blueprint(com_pay,url_prefix="/communications/payment")
    app.register_blueprint(com_prod,url_prefix="/communications/products")
    app.register_blueprint(com_user,url_prefix="/communications/user")
    # End of IT and Communications routes

    app.register_blueprint(aut_routes)
    app.register_blueprint(fas_routes)
    app.register_blueprint(hea_routes)
    app.register_blueprint(fin_routes)
    return app
