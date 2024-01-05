import setuptools

# Here which opens and read the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# version of the application that is getting created
__version__ = "0.0.0"

# Basic information with respect to the project
REPO_NAME = "Chicken-Disease-Classification--Project"
AUTHOR_USER_NAME = "Uday"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "udayr.2012@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)