from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="Promit",
    author_email="promit8228@gmail.com",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'PyYAML',
        'dill'
    ]
)