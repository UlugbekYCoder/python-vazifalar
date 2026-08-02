from flask import Flask, render_template, redirect, url_for
from models import *

app = Flask(__name__)

# -------------------------
# Products
# -------------------------

Management.add_product(Product("Apple", 12000, 2026, "Fruit"))
Management.add_product(Product("Banana", 8000, 2026, "Fruit"))
Management.add_product(Product("Orange", 10000, 2025, "Fruit"))
Management.add_product(Product("Peach", 15000, 2026, "Fruit"))

# -------------------------
# User
# -------------------------

user = User("Anvar")


# =========================
# Routes
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# Products
# -------------------------

@app.route("/products")
def products():
    return render_template(
        "products.html",
        products=Management.products
    )


# -------------------------
# Product Details
# -------------------------

@app.route("/product/<name>")
def product(name):

    for item in Management.products:

        if item.name == name:
            return render_template(
                "product.html",
                product=item
            )

    return "Product not found"


# -------------------------
# Add To Cart
# -------------------------

@app.route("/add/<name>")
def add(name):

    for item in Management.products:

        if item.name == name:
            user.add_to_cart(item)
            break

    return redirect(url_for("cart"))


# -------------------------
# Shopping Cart
# -------------------------

@app.route("/cart")
def cart():

    return render_template(
        "cart.html",
        cart=user.cart,
        total=user.get_total()
    )


# -------------------------
# Remove Product
# -------------------------

@app.route("/remove/<name>")
def remove(name):

    for item in user.cart:

        if item.name == name:
            user.remove_from_cart(item)
            break

    return redirect(url_for("cart"))


# -------------------------
# Checkout
# -------------------------

@app.route("/checkout")
def checkout():

    return render_template(
        "checkout.html",
        cart=user.cart,
        total=user.get_total()
    )


# -------------------------
# Confirm Purchase
# -------------------------

@app.route("/confirm")
def confirm():

    user.clear_cart()

    return render_template("success.html")


# =========================
# Run
# =========================

if __name__ == "__main__":
    app.run(debug=True)