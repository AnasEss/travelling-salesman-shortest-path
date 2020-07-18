from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="travelling_salesman_pkg",
    version="0.0.1",
    description="Implementation of travelling salesman algorithm",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AnasEss/",
    author="Anas ESSOUNAINI, Ali MOURTADA",
    author_email="essounaini97@gmail.com, mourtada.ali1997@gmail.com ",
    keywords="meta-heuristics - travelling_salesman_algorithm  ",
    license="MIT",
    packages=[
        "travelling_salesman_pkg",
    ],
    install_requires=[],
    include_package_data=True,
)