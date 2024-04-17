from setuptools import setup

setup(
    name="PySwitchmate",
    packages=["switchmate2"],
    install_requires=["bleak"],
    version="1.0",
    description="A library to communicate with Switchmate",
    author="JeffDaniel Hjelseth Hoyer",
    url="https://github.com/lawrence-jeff/pySwitchmate/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
