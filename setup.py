from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'Listreqs',
    version = '0.0.5',
    description = "Listreqs is a simple requirements.txt generator. It's an alternative to pipreqs.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/soumya997/Listreqs",
    author = "Soumyadip Sarkar",
    author_email = "soumya997.sarkar@gmail.com",
    license = "MIT",
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'listreqs = listreqs.__main__:main'
        ]
    })
