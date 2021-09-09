# carbon-footprint-calculator

[![Carbonfootprint Latest PY Release](https://img.shields.io/badge/carbonfootprint-latest%20release-pink)](https://pypi.org/project/carbonfootprint/)
[![Carbonfootprint Latest Anaconda Release](
https://anaconda.org/altanai/carbonfootprint/badges/version.svg)](https://anaconda.org/altanai/carbonfootprint)


[![Carbonfootprint Status](https://img.shields.io/badge/status-stable-brightgreen)](https://pypi.org/project/carbonfootprint/#history)
[![License](https://img.shields.io/github/license/renewable-energy-experiments/carbon-footprint-calculator)](https://github.com/renewable-energy-experiments/carbon-footprint-calculator/blob/main/LICENSE)
[![Issues](https://img.shields.io/github/issues/renewable-energy-experiments/carbon-footprint-calculator)](https://github.com/renewable-energy-experiments/carbon-footprint-calculator/issues)

[![Twitter](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Frenewable-energy-experiments%2Fcarbon-footprint-calculator
)](https://twitter.com/altanai)
[![Stars](https://img.shields.io/github/stars/renewable-energy-experiments/carbon-footprint-calculator)](https://github.com/renewable-energy-experiments/carbon-footprint-calculator/stargazers)

## Conda distribution

    ~/anaconda3/bin/conda install anaconda-client conda-build
    ~/anaconda3/bin/conda config --set anaconda_upload no
    ~/anaconda3/bin/conda build . --output

    ~/anaconda3/bin/anaconda login
    ~/anaconda3/bin/anaconda upload dist/carbonfootprint-1.1.5.tar.gz
    
## PYppi ditribution 

**1. Generating distribution archives**

First install latest version of PyPA’s build then build . This should generate dist directory:

    python3 -m pip install --upgrade build
    python3 -m build
    
**2. Uploading the distribution archives**

    python3 -m pip install --upgrade twine
    twine check dist/*
    
        Checking dist/carbon_footprint_calculator-1.1.1-py3-none-any.whl: PASSED
        Checking dist/carbon_footprint_calculator-1.1.1.tar.gz: PASSED

Install twine and upload all of the archives under dist to pypi’s test server

    python3 -m twine upload --repository testpypi dist/*
    
or to pyapi
    
    python3 -m twine upload dist/*
    
**3.Installing the package**

From pytest 

    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps carbonfootprint

From pyapi

    pip3 install carbonfootprint

List of classifiers 

- https://pypi.org/classifiers/ 


## Test Enviornment 

Install and Setup Conda 

    export PATH=$PATH:/home/altanai/anaconda3/bin
    
Activate virtual env 

     source energycarbon_env/bin/activate
     
Run unit tests 

    python tests/unittests.py
 
 
## Debugging and Help
 
**Issue1** Adding csv for the datasets 

**solution** refer to https://python-packaging.readthedocs.io/en/latest/non-code-files.html 
Add the following to dynamic setup.py 

    include_package_data=True
    package_data={'': ['dataset/*']},