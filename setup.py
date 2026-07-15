from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "Sarvesh Sapkale"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version = "0.0.1",
    author = "Sarvesh Sapkale",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarveshhh98/End-to-End-book-recommender-system",
    author_email="sapkalesarvesh@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires= ">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)