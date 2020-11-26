from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class GeneratorForm(FlaskForm):
    caller_id = StringField(
        "Caller ID",
        validators=[
            validators.DataRequired(),
            validators.Length(max=12),
        ],
    )
    submit = SubmitField("Generate")
