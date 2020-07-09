# Cookiecutter to webform

This application buils a webform for a given cookiecutter template where the user fills in the requirements and when submited, returns a zip file containing the file architecture build with the specified cookiecutter template.
 
The cookiecutter-to-webform application is a Python application built with [Flask](http://flask.pocoo.org/).

The docker image uses [Gunicorn](https://gunicorn.org/) as WSGI HTTP server to serve the Flask Application.

# Running the application

You can either clone the project and run it:
```
python3 cookiecutterform.py
```
or you can download the [docker image](https://hub.docker.com/repository/docker/silked/cookie2webform) with:
```
docker run -p 5001:5001 silked/cookie2webform:latest
```
then go to `http://0.0.0.0:5001/` to find the webform.

# Configuration

To determine the cookiecutter template to be transformed as a webform, first you need to specify where it is located. For that the [config.py](https://github.com/SilkeDH/cookiecutter-to-webform/blob/master/app/config.py) file must be changed. The following parameters must need to be changed in order to find the template:

| Parameter name  | Description | Mandatory (Y/N) | Default Value 
| -------------- | ------------- |------------- |------------- |
| git_repo_download_url | Download url of git repo containing the cookiecutter json file. | Y | N/A
| git_repo_url | Normal url of git repo containing the cookiecutter json file. | Y | N/A
| branch_name | Branch name of the git repo containing the cookiecutter json file.  | Y | N/A
| cookiecutter_template | Name of the cookiecutter .json file. | Y | N/A

If you want a "cleaner" webform, e.g. add a better description, you can also manually add a "help" file. This file must have the same name as you cookiecutter json file with the suffix "-help" to be found. For example, if you template is called `cookiecutter.json`, the help file name would be `cookiecutter-help.json`.

# Flowchart

The application works as following:



The functions showed in the flowchart are called in the [routes.py](https://github.com/SilkeDH/cookiecutter-to-webform/blob/master/app/routes.py) file.

# Notes

This application only downloads the cookiecutter json file. If it is manually provided in the files, it will be deleted. This is because if the cookiecutter json file is modified in the git repository, the changes will be automatically visible in the webform.



