## Component design

This section describes the components required for the use cases in the functional design.

### Component 1: Project search function
- Get user choice of search criteria
    - total blocks, total remixes, total views, total favorites, total loves, block types [allow user to choose from list of top block types], abstraction, parallelism, logic, synchronization, flow control, user interactivity, data representation, mastery
    - The metrics are described in more detail [here](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNzUPptD/pdf) 
- Search through database to find projects containing search criteria
- Display project in page, and allow user to view the project without needing to use a separate browser
- Display URL for project's source code
- On user click, load the next Scratch project 

### Component 2: random forest regression
- Pull all Scratch features into a pandas array
- Run random forest regression model with all popularity metrics
- Write feature importances for all features for each popularity metric

### Component 3: dashboard `(dash)`
- Combines results from search function and random forest regression in one location
- Each component is on a separate page
- One page allows user to search through the database for sample projects
- Second page allows user to see which features are important in popular projects
