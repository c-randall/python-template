# python-template

This repo helps set up a Python project, including the boilerplate for issue templates, sphinx documentation, nox, etc. The template makes use of the `cookiecutter` package to make sure details like the author and package name are updated throughout the files correctly. To get started, set up your python environment and run the following:

```
pip install cookiecutter
cookiecutter https://github.com/c-randall/python-template
```

You will be prompted to enter information about the project and author. Be careful and avoid typos. The descriptions of each field are described below.

* project_slug: repository name
* project_name: human-facing name
* package_name: python import name
* author_name: author's name
* author_email: author's email

After you have completed these steps you should have a template repo set up on your computer for your new project. However, you will want to set up some additional details in some areas. Specifically, the `pyproject.toml` file will need to know which dependencies your project requires. You may also want to uncomment and fill in some of the details left blank. After you finish updating `pyproject.toml`, run the following to install all of your dependencies, including the developer dependencies.

```
pip install -e .[dev]
```

The `-e` option will install your package in editable mode so any changes you made are automatically reflected the next time you import your package. Note that this is only true for files inside the `src` folder. If you add dependencies to `pyproject.toml` then you will need to re-install your package. You can re-use the command above to do this. 

# Developer tools
One benefit of using this template over over project environment managers is that is comes set up to use `sphinx` to build your documentation. Additionally there are `nox` commands that can help you perform linting and spellchecks on your code. All of the developer tools are run using `nox` to make the commands shorter and easier to remember. You can get a full list of the `nox` sessions by running `nox -l` in your terminal. Any of the listed sessions can then be run using `nox -s {{ session }} -- {{ options }}` where `{{ session }}` and `{{ options }}` are placeholders for the specific session and options you want to run. A few common examples are given below.

* `nox -s docs -- clean` - Build your documentation, after deleting any old build files.
* `nox -s pre-commit -- write format` - Run the linter, spellcheck, and tests. Autoformat any issues (if possible) that conflict with the linter, and write any spelling corrections directly.

The best way to get more information on any of the `nox` sessions and options is to look at the `noxfile.py` file.
