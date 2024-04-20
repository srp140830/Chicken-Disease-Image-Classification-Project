import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "Chicken-Disease-Image-Classification-Project"
AUTHOR_USER_NAME = "srp140830"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "panaskar.sanket@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for Chicken disease classifier",
    package_dir={"": "src"},
    packeges=setuptools.find_packages(where="src")
)
