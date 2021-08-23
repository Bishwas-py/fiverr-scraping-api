from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="fiverr-api",
    version="0.0.8",
    description="Fiverr API - This Fiverr scrapping API is capable of getting all the info from a gig in Fiverr.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bishwas-py/fiverr-scraping-api",
    author="Bishwas Bhandari",
    author_email="bishwasbh@gmail.com",
    py_modules=["fiverr_api"],
    package_dir={'':'src'},
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires = [
        "beautifulsoup4 ~= 4.9.3",
        "bs4 ~= 0.0.1",
        "certifi ~= 2021.5.30",
        "charset-normalizer ~= 2.0.4",
        "html5lib ~= 1.1",
        "idna ~= 3.2",
        "random-user-agent ~= 1.0.1",
        "requests ~= 2.26.0",
        "six ~= 1.16.0",
        "soupsieve ~= 2.2.1",
        "urllib3 ~= 1.26.6",
        "webencodings ~= 0.5.1"
    ],
    extras_require = {
        "dev": [
            "pytest>=3.7",
            "check-manifest"
        ]
    }
)