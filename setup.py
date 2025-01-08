from setuptools import setup, find_packages


setup(
    name="code_testing_agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
    ],
    author="Ankush Gupta",
    author_email="gptankush9@gmail.com",
    description="AI-powered code testing framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/code_testing_agent",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)