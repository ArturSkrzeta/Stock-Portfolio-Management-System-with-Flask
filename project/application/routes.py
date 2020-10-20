from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Stock
from application.forms import StockForm

@app.route('/', methods=['GET', 'POST'])
def index():

    form = StockForm()

    stocks = Stock.query.all()

    if form.company.data:

        s = Stock(company=form.company.data,
                    open=form.open.data,
                    price=form.price.data,
                    quantity=form.quantity.data,
                    commission=form.commission.data,
                    signal=form.signal.data,
                    close="",
                    roi=0.0,
                    comments=form.comments.data)

        db.session.add(s)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html', stocks=stocks, form=form)
