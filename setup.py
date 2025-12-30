from typing import List

from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Return a cleaned list of requirements from a requirements.txt file.

    Ignores empty lines, comments, and editable installs like `-e .`.
    """
    requirements: List[str] = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        requirements = [req for req in requirements if req and not req.startswith("#")]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# setup.py file for packaging the project (MachineLearning)
setup(
        name='MachineLearning',
        version='0.0.1',
        author='Manoj',
        author_email='chapalamanojreddy@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements('requirements.txt')
)
