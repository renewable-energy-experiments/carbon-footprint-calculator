# Industrial carbon footprint visualizer by fuel mix in the utility 

From pytest 

    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps carbonfootprint

From pyapi

    pip3 install carbonfootprint

or upgrade the already installed 

    python3 -m pip install --upgrade carbonfootprint
    
Ensure pip is installed and updated     
    
    python3 -m pip install --user --upgrade pip
        Requirement already satisfied: pip in /home/altanai/.local/lib/python3.6/site-packages (21.2.4)

    python3 -m pip --version
        pip 21.2.4 from /home/altanai/.local/lib/python3.6/site-packages/pip (python 3.6)


Install Virtualenv

    python3 -m pip install --user virtualenv
    
Creating a virtual environment

    python3 -m venv env
    
Activating a virtual environment    

    source env/bin/activate


Leaving the virtual environment

    deactivate
    
## Installing required modules

     python3 -m  pip install pandas numpy carbonfootprint

**For other missing dependencies**
 
     python3 -m pip install -r requirements.txt   
     python3 -m pip freeze
     
## Industrial use datasets

5-minute interval load data collected and published by EnerNOC, for 100 anonymized commercial customers over a single year (2012) https://open-enernoc-data.s3.amazonaws.com/anon/index.html  which is also referenced by 

US utility database for all of US ( incudes all demand and energy charges and flat rates ) https://openei.org/apps/USURDB/?utilRateFindByZip=98122&sectors%5B%5D=Commercial&sectors%5B%5D=Industrial&service_type=&is_default=&asc=1&search= 