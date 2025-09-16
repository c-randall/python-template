# python-template

This repo helps set up the base elements for a Python project, including all the boilerplate for issue templates, sphinx documentation, nox, etc. To get started you need to install the `cookiecutter` package. Afterward, you can download the template and fill in the details when prompted.

```
pip install cookiecutter
cookiecutter https://github.com/c-randall/python-template
```

You will be prompted to enter information about the project and author. These details will be copied into the template in multiple places, be careful and avoid typos. The descriptions of each field are described below.

* project_slug: repository name
* project_name: human-facing name
* package_name: python import name
* author_name: author's name
* author_email: author's email

After you have completed these steps you should have a template repo set up on your computer for your new project. However, you will want to set up some additional details in some areas. Specifically, the `pyproject.toml` file will need to know which dependencies your project requires. Additionally you may want to uncomment and fill in some of the details left blank. You will also want to add your source code in `src/{{ package_name }}` where `{{ package_name }}` is the name you specified. The `tests` folder will also need to be filled in as you develop your package. In order to install all the developer tools and set up your basic package, run the following.

```
pip install -e .[dev]
```

This command installs your empty package in editable mode and gets the developer packages installed so the `nox` commands work correctly. You should re-run this command any time you 
