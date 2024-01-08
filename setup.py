import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TripOpt",
    version="0.2.0",
    author="Yuki1005",
    license='MIT',
    description="You can receive AWS Service Name.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yuki1005/TripOpt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.11",
    install_requires = ["numpy","pandas","folium","openrouteservice","pulp"]
)