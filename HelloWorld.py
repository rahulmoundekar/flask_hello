from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = 'Rahul'
    return render_template('index.html', welcomeName=name)


app.run(debug=True)
