from setuptools import setup, find_packages

setup(
    name="smartfilesort",
    version="0.1.0",
    author="Subham Das",
    author_email="gturtle.service@gmail.com",
    description="A smart file sorting and renaming tool with  auto renaming",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/master-subham/smartfilesort",
    packages=find_packages(),
    install_requires=[
        "spacy",
        "python-magic"  # Required for file type detection
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "smartfilesort=smartfilesort.smartfilesort:organize_files"
        ]
    },
)
