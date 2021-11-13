from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Matplotlib wrapper'
LONG_DESCRIPTION = 'Simple wrapper for the matplotlib templates I frequently use.'

# Setting up
setup(
        name="stuart_plot", 
        version=VERSION,
        author="Stuart Watt",
        url="https://github.com/stuart-watt/stuart_plot",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        packages=setuptools.find_packages(),
        python_requires=">=3.6",
        install_requires=[
            "matplotlib",
        ],
)