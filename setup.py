# For info on how to write a setup.py file, check out the link below 
# or ask a friendly neighborhood python programmer! 
# https://docs.python.org/3.7/distutils/setupscript.html

# You can also alternatively use a requirements.txt file which contains ALL 
# packages needed for your package. Ask someone about this before doing it!

from setuptools import setup, find_packages

setup(
    name = "mypackagename",
    version = "0.0.1",
    description = "My package does this really cool thing",
    author = "Jo Taylor",
    author_email = "jotaylor@stsci.edu",
    keywords = ["astronomy", "jwst", "simulations", "etc"],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Development Status :: 1 - Planning',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering :: Astronomy',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
	packages = find_packages(),
    # Specify necessary, but minimal, requirements needed to run. 
    # Only specify version numbers if you know some versions will break your code.
    # An example of how to make another git repo a dependency of your package:
    install_requires = ["setuptools",
                        "numpy",
                        "astropy"],
#   This is just to show you how to specify version numbers
#                        "matplotlib>=3.0.0,<3.1.0",
#                        "beautifulsoup4>=1.0",
    # Maybe you need access to a script in another repo for your package. Here's how you do that:
#                        "package2"],
#    dependency_links = ["git+ssh://git@grit.stsci.edu/NIRISS/package2.git#egg=package2-0.0.1"],
    # If you need something from github, any of the below formats work:
#    dependency_links = ["git+ssh://git@github.com/npirzkal/GRISMCONF.git#egg=GRISMCONF-0.1"],
#    dependency_links = ["git+git@github.com:npirzkal/NIRCAM_Gsim@master#egg=NIRCAM_Gsim-0.1"],
#    dependency_links = ["git+https://github.com/npirzkal/NIRCAM_Gsim@master#egg=NIRCAM_Gsim-0.1"],
    
#   Can also include entry_points, but you likely won't need to do this.
#   entry_points = {"console_scripts": [
#                       "dothething = mypackagename.package:module"],
#                    },                       
    )

