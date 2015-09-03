from setuptools import setup

setup(
    name='tarun',
    version='0.1.0',
    packages=['tarun'],
    url='https://github.com/wangyu190810/tarun',
    license='MIT',
    author='22too',
    entry_points={
            "console_scripts":"""
                tarun = tarun.run:main
            """,
        },
    author_email='wo190810401@gmail.com',
    description='Extract file'
)
