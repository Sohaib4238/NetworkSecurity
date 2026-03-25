from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            #read lines from the file 
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                ## igonre empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.1',
    author='Sohaib',
    author_email='sohaib4238@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)