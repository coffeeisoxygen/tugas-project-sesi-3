from setuptools import find_packages, setup

setup(
    name="tipedata-python",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Ahmad Hasan Maki",
    author_email="your.email@example.com",
    description="Aplikasi pembelajaran tipe data Python",
    python_requires=">=3.6",
)
