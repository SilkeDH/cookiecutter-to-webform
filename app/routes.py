from flask import render_template, request, Response
from app.form2cookie import call_cookiecutter, read_json
import app.config as cfg
from app import app
import os

@app.route('/')
def my_form():
    data = read_json()
    return render_template('index.html', data = data)

@app.route('/', methods =["POST"])
def cookieweb():
    result = request.form
    call_cookiecutter(result)
    with open(cfg.zip_name + ".zip", 'rb') as f:
        data = f.readlines()
    os.remove(cfg.zip_name + ".zip")
    return Response(data, headers={
        'Content-Type': 'application/zip',
        'Content-Disposition': 'attachment; filename=%s;' % cfg.zip_name + ".zip"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
