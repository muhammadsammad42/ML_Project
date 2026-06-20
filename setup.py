from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list:
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="ML_Project",
    version="0.0.1",
    author="Sammad",
    author_email="muhammadsammad30465@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)