from setuptools import setup, find_packages

setup(
    name="python-package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Your package dependencies here
        'requests',  # Example: external dependency
        'numpy'
    ],
    description="This package is for numpy amd requests",
    author="",
    author_email="tp.email@example.com",
    url="https://github.com/JayanthSureshjfrog/devops-frogbot-examples/tree/frogbot-python/python",
)
