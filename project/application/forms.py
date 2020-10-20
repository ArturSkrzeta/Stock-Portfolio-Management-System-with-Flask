from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class StockForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    open = StringField('Open Date', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    commission = FloatField('Commision', validators=[DataRequired()])
    signal = StringField('Signal', validators=[DataRequired()])
    close = StringField('Close Date')
    roi = FloatField('ROI')
    comments = StringField('Comments', validators=[DataRequired()])
    enter = SubmitField('Enter')
