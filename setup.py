
from setuptools import setup
with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tarun',
    version='0.1.2',
    packages=['tarun'],
    url='https://github.com/wangyu190810/tarun',
    license='MIT',
    author='22too',
    entry_points={
            "console_scripts":"""
                tarun = tarun.run:main
            """,
        },
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='info@22too.com',
    description='Extract many style file',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
