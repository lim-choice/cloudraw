from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    description="ncli project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    author="Ryu Jihyeong",
    author_email="jihyeong@didim365.com",
    license="Apache 2.0",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        # 여기에 필요한 패키지 종속성을 추가
    ],
)
