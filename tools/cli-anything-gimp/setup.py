"""Setup configuration for cli-anything-gimp."""

from setuptools import setup, find_namespace_packages

setup(
    name="cli-anything-gimp",
    version="1.0.0",
    description="CLI harness for GIMP - Raster image processing via gimp -i -b (batch mode)",
    long_description=open("README.md").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    author="RelayLaunch (cli-anything contributors)",
    license="MIT",
    python_requires=">=3.10",
    packages=find_namespace_packages(include=["cli_anything.*"]),
    install_requires=[
        "click>=8.0.0",
        "Pillow>=10.0.0",
        "prompt-toolkit>=3.0.0",
    ],
    extras_require={
        "numpy": ["numpy>=1.24.0"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "cli-anything-gimp=cli_anything.gimp.gimp_cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Editors :: Raster-Based",
    ],
)
