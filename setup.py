from setuptools import setup, find_packages

setup(
    name='ModelSleuth',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'modelsleuth=main:main',  # Command to run your CLI tool
        ],
    },
    install_requires=[],
    python_requires='>=3.6',
    author="Ritabrata Chakraborty",
    author_email="ritabrata04@gmail.com",
    description="A CLI tool to analyze Python files for models and extract detailed information.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Ritabrata04/ModelSleuth",  # Your project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
