from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    tableau_url = "https://public.tableau.com/views/ToyCraftTalesTableausVisionintoToyManufacturerData_17711547732550/Dashboard1?:showVizHome=no&:embed=true"
    return render_template("dashboard.html", tableau_url=tableau_url)

if __name__ == "__main__":
    app.run(debug=True)
