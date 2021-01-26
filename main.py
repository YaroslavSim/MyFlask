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


def check_str_to_float(number):
    try:
        float(number)
        return True
    except:
        return False


def write_result_to_file(name_file, data):
    current_path = os.getcwd()
    path_file_history = os.path.join(current_path, name_file)
    if os.path.isfile(name_file) is True:
        with open(path_file_history, 'a') as file:
            file.write("{}\n".format(data))
    else:
        with open(path_file_history, 'w') as file:
            file.write("{}\n".format(data))


def check_exchange_result(status_check_str_to_float, amount, exchange_rates, currency_to):
    if status_check_str_to_float is True:
        result = round(float(amount) * exchange_rates, 2)
        data_to_file = "{},{},{},{}".format(currency_to, exchange_rates, amount, result)
        write_result_to_file('history.log', data_to_file)
        return f'You received: <b>{result}</b>'
    if status_check_str_to_float is False:
        return f'You entered an incorrect amount: <b>{amount}</b>'


@app.route('/')
def index():
    return 'A web application that converts a certain amount of EUR into various currencies!'


@app.route('/eur_to_usd/<amount>')
def get_eur_to_usd(amount):
    currency_to = 'USD'
    exchange_rates = check_exchange_rates(currency_to)
    check_enter_sum = check_str_to_float(amount)
    return check_exchange_result(check_enter_sum, amount, exchange_rates, currency_to)


@app.route('/eur_to_gbp/<amount>')
def get_eur_to_gbp(amount):
    currency_to = 'GBP'
    exchange_rates = check_exchange_rates('GBP')
    check_enter_sum = check_str_to_float(amount)
    return check_exchange_result(check_enter_sum, amount, exchange_rates, currency_to)


@app.route('/eur_to_php/<amount>')
def get_eur_to_php(amount):
    currency_to = 'PHP'
    exchange_rates = check_exchange_rates('PHP')
    check_enter_sum = check_str_to_float(amount)
    return check_exchange_result(check_enter_sum, amount, exchange_rates, currency_to)


@app.route('/history/')
def show_file_history():
    name_file = 'history.log'
    current_path = os.getcwd()
    path_file_history = os.path.join(current_path, name_file)
    if os.path.isfile(name_file) is False:
        return f'History file is missing!'
    if os.path.isfile(name_file) is True:
        with open(path_file_history,"r") as file:
            content = file.readlines()
            return render_template('history.html', content=content)


if __name__ == '__main__':
    app.run()