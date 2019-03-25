from setuptools import setup

setup(
    name="match",
    version="0.0.1",
    description="Truepic Image Matching Service",
    url="http://truepic.com",
    author="Truepic Inc.",
    author_email="oliver@truepic.com",
    license="Proprietary",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6",
    test_suite="nose.collector",
    install_requires=[
        "numpy==1.16.2",
        "scipy==0.19.0",
        "flask==1.0.2",
        "image-match==1.1.2",
        "python-dotenv==0.10.1",
        "certifi==2019.3.9",
        "elasticsearch==6.3.1",
    ],
    extras_require={
        "dev": [
            "matplotlib==3.0.2",
            "black==18.9b0",
            "isort==4.3.4",
            "pylint==2.2.2",
            "pytest==4.0.1",
            "nose==1.3.7",
            "mypy==0.650",
        ],
        "prod": ["gunicorn==19.9.0"],
    },
)

def run(self):
    __builtins__.__NUMPY_SETUP__ = False
    import numpy
