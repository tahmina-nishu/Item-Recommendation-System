from flask import Flask, render_template, request
import json
from knapsack import knapsack

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    with open("data/items.json") as f:
        all_items = json.load(f)
    recommended_items = []
    total_value = 0

    if request.method == "POST":
        try:
            budget = int(request.form["budget"])
            total_value, recommended_items = knapsack(all_items, budget)
        except:
            pass

    return render_template("index.html",
                           all_items=all_items,
                           items=recommended_items,
                           value=total_value)

if __name__ == "__main__":
    app.run(debug=True)

