from setuptools import setup

with open("REDAME.md",'r',encoding="utf-8") as f:
    long_description=f.read()

REPO_NAME= "project-template"
AUTHOR_USER_NAME="SiddharthTyagi119"
SRC_REPO="src"
LIST_OF_REQUIREMENTS=[]

setup(name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    descryption="This is first release"
    long_description=long_description,
    url=f"https//github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="sidtyagi05@gmail.com"
    packages=[SRC_REPO],
    python_requires= ">=3.6",
    install_requires=LIST_OF_REQUIREMENTS)