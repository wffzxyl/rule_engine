# coding: utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyrules",
    version="0.0.2",
    author="wffzxyl",
    author_email="wffzxyl@gmail.com",
    description="A simple rules engine",
    keywords = "python rules engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wffzxyl/easyrules",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
		'Topic :: Scientific/Engineering :: Astronomy',
		'Topic :: Scientific/Engineering :: GIS',
		'Topic :: Scientific/Engineering :: Mathematics',
		'Intended Audience :: Science/Research',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
    ],
    python_requires='>=3.7',
    license = "MIT",
)
