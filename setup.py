from setuptools import setup, find_packages

setup(
    name='fontfinder',
    version='0.0.1',
    author='Maximilian Nöthe',
    author_email='maximilian.noethe@tu-dortmund.de',
    packages=find_packages(),
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
)
