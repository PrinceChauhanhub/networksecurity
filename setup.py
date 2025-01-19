'''
It is the essential part of packing and distributing python projects. It is used by setuptools( or distutils in older Python versions) to define the configuration of your project, such as its metadata, dependencied and more
'''

from setuptools import find_packages, setup

from typing import List

def get_requirements()->List[str]:
    # Function will return list of requirements
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_list

setup(
    name = "NetworkSecurity",
    vesion = "0.0.1",
    author = "Prince Chauhan",
    author_email= "princechauhan220103@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)