import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='flagser',
    version='2.3',
    author="Alfred Roos",
    author_email="alfred@stensatter.se",
    description="Flag manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spynetS/flagser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
