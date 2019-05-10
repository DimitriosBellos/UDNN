import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DimitriosBellos",
    version="0.0.1",
    author="Dimitrios Bellos",
    author_email="Dimitrios.Bellos@nottingham.ac.uk",
    description="UDNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DimitriosBellos/UDNN",
    packages=setuptools.find_packages(),
    install_requires=['numpy','pillow','pytorch','h5py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
    ],
)