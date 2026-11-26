from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Margherita Pizza", "price": 299, "description": "Classic cheese and tomato pizza"},
    {"id": 2, "name": "Veg Burger", "price": 149, "description": "Crispy vegetable patty with fresh vegetables"},
    {"id": 3, "name": "Paneer Biryani", "price": 249, "description": "Fragrant rice cooked with paneer and spices"},
    {"id": 4, "name": "Chocolate Shake", "price": 129, "description": "Rich and creamy chocolate shake"},
]

cart = []

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Delivery</title>
    <style>
        * { box-sizing: border-box; }
        body { margin: 0; font-family: Arial, sans-serif; background: #fff8f1; color: #222; }
        header { background: #ff5722; color: white; padding: 20px; text-align: center; }
        main { max-width: 900px; margin: 30px auto; padding: 0 20px; }
        .menu { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; }
        .card { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 3px 10px #0001; }
        .card h3 { margin-top: 0; }
        .price { color: #ff5722; font-weight: bold; }
        button { background: #ff5722; color: white; border: 0; border-radius: 6px; padding: 10px 14px; cursor: pointer; }
        button:hover { background: #e64a19; }
        .cart { background: white; border-radius: 10px; padding: 20px; margin-top: 30px; box-shadow: 0 3px 10px #0001; }
        .cart-row { display: flex; justify-content: space-between; border-bottom: 1px solid #eee; padding: 8px 0; }
        .empty { color: #777; }
    </style>
</head>
<body>
    <header><h1>Fast Food Delivery</h1></header>
    <main>
        <h2>Menu</h2>
        <div class="menu">
            {% for item in menu %}
            <div class="card">
                <h3>{{ item.name }}</h3>
                <p>{{ item.description }}</p>
                <p class="price">₹{{ item.price }}</p>
                <form action="{{ url_for('add_to_cart') }}" method="post">
                    <input type="hidden" name="item_id" value="{{ item.id }}">
                    <button type="submit">Add to Cart</button>
                </form>
            </div>
            {% endfor %}
        </div>

        <div class="cart">
            <h2>Your Cart</h2>
            {% if cart %}
                {% for item in cart %}
                <div class="cart-row"><span>{{ item.name }}</span><span>₹{{ item.price }}</span></div>
                {% endfor %}
                <p><strong>Total: ₹{{ total }}</strong></p>
            {% else %}
                <p class="empty">Your cart is empty.</p>
            {% endif %}
        </div>
    </main>
</body>
</html>
"""


@app.route("/")
def home():
    total = sum(item["price"] for item in cart)
    return render_template_string(PAGE, menu=menu, cart=cart, total=total)


@app.route("/add", methods=["POST"])
def add_to_cart():
    item_id = int(request.form["item_id"])
    item = next((item for item in menu if item["id"] == item_id), None)
    if item:
        cart.append(item)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
