from setuptools import setup, find_packages

setup(
    name='flexarray',
    version='0.1.0',
    description='A Python library for static arrays with dynamic memory allocation like malloc, realloc, and free',
    author='Shashank Pandey',
    author_email='jpshashank200@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
