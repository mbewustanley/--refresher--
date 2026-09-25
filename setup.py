from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if '-e .' in requirements:   #remove the '-e .' entry if it exists so as to prevent issues during installation
            requirements.remove('-e .')
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Stanley",
    author_email="mbewustanley@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
# create src folder and create __init__.py file in it

# To install the package, run the following command in your terminal:
# pip install -e .  

# with this command, you are installing the package in "editable" mode, which means that any changes you make to the source code 
# will be reflected immediately without needing to reinstall the package.