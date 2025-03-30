from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculadora",
    version="0.0.1",
    author="Homero Neto",
    author_email="homerobneto@hotmail.co.uk",
    description="retorna operações básicas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bNetoH/simple-package-template/tree/desafio-dio-pypi-distr-pkg",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
