from setuptools import find_packages, setup
from typing import List

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


setup(
    name="mlproject",
    version="0.0.1",
    package_dir={"": "MachineLearning"},
    packages=find_packages(where="MachineLearning"),
    install_requires=get_requirements("requirements.txt"),
)

