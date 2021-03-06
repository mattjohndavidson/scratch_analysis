# Scratch Explorer
[![Build Status](https://travis-ci.com/mattjohndavidson/scratch_analysis.svg?branch=main)](https://travis-ci.com/github/mattjohndavidson/scratch_analysis)
[![Coverage Status](https://coveralls.io/repos/github/mattjohndavidson/scratch_analysis/badge.svg?branch=main)](https://coveralls.io/github/mattjohndavidson/scratch_analysis?branch=main)

## About Scratch
<img src="https://user-images.githubusercontent.com/56270805/102248582-29baa580-3eb6-11eb-8b7f-d34037d3ad51.jpg" width="200" align="right">

Scratch is a block-based visual programming language. 
It was created by the MIT Media Lab to introduce children aged 8-16 to the concepts and logic of coding. 
The Scratch website is located [here](https://scratch.mit.edu).

In 2016, a group of researchers scraped the Scratch project repository and stored the information in a database located in [this github repository](https://github.com/TUDelftScratchLab/ScratchDataset). 
Over 250,000 projects were scraped, resulting in a database of size approximately 3.8 GB.
Additional information about the scraped dataset can be found in this paper [here](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNzUPptD/pdf).     

## About Scratch Explorer
We provide this tool to help interested users explore this large database. 
Using this tool, users are able to search the database of Scratch projects to locate and view existing projects.
They are also able to explore which coding features are important in popular Scratch projects.

### Example Users
1. A middle school CS teacher is looking for examples of Scratch projects that illustrate various programming aspects well to show as an example in class. He doesn’t want to search through individual projects and assess each one to find suitable projects. He would like to use a simple search function to find potential projects.

2. A researcher has found the scraped Scratch project repository and wants to use it to understand what kinds of Scratch projects get the most views, favorites, loves, or remixes. However, the data file is too large to be opened in Excel, and she doesn’t have any experience using other tools like Python to examine the data. She would like to see what features are important in popular Scratch projects.


Our tool allows users to search through the Scratch dataset to locate relevant projects. If the project is still hosted on Scratch, the project is directly displayed and can be viewed within our tool. The source code for the selected project is also linked. 

Our tool also analyzes the dataset to determine the top ten features popular Scratch projects usually contain. The results, along with each feature's importance, are visually displayed.

## Demonstration
A short demonstration of our tool can be viewed [here](https://github.com/mattjohndavidson/scratch_analysis/blob/main/example/demo.mp4).

## Installation and setup
To install and run this explorer:
1. Install `conda` if it is not already installed.
2. Clone the repository using the command `git clone https://github.com/mattjohndavidson/scratch_analysis.git`
3. Create an environment for the app by using: `conda env create -f environment.yml`
4. Run the environment using: `conda activate test_env`
5. Change the working directory using: `cd scratch_explorer`
6. Run the app on your machine by using: `python explore.py`
7. Happy exploring!


## Limitations
There are some limitations to this project:
- Some Scratch projects are no longer available on the website, and our tool will display an empty project if an unavailable project is selected
- The app runs locally on the user's machine and is not hosted by cloud server
- Scratch projects that employ custom, user-created blocks are not included in our tool

## Directory Structure
```
scratch_analysis/  
    |- docs/
        |- component_design.md
        |- functional_design.md
        |- scratch_explorer_final.pdf        
        |- scratch_tech_review.pdf 
        |- software_design.md  
    |- example/  
        |- demo.mp4
    |- scratch_explorer/  
        |- data/  
            |- scratch_data.csv  
            |- scratch_sample.csv   
        |- exports/
            |- diagnostics.sav  
            |- feature_list.sav   
            |- fitted_model.sav   
        |- tests/   
            |- __init__.py   
            |- test_rf_regression.py   
            |- test_save_data.py   
            |- test_search.py   
        |- __init__.py   
        |- explore.py  
        |- model_fit.py  
        |- save_data.py  
        |- search.py  
    |- .coveragerc  
    |- .gitignore  
    |- .travis.yml  
    |- LICENSE  
    |- README.md  
    |- environment.yml
    |- setup.py
```

## Team Members
- Faisal Alsallum
- Jacob Cohen
- Matt Davidson
- Crystal Yu

## Project History
This tool was created for CSE 583, Autumn 2020 at University of Washington.