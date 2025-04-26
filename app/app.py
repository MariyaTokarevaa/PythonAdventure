from flask import Flask, render_template, request

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
        form = request.form["form"]
        print("Form: ", form)
        return render_template("print.html", form=form)

    return render_template("forms.html")

if __name__ == "__main__":
    app.run(debug=True)