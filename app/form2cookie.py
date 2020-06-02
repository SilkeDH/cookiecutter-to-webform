from cookiecutter.main import cookiecutter
import app.config as cfg
import os
import shutil
import json
import requests

def read_json():
    if os.path.exists(cfg.cookie_json_dir):
        os.remove(cfg.cookie_json_dir)

    download_cookiejson()
    f = open(cfg.cookie_json_dir, "r")

    # Reading from file
    cookie_data = json.loads(f.read())
    data = []

    # If cookiecutter-help.json exists then combine it with the cookiecutter placeholders
    if os.path.exists(cfg.help_json_dir):
        f = open(cfg.help_json_dir, "r")
        help_data = json.loads(f.read())
        for key, dsc in help_data.items():
            data.append([key, dsc, cookie_data[key]])

    # If not, just use the plain cookiecutter.json file
    else:
        for key, value in cookie_data.items():
            data.append([key,value])

    return data

def download_cookiejson():
    response = requests.get(cfg.download_url)
    with open(cfg.cookie_json_dir, mode='wb') as file:
        file.write(response.content)


def call_cookiecutter(form):
    with open(cfg.cookie_json_dir, 'r') as file:
        json_data = json.load(file)
        for key, value in form.items():
            if value!= "" and key != "submit":
                    json_data[key] = value

    # create a temp directory
    owd_parent = os.getcwd()
    os.mkdir('Deep_Project')

    # switch to that temp directory
    os.chdir('Deep_Project')
    owd_child = os.getcwd()

    # call cookiecutter
    cookiecutter(cfg.git_repo_url, no_input=True, extra_context=json_data)
    os.chdir(owd_parent)
    shutil.make_archive(cfg.zip_name, 'zip', 'Deep_Project')
    shutil.rmtree(owd_child)




