# IBM Data Science Professional Certificate- Coursera

## This repository contains a comprehensive curriculum for mastering data science, including essential modules that cover foundational concepts, practical tools, methodologies, and advanced techniques. This repository encompasses all the data science labs, and projects completed throughout the course.
I have provided a brief overview of all the modules – this repo only contains the Jupyter Notebook files 


### Course Modules
- [What is Data Science?](#what-is-data-science?)
- [Tools for Data Science](#tools-for-data-science)
- [Data Science Methodology](#data-science-methodology)
- [Python for Data Science, AI & Development)](#python-for-ai-&-developemt)
- [Data Visualization and Mapping](#data-visualization-and-mapping)
- [Feature Engineering](#feature-engineering)
- [Machine Learning Model Development](#machine-learning-model-development)
- [Model Evaluation](#model-evaluation)
- [Conclusion and Findings](#conclusion-and-findings)

## What is Data Science?
An introduction to the field of data science, its significance, and its impact on various industries. Explore the core concepts and the role of data scientists in today’s data-driven world.
- Data Science,	Big Data,	Machine Learning,	Deep Learning,	Data Mining

## Tools for Data Science
A survey of essential tools and technologies used in data science, including programming languages, data manipulation libraries, and development environments
- Data Science,	Python Programming,	Github,	Rstudio, Jupyter notebooks

## Data Science Methodology
An overview of the structured approach to data science projects, covering the steps from problem definition to data collection, analysis, and deployment.
- Data Science,	Data Analysis	CRISP-DM,	Methodology, Data Mining 

## Python for Data Science, AI & Development
A deep dive into Python programming, emphasizing its applications in data science, artificial intelligence, and software development
- Learn Python - the most popular programming language and for Data Science and Software Development
-	Apply Python programming logic Variables, Data Structures, Branching, Loops, Functions, Objects & Classes.
-	Demonstrate proficiency in using Python libraries such as Pandas & Numpy, and developing code using Jupyter Notebooks.
-	Access and web scrape data using APIs and Python libraries like Beautiful Soup


## Data Visualization and Mapping
A Folium map was created to visualize the geographical distribution of launch sites and their outcomes. The map includes:
- Markers: Indicating launch sites with color-coded markers for successful (green) and unsuccessful (red) launches.
- Circles: Displaying the proximity of launch sites to nearby key locations, such as coastlines and highways.
- Zoomed Views: Focused views on individual launch sites like Kennedy Space Center to highlight detailed launch histories.
  <hr>
-	Data Science,	Data Analysis, Python Programming, Numpy,	Pandas


## Feature Engineering
New features were engineered to enhance the predictive power of the machine learning model:
- Derived Features: Created features such as "Distance to Coast" and "Payload-to-Orbit Ratio."
- Categorical Encoding: Encoded categorical variables like "Orbit Type" and "Booster Version" into numerical formats.
- Scaling and Normalization: Applied scaling techniques to normalize numerical features.

## Machine Learning Model Development
The predictive modeling process involved the following steps:
1. Model Selection: Various models such as Logistic Regression, Decision Trees, Random Forests, and Support Vector Machines (SVM) were tested.
2. Hyperparameter Tuning: Optimized model parameters using techniques like Grid Search and Random Search.
3. Training and Validation: Split the dataset into training and test sets for model training and evaluation.

## Model Evaluation
The model performance was evaluated using metrics like:
- Accuracy: The percentage of correctly predicted outcomes.
- Precision and Recall: To assess the model's ability to correctly identify successful launches.
- Confusion Matrix: Provided a detailed breakdown of true positives, true negatives, false positives, and false negatives.
- ROC Curve and AUC: Measured the model's ability to distinguish between successful and failed launches.

## Conclusion and Findings
The analysis revealed several key insights:
- Geographical Distribution: Launch sites on the East Coast tend to cater to geostationary missions, while West Coast sites focus on polar orbits.
- Significant Factors: Variables such as payload mass, weather conditions, and orbit type have a considerable impact on launch success.
- Model Accuracy: The best-performing model achieved an accuracy of over 85% in predicting launch outcomes.
