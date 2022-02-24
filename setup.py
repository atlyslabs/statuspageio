import os

from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="statuspageio",
    version="0.1.1",
    description="StatusPage.io API V1 library client for Python",
    long_description=README,
    author="Grant Delaney",
    url="https://github.es.ecg.tools/gdelaney/statuspageio",
    license="MIT",
    packages=["statuspageio"],
    install_requires=["requests", "munch"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
