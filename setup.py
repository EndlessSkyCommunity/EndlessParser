import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="EndlessParser",
    version="0.2",
    description="A robust Parser for Endless Sky's data files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EndlessSkyCommunity/EndlessParser",
    author="MCOfficer",
    author_email="mcofficer@gmx.de",
    license="GPL3",
    packages=setuptools.find_packages(),
    zip_safe=False,
    python_requires=">=3.7",
)
