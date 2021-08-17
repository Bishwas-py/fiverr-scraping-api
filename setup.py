from setuptools import setup

setup(
    name="fiverr-api",
    version="0.0.1",
    description="Fiverr API - This Fiverr scrapping API is capable of getting all the info from a gig in Fiverr.",
    url="https://github.com/Bishwas-py/fiverr-scraping-api",
    author="Bishwas Bhandari",
    author_email="bishwasbh@gmail.com",
    py_modules=["fiv_api"],
    package_dir={'':'src'},
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
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