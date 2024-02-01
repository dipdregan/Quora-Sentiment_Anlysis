import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0" 

REPO_NAME = "Quora-Sentiment_Analysis"
AUTHOR_NAME = "YourName"
PACKAGE_NAME = "quora_sentiment_analysis" 
AUTHOR_EMAIL = "your.email@example.com"

setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Quora Sentiment Analysis Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "senti_ays"},
    packages=setuptools.find_packages(where="senti_ays"),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
