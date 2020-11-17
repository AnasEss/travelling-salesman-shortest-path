##################################################################################
#                            Author: Anas ESSOUNAINI                             #
#                              File Name: setup.py                               #
#                     Creation Date: July 18, 2020 09:51 PM                      #
#                    Last Updated: November 17, 2020 03:05 AM                    #
#                            Source Language: python                             #
#  Repository: https://github.com/AnasEss/travelling-salesman-shortest-path.git  #
#                                                                                #
#                            --- Code Description ---                            #
#                                 package setup                                  #
##################################################################################

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