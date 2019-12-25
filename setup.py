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
    license="GPLv3+",
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.7",
)
