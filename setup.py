from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    description_rd = f.read()


setup(
    name="recommendation_system",
    version="0.0.2",
    author="Diogo Leme Jacomini",
    author_email="diogojacomini@outlook.com",
    description="API de Recomendação de Produtos utilizando FastAPI",
    long_description=description_rd,
    long_description_content_type="text/markdown",
    url="https://github.com/diogojacomini/recommendation_system",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "start-api=app.main:app",
        ],
    },
)
