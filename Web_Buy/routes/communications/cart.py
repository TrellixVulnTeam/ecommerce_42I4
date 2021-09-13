from flask import Flask, Blueprint, session, render_template, request ,redirect, jsonify
import sys


sys.path.append("../..")

from Utilities.communications.Loader import *
com_cart = Blueprint('communications_cart', __name__)
route_loader = Loader()

@com_cart.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id=0):
    # AddCart is a form from WTF forms. It has a prefix because there
    # is more than one form on the page.
    cart = AddCart(prefix="cart")

    # This is the product being viewed on the page.
    product = Product.query.get({{product_id}})


    if cart.validate_on_submit():
        # Checks to see if the user has already started a cart.
        if 'cart' in session:
            # If the product is not in the cart, then add it.
            if not any(product.name in d for d in session['cart']):
                session['cart'].append({product.name: cart.quantity.data})

            # If the product is already in the cart, update the quantity
            elif any(product.name in d for d in session['cart']):
                for d in session['cart']:
                    d.update((k, cart.quantity.data) for k, v in d.items() if k == product.name)

        else:
            # In this block, the user has not started a cart, so we start it for them and add the product.
            session['cart'] = [{product.name: cart.quantity.data}]


        return redirect(url_for('store.index'))
