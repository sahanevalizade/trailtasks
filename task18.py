from flask import Flask
from random import randint

app = Flask(__name__)

def roll_dice():
    return randint(1, 6), randint(1, 6)

def show_dice():
    d1, d2 = roll_dice()
    dice_sides = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    return f" {dice_sides[d1]} {dice_sides[d2]} "

@app.route("/")
def index():
    return f"<h1>Zarlar: {show_dice()}</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)
