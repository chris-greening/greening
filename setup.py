from setuptools import setup, find_packages

setup(
    name="greening",
    version="0.4.2",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "greening = greening.cli:main"
        ]
    },
)
