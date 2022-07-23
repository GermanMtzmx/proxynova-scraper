from pathlib import Path
from setuptools import find_packages, setup

dependencies = ['bs4', 'html5lib', 'pyppeteer', 'asyncio', 'unidecode']

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='proxynova_scrapper',
    packages=find_packages(),
    version='0.1',
    description='Package to get proxies from proxynova.com via web scraping',
    author='German Martinez Solis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/GermanMtzmx/proxynova_scraper",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=dependencies,
)