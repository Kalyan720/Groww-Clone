from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/Main")
def MainPage():
    return render_template("navbar.html")

@app.route("/MutualFunds")
def Funds():
    return render_template("MutualFunds.html")
if __name__ == "__main__":   # added: prevents auto-run on import
    app.run(debug=True)