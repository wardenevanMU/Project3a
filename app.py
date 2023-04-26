
from flask import Flask, redirect, request, render_template, flash, session

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True
app.config['MESSAGE_FLASH_OPTIONS'] = {'duration' : 5}

app.config['SECRET KEY'] = 'your secret key'
app.secret_key = "hello"

@app.route("/", methods=('GET', 'POST'))
def stocks(): 
    if request.method == "POST":
        symbol = request.form['symbol']
        chart_type = request.form['chart_type']
        time_series = request.form['time_series']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        if not symbol:
            flash("Symbol is required.")
            redirect('stock.html')
        elif not chart_type:
            flash("ChartType is required.")
        elif not time_series:
            flash("Time Series is required.")
        elif not start_date:
            flash("Start Date is required.")
        elif not end_date:
            flash("End Date is required.")
        else:
            flash("Saved Successfully - your graph is below!", "success")    
    return render_template("stock.html")

if __name__ == "__main__":
    app.run()