from setuptools import setup, find_packages

setup(
    name="moderation-service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[

    ],
    python_requires=">=3.12",
    author="Dmitry Ilyenko",
    author_email="ilyenkod@yandex.ru",
    description="Content moderation service for Neural News Platform",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
