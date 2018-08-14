import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="safevid_pkg",
    version="0.0.1",
    author="Yeahia Sarker",
    author_email="goyeahia@gmail.com",
    description="An encrypted full duplex video transmission package for local network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/goyeahia/SafeVid",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
