# Software Design

This document describes the functional and component design for this project. Our objective is to create a web-based tool that will allow users to search a large (~3.8 GB) database of Scratch programs and to learn more about computational features found in popular Scratch programs. The full Scratch database is located [here](https://github.com/TUDelftScratchLab/ScratchDataset).

## About Scratch and our data source
Scratch is a block-based visual programming language. It was created by the MIT Media Lab to introduce children aged 8-16 to the concepts and logic of coding. The Scratch website is located [here](https://scratch.mit.edu).

In 2016, a group of researchers scraped the Scratch project repository and stored the information in a database located in [this github repository](https://github.com/TUDelftScratchLab/ScratchDataset). 
Over 250,000 projects were scraped, resulting in a database of size approximately 3.8 GB.
Additional information about the scraped dataset can be found in this paper [here](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNzUPptD/pdf).

In this analysis, we filter the full database to keep only projects with standard blocks, leaving over 233,000 projects for use. 
