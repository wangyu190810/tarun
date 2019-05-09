
from setuptools import setup


setup(
    name='tarun',
    version='0.1.1',
    packages=['tarun'],
    url='https://github.com/wangyu190810/tarun',
    license='MIT',
    author='22too',
    entry_points={
            "console_scripts":"""
                tarun = tarun.run:main
            """,
        },
    author_email='info@22too.com',
    description='Extract many style file',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
