from flask import Flask, render_template, request
import os
import json

def save_orders(orders, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=4, ensure_ascii=False)
        f.close()

def load_orders(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            orders = json.load(f)
            f.close()
        return orders
    else:
        return []

orders = load_orders("orders.json")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<name>")
def hello(name="stranger"):
    return render_template("greeting.html", name=name)

@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        new_order = {"name": request.form["name"],
                     "form": request.form["form"],
                     "flavor": request.form["flavor"],
                     "topping": request.form["topping"]
                     }
        orders.append(new_order)
        save_orders(orders, "orders.json")
        return render_template(
            "print.html", new_order=new_order
        )

    return render_template("forms.html")

if __name__ == "__main__":
    app.run(debug=True)