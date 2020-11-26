import os

from flask import (
    Flask,
    render_template,
)
from flask_bootstrap import Bootstrap

from forms import GeneratorForm
from utils import generate_image


app = Flask(__name__)
app.config["SECRET_KEY"] = (
    os.environ.get("SECRET_KEY") or "this-is-super-random-and-crazy"
)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def index():
    form = GeneratorForm()
    if form.validate_on_submit():
        return generate_image(form.caller_id.data)
    return render_template("index.html", title="Home", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
