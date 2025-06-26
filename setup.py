from setuptools import setup, find_packages

setup(
    name="flask-devops-pipeline",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.3.3",
        "gunicorn>=21.2.0",
        "prometheus-client>=0.17.1",
    ],
    author="Arjun Bector",
    author_email="arjunbector@gmai.com",
    description="A Flask application with DevOps CI/CD pipeline",
    python_requires=">=3.8",
)