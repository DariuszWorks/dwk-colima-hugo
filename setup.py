import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dwk-colima-hugo",
    version="0.1.1",
    author="Dariusz",
    author_email="info@dariuszworks.co.uk",
    description="Colima Framework Hugo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DariuszWorks/dwk-colima-hugo",
    project_urls={},
    license="MIT",
    packages=["dwk-colima-hugo"],
    install_requires=["boto3", "python-dotenv", "pyaml"],
)
