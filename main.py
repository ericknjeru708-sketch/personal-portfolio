import importlib


try:
    flask = importlib.import_module("flask")
except ModuleNotFoundError as error:
    raise RuntimeError(
        "Flask is required. Install it with: python -m pip install flask"
    ) from error

Flask = flask.Flask
render_template = flask.render_template

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="app/static"      # ← tell Flask where your CSS is
)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
