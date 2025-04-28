from flask import Flask, render_template, request
import os
import json
import sqlite3

def save_order(order):
    con = sqlite3.connect("orders.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO orders(name, form, flavor, topping) VALUES(?,?,?,?);",
        (order["name"], order["form"], order["flavor"], order["topping"]),
    )
    con.commit()
    return

def get_orders():
    con = sqlite3.connect("orders.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()

    return rows

def read_menu(filename):
    with open(filename, "r", encoding="utf-8") as f:
        temp = f.readlines()
    result = []
    for item in temp:
        new_item = item.strip()
        result.append(new_item)
    return result

forms = read_menu("forms.txt")
flavors = read_menu("flavors.txt")
toppings = read_menu("toppings.txt")

con = sqlite3.connect("orders.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS orders(name, form, flavor, topping);")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        new_order = {"name": request.form["name"],
                     "form": request.form["form"],
                     "flavor": request.form["flavor"],
                     "topping": request.form["topping"]
                     }

        save_order(new_order)
        return render_template(
            "print.html", new_order=new_order
        )
    return render_template("order.html", forms=forms, flavors=flavors, toppings=toppings)

@app.route("/list", methods=["GET"])
def list():
    orders = get_orders()
    return render_template("list.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)