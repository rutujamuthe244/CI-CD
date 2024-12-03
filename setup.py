from setuptools import setup, find_packages

setup(
    name='my_package',  # Replace with your package name
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # List of dependencies, e.g., ['requests']
    include_package_data=True,  # Include other files like config files
    description='A description of your package',
    url='https://github.com/rutujamuthe244/CI-CD',
    author='Rutuja',
    author_email='rutujamuthe24@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
