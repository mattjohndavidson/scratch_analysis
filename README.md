# Scratch Explorer
[![Build Status](https://travis-ci.com/mattjohndavidson/scratch_analysis.svg?branch=main)](https://travis-ci.com/github/mattjohndavidson/scratch_analysis)
[![Coverage Status](https://coveralls.io/repos/github/mattjohndavidson/scratch_analysis/badge.svg?branch=main)](https://coveralls.io/github/mattjohndavidson/scratch_analysis?branch=main)
![videogames_48_37](https://user-images.githubusercontent.com/56270805/102248582-29baa580-3eb6-11eb-8b7f-d34037d3ad51.jpg)

## About Scratch
Scratch is a block-based visual programming language. 
It was created by the MIT Media Lab to introduce children aged 8-16 to the concepts and logic of coding. 
The Scratch website is located [here](https://scratch.mit.edu).

In 2016, a group of researchers scraped the Scratch project repository and stored the information in a database located in [this github repository](https://github.com/TUDelftScratchLab/ScratchDataset). 
Over 250,000 projects were scraped, resulting in a database of size approximately 3.8 GB.
Additional information about the scraped dataset can be found in this paper [here](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNzUPptD/pdf).     

## About Scratch Explorer
We provide this tool to help interested users explore this large database. 
Using this tool, users are able to search the database of Scratch projects to locate and view existing projects.
They are also able to explore which coding features are important in popular projects.

### Example Users
1. A middle school CS teacher is looking for examples of Scratch projects that illustrate various programming aspects well to show as an example in class. She doesn’t want to search through individual projects and assess each one to find suitable projects. She would like to use a simple search function to find potential projects.

2. A researcher has found the scraped Scratch project repository and wants to use it to understand what kinds of Scratch projects get the most views, favorites, loves, or remixes. However, the data file is too large to be opened in Excel, and he doesn’t have any experience using other tools like Python to examine the data. He would like to see what features are important in popular Scratch projects.


Our tool allows users to search through the Scratch dataset to locate relevant projects. If the project is still hosted on Scratch, the project is directly displayed and can be viewed within our tool. The source code for the project is also linked. 

Our tool also analyzes the dataset to determine the top ten features popular projects usually contain. The results, along with each feature's importance, are visually displayed.

## Demonstration
Add video here

## Installation
To install and run this explorer :
\begin{enumerate}
  \item Install conda.
  \item Clone the repository using: git clone https://github.com/mattjohndavidson/scratch_analysis.git
  \item Create an environment for the app by using: conda env create -f environment.yml
  \item Run the environment using: source activate test_env
  \item ...
  \item Run the website on your local machine by using: python app.py
  \item ...
\end{enumerate}

## Limitations
There are several limitiation to this project:
\begin{itemize}
  \item The size of the data set is very large (3.8GB) and cannot be hosted in this Github repository.
  \item Some Scratch projects are no longer available on the website.
  \item The app runs locally at the user's machine and is not hosted by cloud server
\end{itemize}


## Notes
To be updated

## Directory Structure
To be updated

## Team Members
1. Faisal Alsallum
2. Jacob Cohen
3. Matt Davidson
4. Crystal Yu

## Project History
This tool was created for CSE 583, Autumn 2020 at University of Washington.
