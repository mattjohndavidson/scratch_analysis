## Functional design

This section will describe the use cases that motivate the design of this tool. 

### Use case 1: Search Scratch project database to locate sample projects
The user may be a Scratch user or a CS teacher looking for examples of specific kinds of Scratch projects, for personal or classroom use. However, it is time consuming to search through the database for individual projects and assess each one to find projects suitable for their needs. The user has some basic programming knowledge but would prefer to search through the database using a more intuitive, user-friendly interface. 

Our goal is to provide a simple search function to locate potential projects that fits the user's needs.
- User input: search metric (e.g. total blocks, block types)
- Outputs: project that includes the search criteria (embedded in page), project source code (url that the user can click on)
- User is able to click on a URL to see the project source code
- User is able to view the next best project by clicking a button

### Use case 2: Model relationships between computational features and social metrics
The user may be a researcher who is trying to understand the kind of computational thinking generated by popular Scratch projects. However, the database is too large to be opened in Excel, and the user has little to no experience using tools like Python to examine the data. The user is interested in seeing which features are important in popular Scratch projects. 

Our goal is to analyze the data and return the results to the user in an interactive, easy to understand format.
- Inputs: user choice of of popularity social metrics (total remixes, total views, total favorites, total loves)
- Output: plot of top features in popular projects, with feature importance displayed in plot 
- When user hovers over plot, more information about the model results is displayed