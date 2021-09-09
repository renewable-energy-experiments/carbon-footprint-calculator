# carbon-footprint-calculator


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
    
    twine upload dist/*
    
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
    