from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "canteen_secret_key_2024"

# ==================================================
#                  DEMO ADMIN LOGIN
# ==================================================
# Hardcoded demo credentials - no database, no user table.
# Change these before using this anywhere real.
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "canteen123"

# ==================================================
#                IN-MEMORY DATA STORE
# ==================================================
# Everything lives in plain Python lists/dicts while
# the Flask dev server is running. No database at all.

menu = [
    {"id": 1, "name": "Veg Burger",   "category": "Snacks", "price": 60},
    {"id": 2, "name": "French Fries", "category": "Snacks", "price": 50},
    {"id": 3, "name": "Cold Coffee",  "category": "Drinks", "price": 70},
    {"id": 4, "name": "Masala Dosa",  "category": "Meals",  "price": 90},
    {"id": 5, "name": "Veg Thali",    "category": "Meals",  "price": 120},
    {"id": 6, "name": "Tea",          "category": "Drinks", "price": 20},
]
next_menu_id = 7

orders = []        # list of dicts: id, student_name, items, total, status
next_order_id = 1


# ==================================================
#                     HELPERS
# ==================================================

def get_cart():
    """Cart is stored in the Flask session (signed cookie) as {item_id: qty}."""
    if "cart" not in session:
        session["cart"] = {}
    return session["cart"]


def get_item(item_id):
    for item in menu:
        if item["id"] == item_id:
            return item
    return None


def get_categories():
    cats = []
    for item in menu:
        if item["category"] not in cats:
            cats.append(item["category"])
    return cats


def admin_login_required(view_func):
    """Blocks access to a view unless session['is_admin'] is True."""
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if not session.get("is_admin"):
            flash("Please log in to access the admin panel.")
            return redirect(url_for("admin_login"))
        return view_func(*args, **kwargs)
    return wrapped


# ==================================================
#                  STUDENT ROUTES
# ==================================================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/menu", endpoint="menu")
def menu_page():
    selected = request.args.get("category", "All")
    items = menu if selected == "All" else [i for i in menu if i["category"] == selected]
    return render_template(
        "menu.html",
        items=items,
        categories=["All"] + get_categories(),
        selected=selected,
    )


@app.route("/add-to-cart/<int:item_id>", methods=["POST"])
def add_to_cart(item_id):
    cart = get_cart()
    key = str(item_id)
    cart[key] = cart.get(key, 0) + 1
    session["cart"] = cart
    session.modified = True
    flash("Item added to cart!")
    return redirect(request.referrer or url_for("menu"))


@app.route("/cart", endpoint="cart")
def cart_page():
    cart = get_cart()
    cart_items = []
    total = 0
    for item_id_str, qty in cart.items():
        item = get_item(int(item_id_str))
        if item:
            subtotal = item["price"] * qty
            total += subtotal
            cart_items.append({**item, "qty": qty, "subtotal": subtotal})
    return render_template("cart.html", cart_items=cart_items, total=total)


@app.route("/update-cart/<int:item_id>", methods=["POST"])
def update_cart(item_id):
    cart = get_cart()
    key = str(item_id)
    action = request.form.get("action")
    if key in cart:
        if action == "increase":
            cart[key] += 1
        elif action == "decrease":
            cart[key] -= 1
            if cart[key] <= 0:
                del cart[key]
    session["cart"] = cart
    session.modified = True
    return redirect(url_for("cart"))


@app.route("/remove-from-cart/<int:item_id>", methods=["POST"])
def remove_from_cart(item_id):
    cart = get_cart()
    key = str(item_id)
    if key in cart:
        del cart[key]
    session["cart"] = cart
    session.modified = True
    flash("Item removed from cart.")
    return redirect(url_for("cart"))


@app.route("/place-order", methods=["POST"])
def place_order():
    global next_order_id
    cart = get_cart()
    student_name = request.form.get("student_name", "").strip() or "Guest"

    if not cart:
        flash("Your cart is empty!")
        return redirect(url_for("cart"))

    order_items = []
    total = 0
    for item_id_str, qty in cart.items():
        item = get_item(int(item_id_str))
        if item:
            subtotal = item["price"] * qty
            total += subtotal
            order_items.append({
                "name": item["name"], "qty": qty,
                "price": item["price"], "subtotal": subtotal,
            })

    order = {
        "id": next_order_id,
        "student_name": student_name,
        "order_items": order_items,
        "total": total,
        "status": "Pending",
    }
    orders.append(order)
    next_order_id += 1

    session["cart"] = {}
    session["last_order_id"] = order["id"]
    session.modified = True

    flash(f"Order placed successfully! Your Order ID is #{order['id']}")
    return redirect(url_for("orders"))


@app.route("/orders", endpoint="orders")
def orders_page():
    last_order_id = session.get("last_order_id")
    return render_template("orders.html", orders=orders, last_order_id=last_order_id)


# ==================================================
#                   ADMIN ROUTES
# ==================================================

@app.route("/admin/login", methods=["GET", "POST"], endpoint="admin_login")
def admin_login_view():
    if session.get("is_admin"):
        return redirect(url_for("admin_page"))

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["is_admin"] = True
            session.modified = True
            flash("Logged in as admin.")
            return redirect(url_for("admin_page"))
        else:
            flash("Invalid username or password.")

    return render_template("admin_login.html")


@app.route("/admin/logout", endpoint="admin_logout")
def admin_logout_view():
    session.pop("is_admin", None)
    session.modified = True
    flash("Logged out.")
    return redirect(url_for("admin_login"))


@app.route("/admin")
@admin_login_required
def admin_page():
    return render_template("admin.html", menu=menu, orders=orders, categories=get_categories())


@app.route("/admin/add-item", methods=["POST"])
@admin_login_required
def admin_add_item():
    global next_menu_id
    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip()
    price = request.form.get("price", "")

    if name and category and price:
        try:
            price = int(price)
            menu.append({"id": next_menu_id, "name": name, "category": category, "price": price})
            next_menu_id += 1
            flash(f"'{name}' added to menu.")
        except ValueError:
            flash("Price must be a number.")
    else:
        flash("Please fill all fields.")
    return redirect(url_for("admin_page"))


@app.route("/admin/remove-item/<int:item_id>", methods=["POST"])
@admin_login_required
def admin_remove_item(item_id):
    global menu
    menu = [i for i in menu if i["id"] != item_id]
    flash("Item removed from menu.")
    return redirect(url_for("admin_page"))


@app.route("/admin/update-status/<int:order_id>", methods=["POST"])
@admin_login_required
def admin_update_status(order_id):
    new_status = request.form.get("status")
    for order in orders:
        if order["id"] == order_id:
            order["status"] = new_status
            break
    flash(f"Order #{order_id} status updated to {new_status}.")
    return redirect(url_for("admin_page"))


if __name__ == "__main__":
    app.run(debug=True)
