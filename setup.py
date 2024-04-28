from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fiverr-api",
    version="1.0.01",
    description="Fiverr API - Scrape Fiverr gigs, ratings, reviews, prices, profiles, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bishwas-py/fiverr-scraping-api",
    author="Bishwas Bhandari",
    author_email="yo@bishwas.net",
    py_modules=["fiverr_api"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "beautifulsoup4 ~= 4.12.2",
        "certifi ~= 2023.7.22",
        "charset-normalizer ~= 3.2.0",
        "html5lib ~= 1.1",
        "idna ~= 3.4",
        "requests ~= 2.31.0",
        "six ~= 1.16.0",
        "soupsieve ~= 2.4.1",
        "urllib3 ~= 2.0.4",
        "webencodings ~= 0.5.1"
    ]
)
