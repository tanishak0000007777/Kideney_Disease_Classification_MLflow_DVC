import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME="Kideney_Disease_Classification_MLflow_DVC"
AUTHOR_USER_NAME="tanishak0000007777"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="tanishakbansal07@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package from CNN app.",
    LongDescription=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)