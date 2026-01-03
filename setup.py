from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="grok-webapi",
    version="0.1.0",
    author="Grok-Web-API Contributors",
    description="Reverse-engineered asynchronous Python wrapper for Grok web app image generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlqattanDev/Grok-Web-API",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "aiohttp>=3.9.0",
        "playwright>=1.40.0",
        "loguru>=0.7.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "cookies": ["browser-cookie3>=0.2.0"],
        "dev": [
            "pytest>=7.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "ruff>=0.1.0",
            "mypy>=1.0",
        ],
    },
)
