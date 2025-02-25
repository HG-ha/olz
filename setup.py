import setuptools

from lanzou.api import version

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="olz",
    version=version,
    author="YiMing",
    author_email="1790233968@qq.com",
    description="蓝奏云网盘第三方API，2025年修复版本",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HG-ha/olz",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
