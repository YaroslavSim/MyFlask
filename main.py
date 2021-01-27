from flask import Flask, render_template
import requests
import json
import os.path

app = Flask(__name__, template_folder='template')


def check_exchange_rates(currency_type):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json  = response.json()
    rates = response_json['rates'][currency_type]
    return float(rates)


def write_result_to_file(name_file, data):
    with open(name_file, 'a') as file:
        file.write("{}\n".format(data))


def check_exchange_result(amount, exchange_rates, currency_to):
    result = round(amount * exchange_rates, 2)
    data_to_file = "{},{},{},{}".format(currency_to, exchange_rates, amount, result)
    write_result_to_file('history.log', data_to_file)
    return f'You received: <b>{result}</b>'


@app.route('/')
def index():
    return 'A web application that converts a certain amount of EUR into various currencies!'


@app.route('/eur_to_usd/<float:amount>')
@app.route('/eur_to_usd/<int:amount>')
def get_eur_to_usd(amount):
    currency_to = 'USD'
    exchange_rates = check_exchange_rates(currency_to)
    return check_exchange_result(amount, exchange_rates, currency_to)


@app.route('/eur_to_gbp/<float:amount>')
@app.route('/eur_to_gbp/<int:amount>')
def get_eur_to_gbp(amount):
    currency_to = 'GBP'
    exchange_rates = check_exchange_rates('GBP')
    return check_exchange_result(amount, exchange_rates, currency_to)


@app.route('/eur_to_php/<float:amount>')
@app.route('/eur_to_php/<int:amount>')
def get_eur_to_php(amount):
    currency_to = 'PHP'
    exchange_rates = check_exchange_rates('PHP')
    return check_exchange_result(amount, exchange_rates, currency_to)


@app.route('/history/')
def show_file_history():
    name_file = 'history.log'
    if os.path.isfile(name_file) is False:
        return f'History file is missing!'
    if os.path.isfile(name_file) is True:
        with open(name_file,"r") as file:
            content = file.readlines()
            return render_template('history.html', content=content)


if __name__ == '__main__':
    app.run()