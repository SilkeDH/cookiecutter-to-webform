from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "wer238aou43owu83e3rf674js4uo9cdb823r"

from app import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0')

