from setuptools import setup, find_packages

setup(
    name='flexarray',
    version='0.1.1',
    description='A Python library for static arrays with dynamic memory allocation like malloc, realloc, and free, and various array operations like searching, sorting, and mathematics.',
    url='https://github.com/shashankpandey04/flexarray',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
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
