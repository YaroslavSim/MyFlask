from flask import Flask, render_template, request
import requests
import json
import os.path
import sqlite3
from flask import g


app = Flask(__name__, template_folder='template')


DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        conn = sqlite3.connect(DATABASE)
        db = g._database = conn
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def check_exchange_rate(currency_type):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json  = response.json()
    rates = response_json['rates'][currency_type]
    return float(rates)


def write_result_to_file(name_file, data):
    with open(name_file, 'a') as file:
        file.write("{}\n".format(data))
    

def check_exchange_result(amount, exchange_rate, currency_to):
    result = round(amount * exchange_rate, 2)
    #data_to_file = "{},{},{},{}".format(currency_to, exchange_rates, amount, result)
    #write_result_to_file('history.log', data_to_file)
    write_result_to_db(currency_to, exchange_rate, amount, result)
    return f'You received: <b>{result}</b>'


@app.route('/')
def index():
    return 'A web application that converts a certain amount of EUR into various currencies!'


@app.route('/eur_to_usd/<float:amount>')
@app.route('/eur_to_usd/<int:amount>')
def get_eur_to_usd(amount):
    currency_to = 'USD'
    exchange_rate = check_exchange_rate(currency_to)
    return check_exchange_result(amount, exchange_rate, currency_to)


@app.route('/eur_to_gbp/<float:amount>')
@app.route('/eur_to_gbp/<int:amount>')
def get_eur_to_gbp(amount):
    currency_to = 'GBP'
    exchange_rate = check_exchange_rate('GBP')
    return check_exchange_result(amount, exchange_rate, currency_to)


@app.route('/eur_to_php/<float:amount>')
@app.route('/eur_to_php/<int:amount>')
def get_eur_to_php(amount):
    currency_to = 'PHP'
    exchange_rate = check_exchange_rate('PHP')
    return check_exchange_result(amount, exchange_rate, currency_to)


@app.route('/history/')
def show_file_history():
    name_file = 'history.log'
    if os.path.isfile(name_file) is False:
        return f'History file is missing!'
    if os.path.isfile(name_file) is True:
        with open(name_file,"r") as file:
            content = file.readlines()
            return render_template('history.html', content=content)


def write_result_to_db(currency_to, exchange_rate, amount, result):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    insert into exchange ('currency_to', 'exchange_rate', 'amount', 'result')
    values (?, ?, ?, ?)
    """, (currency_to, exchange_rate, amount, result))
    conn.commit()


@app.route('/history/currency/<currency_to>')
def select_history_currency(currency_to):
    connection = get_db()
    cursor = connection.cursor()
    resp = cursor.execute("""
        select currency_to, exchange_rate, amount, result
        from exchange where currency_to = ?
        """, (currency_to, ))
    resp = cursor.fetchall()
    return render_template('view_results.html', content=resp)


@app.route('/history/amount_gte/<float:number>')
@app.route('/history/amount_gte/<int:number>')
def select_history_amount(number):
    connection = get_db()
    cursor = connection.cursor()
    resp = cursor.execute("""
        select currency_to, exchange_rate, amount, result
        from exchange where amount >= ?
        """, (number, ))
    resp = cursor.fetchall()
    return render_template('view_results.html', content=resp)


@app.route('/history/statistic/')
def select_history_statistic():
    connection = get_db()
    cursor = connection.cursor()
    resp = cursor.execute("""
        select currency_to, count(*), sum(result)
        from exchange group by currency_to
        """)
    resp = cursor.fetchall()
    return render_template('view_statistic.html', content=resp)


if __name__ == '__main__':
    init_db()
    app.run()