# Software Design

This document describes the functional and component design for this project. Our objective is to create a web-based tool that will allow users to fit regression models and search a database of Scratch programs, described [here](https://github.com/TUDelftScratchLab/ScratchDataset).

## Functional design

This section will describe the use cases that are designing this tool for. 

### Use case 1: Model relationships between computational thinking scores and social metrics
The user may be a researcher who is trying to understand the kind of computational thinking generated by popular or unpopular Scratch projects. 
- Inputs: user choice of computational thinking scores; user choice of social metrics
- Output: table of regression coefficients; plots of model predicted values; plots of residuals


### Use case 2: Predict computational thinking score based on how the project was written
The user may be a researcher who is interested in how the code-in-progress is related to outcome measures.
- Inputs: user choice of number of blocks to include (e.g. only the first 5 blocks, all possible blocks); user choice of computational thinking score(s)
- Outputs: accuracy of predicted score; plot of prediction accuracy over interval [0:user_chosen_number of blocks]

### Use case 3: Search Scratch project database
The user may be a Scratch user or a CS teacher who is looking for examples of specific kinds of Scratch projects, for personal or classroom use.
- Inputs: search criteria (e.g. keyword, block types, filter by popularity or computational thinking scores)
- Outputs: table with results from search, including the project description, length of code, url

### Use case 4: Search project DB by model output
The user may be a researcher who, after seeing model output, wants to get some examples of specific projects to help in writing up the results.
- Inputs: model output from either use case 1 or use case 2; user choice of most or least accurately predicted projects; user choice of number of projects
- Outputs: table of results, including project description, length of code, url

## Component design

This section describes the components required for the above use cases.

### Component 1: regression
`regression`
- Get user choice of predictor and outcome variables
- Pull those choices into a pandas array
- Run regression model, specified according to user choices of variables
- Display clean, readable table of results
- Display plot(s) of model-predicted values
- 3 cases: for each predictor, z-score of -1, 0, or 1
- Display plot(s) of residuals

### Component 2: score prediction
`predict_score`
- Get user choice of number of blocks to include and computational thinking score(s) to predict
- Create pandas db of all projects, using first to the Nth block (or fewer, if total number of blocks is lower)
- Run prediction model with blocks as input and computational thinking scores as predicted values
- Display table of prediction accuracy
- Display plot of how prediction accuracy would change with greater or fewer blocks

### Component 3: Project search
`search`
- Get user choice of search criteria
- Keywords, block types, project length, social metrics, computational thinking scores
- Display table of results
- Project description, project length, social metrics, computational thinking scores, url
- Display project in page
- On user click, load the scratch project in an inset window

### Component 4: Link between modeling results and search feature
`search_from_model`
- Get model specification, residuals, number of projects desired, and user choice of best or worst predicted
- Display table of results
- Same as in search component, but including the value of the residual