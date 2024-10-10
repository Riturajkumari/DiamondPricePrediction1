from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements from the given file."""
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines from the file
        requirements = [req.strip() for req in requirements]  # Remove newlines and strip spaces

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='DiamondPricePrediction',  # Corrected spelling here
    version='0.0.1',
    author='Ritu',
    author_email='rituraj1396@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),  # Added a comma here
)
