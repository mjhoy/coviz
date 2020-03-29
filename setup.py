"""Packaging for the coviz backend."""
from setuptools import find_packages, setup


def get_version():
    """Get library version."""
    with open("VERSION") as f:
        return f.read()


setup(
    name="coviz",
    version=get_version(),
    url="",
    author="Camen and Mikey",
    author_email="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.in").readlines(),
    tests_require=open("requirements-dev.in").readlines(),
    description="Backend for COVID-19 visualization website",
    long_description="\n" + open("README.md").read(),
)
