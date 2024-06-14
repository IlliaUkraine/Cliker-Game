import os

from flask import Flask, render_template, request

app = Flask(__name__)

# Змінні для збереження кількості кліків, потужності кліка та кількості кліків для прокачки
click_count = 0
click_power = 1
upgrade_cost = 10

@app.route('/', methods=['GET', 'POST'])
def index():
    global click_count, click_power, upgrade_cost
    if request.method == 'POST':
        if 'click' in request.form:
            click_count += click_power
        elif 'upgrade' in request.form:
            if click_count >= upgrade_cost:
                click_count -= upgrade_cost
                click_power += 1
                upgrade_cost *= 2
        elif 'reset' in request.form:
            click_count = 0
            click_power = 1
            upgrade_cost = 10
    return render_template('index.html', click_count=click_count, click_power=click_power, upgrade_cost=upgrade_cost)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

