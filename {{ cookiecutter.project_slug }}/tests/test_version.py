import {{ cookiecutter.package_name }}


def test_development_version():
    assert 'dev' in {{ cookiecutter.package_name }}.__version__
    