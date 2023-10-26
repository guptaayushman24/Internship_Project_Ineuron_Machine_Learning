from setuptools import setup
from typing import List
setup(
    name='Fraud Detection',
    version='3.1.1',
    author='Ayushman Gupta',
    author_email='guptaayushman24@gmail.com'
)

# Function for running the requirments.txt
def getrequirments(file_path:str)->List[str] :
    requirments=[]
    with open(file_path) as file_obj :
        requirments = file_obj.readlines()
        requirments=[req.replace("\n","")for req in requirments]
    return requirments