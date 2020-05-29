from flask import render_template, request, Response
from app.form2cookie import call_cookiecutter, read_json
import os
from app import app


@app.route('/')
def my_form():
    data = read_json()
    return render_template('index.html', data = data)

@app.route('/', methods =["POST"])
def cookieweb():
    result = request.form
    call_cookiecutter(result)
    with open("deep_project.zip", 'rb') as f:
        data = f.readlines()
    os.remove("deep_project.zip")
    return Response(data, headers={
        'Content-Type': 'application/zip',
        'Content-Disposition': 'attachment; filename=%s;' % "deep_project.zip"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
