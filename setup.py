import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text-summarizer"
AUTHOR_USER_NAME = "shreya-gaikwad-1"
SRC_REPO = "text_summarizer"            #f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}.git"
AUTHOR_EMAIL = "shreyagaikwad6205@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    url="https://github.com/shreya-gaikwad-1/text-summarizer",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    description="Summarizes long texts into shorter versions.",
    long_description=long_description,
    long_description_content = "text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/shreya-gaikwad-1/text-summarizer/issues",
    }
)
