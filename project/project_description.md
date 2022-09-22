# AIPI 510 Project Requirements
## Introduction
The course project is an opportunity for you to put into practice many of the tools and methods you will learn this semester on a real-world data problem of interest to you.  You will work in an assigned team of to complete a data analysis on a problem of your choice.  The project will require you to apply the skills learned in the course to identify data sources, collect and integrate data, evaluate data quality, analyze and visualize the datasets, conduct pre-processing in preparation for modeling, and build a model to derive a useful insight on your problem.  You will also provide an analysis of the relevant regulatory issues related to use of the datasets proposed and identify potential ethical concerns that may arise by using the data in AI algorithms to solve the problem identified. 

Performance will be evaluated based on:
1)	 Creativity and thoughtfulness in defining the problem, sourcing data, and determining an appropriate analysis to conduct in support of solving the problem
2)  Technical merit in sourcing, manipulating and analyzing data
3)	Your strength of communication of your process and results

As the ability to communicate your process and findings is of critical importance for a data scientist or engineer, the project will culminate in a presentation back to the class on your methodology and results.

## Topics
The topic of your project is up to you.  While you have freedom to choose a topic of interest, note that you cannot focus your project on a topic which you have already worked on for university-related research or another academic project.  A major component of the project is identification and sourcing of relevant data, and if you have already done this as part of another previous effort, it defeats the point of the project. 

Below are a few examples from last year’s class to give you some sense of the range of possible topics:  
•	Identifying the most attractive locations for solar energy installations across the US  
•	Improving rankings for AirBnB properties in New York City  
•	Helping Wake County restaurant inspectors priortize their inspections

Whatever topic you choose, you must frame it as a problem which you are attempting to solve via your project.  

## Process
Your project should follow all of the steps of the CRISP-DM process. 

Additionally, because this is an academic project (rather than an industry one) and we are focused on learning, there are a couple specific requirements / changes: 
- As part of the Business Understanding step, you must research any previous attempts to solve the problem you have selected, and should summarize them briefly in your final presentation.  You should then clearly explain how your solution is different (better!) than the previous solutions you have identified.
- In the Data Understanding step, you must collect and use at least 3 sources of data (meaning that you must use data from at least 3 different organizations or web sources).  
    - Your data sources must include at least two different types of sources.  Types of data sources might include: a web API, web scraping, downloaded csv files, a sensor or wearable, manual collection via survey, etc.  
    - You must use a database to store some (if not all) of your data for the project.  You may choose whether to store raw or processed data (or both) but I would like you to gain practice working with a database.  You may choose what type of database you want to use.  You may use a SQLite database as we do in class, or a NoSQL database, a graph database, etc.
- In the Deployment step, you must build an interface for your project to visually interact in some way with your model and data.  However, you are not required to "deploy" it (as in, make it publicly accessible via the web).  Instead you may demo it for the presentation locally on your laptop if you wish.  If you do not have experience in web development and are not interested in learning for this project, you might consider using [Streamlit](https://streamlit.io), a Python package that allows you to easily create an interactive web app around your project using pure Python.


## Logistics
### Team Responsibilities
You may choose to divide up the project work as you wish.  However, each team member must contribute an equal amount of effort, and all team members must contribute to the programming aspects of the project.

### Software & Infrastructure
Your project must be completed using Python.  You may use any libraries that you choose to assist you.  You may build the project locally on your laptop, or if you need additional storage or processing capability you may (and are encouraged to) complete your project using a cloud setup.  Google Cloud, Microsoft Azure, and Amazon AWS all have special educational accounts available and you are free to choose between these options. You may choose to set up a team GitHub repo to manage collaboration on the project.

### Citing Sources
You may make use of papers, analyses or scripts which you find online.  If you do, you must properly cite each source.  Use of third party materials without citing the source is a violation of the honor code.

## Project Proposal
The project proposal is a written (2 pages maximum) document describing the motivation and plan for your project.  The proposal should include the following: 
- What problem have you selected and why?  
- How is it currently solved / what has been tried before?  
- How are you planning to approach it?  
- How do you plan to measure success in solving it?  What type of metric(s)?
- What data sources do you plan to use (may change later if needed, but need to present an initial plan of what you intend to use)?

In addition to the above, please also include the following sections in your proposal:  
-	Draft plan to complete the remaining steps with simple timeline
-	Responsibilities of each team member

## Final Deliverables

The final deliverables for the project are:
-	A final presentation communicating your project process and results including a brief demo
-	Organized and documented code for your project

### Final presentation
Your final presentation must be in slide format.  You will have a maximum of 10 minutes to present in front of the class.  You may choose whether to have 1 team member narrate or all team members participate. You should include a brief demo of your project as part of the presentation.  Your presentation should include at the end a list of any references cited in the presentation.

Your final presentation should include the following contents:
-	Background/introduction of the problem  
-   Summary of previous attempts to solve the problem and clear explanation of how your solution differs
-	Summary of the highlights from the CRISP-DM process steps you conducted for your topic (e.g. your data sources, describe your data pipeline, your modeling approach)
-	Conclusions / interpretation of the results of your modeling
-	Legal, regulatory and ethical considerations of your data, model and/or  interface
-   Demo of a visual interface for your project

### Project Repo
Code for your project can be either in the form of Jupyter Notebooks or Python scripts.  Your code should be well organized (use OOP, no loose code) and well documented with readme file(s) and code comments.  If we are unable to understand or run your code, points will be deducted.  You should include a main readme file which explains the structure of your code and provides instructions to set up and run it.  If your data is sufficiently small, you can include it in your repo.  If it is too large, you must include links in your repo to access the data (or at least a subsample of it) to be able to run your code.

## Grading
The project proposal is worth 10% of your class grade, and the final submission is worth 25%. The final submission grade is determined as follows (points out of 100):
-	Problem statement and definition of success – 20%
-	Data identification and sourcing - 10%  
-   Data pipeline - 10%
-	Exploratory data analysis – 10%
-	Modeling and conclusions/interpretation - 20%
-	Data privacy and ethical considerations – 5%
-	Project repo organization – 10%
-	Presentation clarity and completeness – 15%

