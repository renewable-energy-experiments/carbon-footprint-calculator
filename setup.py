import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="carbonfootprint",
    version="1.1.2",
    author="Altanai",
    author_email="tara181989@gmail.com",
    description="A small example package",
    long_description="Calculates carbon footprint based on fuel mix and discharge profile at the utility selected. Can create graphs and tabular output for fuel mix based on input file of series of power drawn over a period of time.",
    long_description_content_type="text/markdown",
    url="https://github.com/renewable-energy-experiments/carbon-footprint-calculator",
    project_urls={
        "Bug Tracker": "https://github.com/renewable-energy-experiments/carbon-footprint-calculator/issues",
    },
    keywords=[
        'carbon-emission', 'energy-efficiency', 'utility-fuel-mix',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
