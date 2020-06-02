## This file is for configuration. Here you configure the git repository path, the name of the cookiecutter.json file
# and the generation of the help file.

git_repo_download_url = "https://raw.githubusercontent.com/indigo-dc/cookiecutter-data-science/"
git_repo_url = "https://github.com/indigo-dc/cookiecutter-data-science/"
branch_name = "master/"
cookiecutter_template = "cookiecutter.json"

download_url = git_repo_download_url + branch_name + cookiecutter_template

cookie_json_dir = "app/files/" + cookiecutter_template
help_json_dir = "app/files/" + cookiecutter_template.split('.')[0] + "-help.json"

zip_name = "deep_project"