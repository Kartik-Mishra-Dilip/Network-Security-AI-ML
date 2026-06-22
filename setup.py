from setuptools import find_packages,setup
from typing import List


def get_requirements()->list[str]:
    """
    this function will return list of requirements
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()

            for line in lines:
                requirement=line.strip()
                #ignore empty line and -e .
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirement,txt not found") 

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="kartik mishra",
    author_email="kartk.mishra8155@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)