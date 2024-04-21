import setuptools
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requirements.

    '''
    requirements = []
    with open(file_path) as f_obj:
        requirements=f_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



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
    packeges=setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
)
