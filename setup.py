# Copyright (C) 2020 Rishabh Moudgil

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boxwine",
    version="0.0.1",
    author="Rishabh Moudgil",
    author_email="me@rishabhmoudgil.com",
    description="Turn your Wine apps into Mac apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rishabh/boxwine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS",
    ],
    install_requires=["ruamel.yaml>=0.16.10,<1", "Click>=7.1.2,<8"],
    extras_require={"dev": ["flake8", "black"], "test": ["unittest"]},
    python_requires=">=3.6",
    entry_points="""
        [console_scripts]
        boxwine=boxwine:cli
    """,
)
