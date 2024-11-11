## DestinationDNA - Predicting Vacation Destination Preferences

<div align="center">
	<img src="docs/images/mountainsVSbeaches.webp">
</div>
Images made with [Midjourney](https://www.midjourney.com/)

## Table of Contents

1. [Dataset Content](#1-dataset-content)
2. [Business Requirements](#2-business-requirements)
   - [Epics](#epics)
   - [User Stories](#user-stories)
3. [Hypotheses and validation](#3-hypotheses-and-validation)
4. [Map the business requirements | Data Visualizations | ML tasks](#4-map-the-business-requirements--data-visualizations--ml-tasks)
5. [ML Business Case](#5-ml-business-case)
6. [Dashboard Design](#6-dashboard-design)
7. [Deployment](#7-deployment)
8. [Main Data Analysis and Machine Learning Libraries](#8-main-data-analysis-and-machine-learning-libraries)
9. [Credits](#9-credits)

## **1. Dataset Content**

- The dataset for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/jahnavipaliwal/mountains-vs-beaches-preference).

- The dataset has about 52.000 thousand rows and represents the vacation preferences of customers based on their persona. The table below indicates the variables, their description and units of measurement. We note that some Features are numerical while others are categorical.

| Age | Gender     | Income | Education Level | Travel Frequency | Preferred Activities | Vacation Budget | Location | Proximity to Mountains | Proximity to Beaches | Favorite Season | Pets | Environmental Concerns | Preference |
| --- | ---------- | ------ | --------------- | ---------------- | -------------------- | --------------- | -------- | ---------------------- | -------------------- | --------------- | ---- | ---------------------- | ---------- |
| 56  | male       | 71477  | bachelor        | 9                | skiing               | 2477            | urban    | 175                    | 267                  | summer          | 0    | 1                      | 1          |
| 69  | male       | 88740  | master          | 1                | swimming             | 4777            | suburban | 228                    | 190                  | fall            | 0    | 1                      | 0          |
| 46  | female     | 46562  | master          | 0                | skiing               | 1469            | urban    | 71                     | 280                  | winter          | 0    | 0                      | 1          |
| 32  | non-binary | 99044  | high school     | 6                | hiking               | 1482            | rural    | 31                     | 255                  | summer          | 1    | 0                      | 1          |
| 60  | female     | 106583 | high school     | 5                | sunbathing           | 516             | suburban | 23                     | 151                  | winter          | 1    | 1                      | 0          |

## **2. Business Requirements**

- The customer is interested in understanding the relationship between their destination and the guest/customer persona. So they can target the right customer with the right marketing.

* Business Requirement 1: The customer wants to understand the relationship between the destination and the customer persona.
* Business Requirement 2: The customer wants to predict the probability of a customer booking a destination based on their persona.

### User Stories

- **US1:** As a client(marketing oriented), I want to see insights into preferred destinations based on user demographics, so I can tailor our advertising efforts to target the right audience. (_Business Requirement Covered: BR2_)

- **US2:** As a user, I want to receive a vacation destination recommendation (mountain or beach) based on my personal preferences, so that I can choose the destination that best suits my interests. (_Business Requirement Covered: BR2_)

- **US3:** As a user, I want to know the most important features that determine my vacation destination preference, so that I can understand the factors that influence my decision. (_Business Requirement Covered: BR1_)

- **US4:** As a user, I want to know the distribution of vacation preferences across different demographic groups, so that I can compare my preferences with those of others. (_Business Requirement Covered: BR1_)

- **US5:** As a client, I want to get a machine learning model that can predict the probability of a customer booking a destination based on their persona. (_Business Requirement Covered: BR2_)

## **3. Hypothesis and how to validate?**

Hypotheses:

    Hypothesis 1:

    Demographic characteristics (age, income, education) significantly influence vacation destination preferences.
    Validation: Perform feature importance analysis using a machine learning classification model (e.g., Random Forest or Logistic Regression) to determine which demographic features most strongly predict destination preference.

    Hypothesis 2:

    There are distinct customer personas that can be clustered based on their vacation preferences and demographic characteristics.
    Validation: Apply unsupervised learning techniques like K-means clustering to group customers, then analyze the cluster characteristics using descriptive statistics and visualization to identify unique customer segments.

    Hypothesis 3:

    Geographic or regional factors play a crucial role in destination preferences beyond individual demographic characteristics.
    Validation: Create interaction features that combine demographic data with geographic information, then compare model performance with and without these interaction features to assess their predictive power.

## **4. Map the business requirements | Data Visualizations | ML tasks**

- **Business Requirement 1 (BR1):** Data Visualization and Correlation study

  - We will use data visualization techniques to understand the relationship between the destination and the customer persona. We will use correlation analysis to identify the most important features that determine vacation destination preferences.

    - The [Data Analytics notebook](https://github.com/paulunder/DestinationDNA/blob/main/jupyter_notebooks/03_Data_Analytics.ipynb) handles this business requirement.

- **Business Requirement 2 (BR2):** Regression Analysis

  - We will use machine learning models to predict the probability of a customer booking a destination based on their persona. We will use classification models like Random Forest, Logistic Regression, and Gradient Boosting to predict destination preferences.

    - The [Feature Engineering notebook](https://github.com/paulunder/DestinationDNA/blob/main/jupyter_notebooks/04_Feature_Engineering.ipynb) + the [Model Evaluation notebook](https://github.com/paulunder/DestinationDNA/blob/main/jupyter_notebooks/05_Model_Evaluation.ipynb) handles this business requirement.

## **5. ML Business Case**
### **Predict Preference**
We want to predict the preference of a customer based on their persona. The target variable is `Preference` which is binary. We will use the following features to predict the target variable:
- Age
- Gender
- Income
- Education Level
- Travel Frequency
- Preferred Activities
- Vacation Budget
- Location
- Proximity to Mountains
- Proximity to Beaches
- Favorite Season
- Pets
- Environmental Concerns

With this information, we can predict the probability of a customer booking a destination based on their persona.
According to that as stated in the [Feature Engineering notebook](https://github.com/paulunder/DestinationDNA/blob/main/jupyter_notebooks/04_Feature_Engineering.ipynb) we added the feature "AgeGroup" to keep it simple and to avoid overfitting.

#### **Regression Model**

- **Model:** Logistic Regression Model - Accuracy: 0.8983

- **Model:** Decision Tree Model Accuracy: 0.9960

- **Model:** Gradient Boosting Model Accuracy: 0.9960

- **Model:** Random Forest Model Accuracy: 0.9953

- **Model:** Naive Bayes Model Accuracy: 0.9250

I have chosen the Decision Tree Model - after some tuning I got an accuracy of 0.9962.

## Dashboard Design

### Page 1: Project Summary

- Introduction the project and motivation
- Project dataset description
- Display the first five rows of the data
- State business requirements

### Page 2: Exploratory Data Analysis

- Display the distribution of the target variable
- Display the distribution of the features
- Display the correlation matrix
- Display the distribution of the target variable by demographic features

### Page 3: Project Hypotheses

- State business requirement 1
- State business requirement 2

### Page 4: Preference Predictor

- Display the prediction form
- Display the prediction result

### Page 5: Decision Tree Model

- Display the decision tree model

### Page 6: Project Conclusions

- Summarize the project findings
- State the main insights


## Technologies Used
The technologies used throughout the development are listed below:

### Languages

* [Python](https://www.python.org/)

### Python Packages

* [Pandas](https://pandas.pydata.org/docs/index.html) - Data analysis and manipulation tool
* [Numpy](https://numpy.org/doc/stable/index.html) - The fundamental package for scientific computing with Python
* [YData Profiling](https://docs.profiling.ydata.ai/latest/) - For data profiling and exploratory data analysis
* [Matplotlib](https://matplotlib.org/) - Comprehensive library for creating static, animated and interactive visualisations
* [Seaborn](https://seaborn.pydata.org/) - Data visualisation library for drawing attractive and informative statistical graphics
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Transformers to engineer and select features for machine learning models
* [ppscore](https://pypi.org/project/ppscore/) - Data-type-agnostic score that can detect linear or non-linear relationships between two columns
* [scikit-learn](https://scikit-learn.org/stable/) - Machine learning library for training the ML model
* [XGBoost](https://xgboost.readthedocs.io/en/stable/) - Optimised distributed gradient boosting library
* [Imbalanced-learn](https://imbalanced-learn.org/stable/) - Tool for dealing with classification problems with imbalanced target
* [Joblib](https://joblib.readthedocs.io/en/stable/) - Tool for dumping pipeline to pickle files
* [Kaggle](https://pypi.org/project/kaggle/) - Kaggle API functionalit
* [Streamlit](https://streamlit.io/) - Build the web app.

### Other Technologies

* [Git](https://git-scm.com/) - For version control
* [GitHub](https://github.com/) - Code repository
* [Heroku](https://heroku.com) - For application deployment
* [Gitpod](https://www.gitpod.io/) - Cloud IDE used for development
* [Jupyter Notebook](https://jupyter.org/) - Interactive Python
* [CI Python Linter](https://pep8ci.herokuapp.com/) - Style guide for python


## Unfixed Bugs
* There are no unfixed bugs except for Jupyter notebook sometimes not plotting when the `Run All` button is pressed.
* Sometimes I get `StreamlitAPIException: set_page_config() can only be called once per app page`, with a refresh of the webpage the streamlit app works fine again. The source of the issue is unknown.


## Deployment

### Set Heroku stack

To log into the Heroku toolbelt CLI:

0. Install the client in the terminal `curl https://cli-assets.heroku.com/install-ubuntu.sh | sh`
1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_login -i`
5. Enter your email and paste in your API key when asked
6. Set the stack to heroku-24 `heroku stack:set heroku-20 --app destinationDNA`
7. In this repo, set the `runtime.txt` Python version to `python-3.10.12` 


The App live link is: [DestinationDNA](https://destination-dna-fea40f3ec5fa.herokuapp.com)

### Deployment steps

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### Important configuration files

* `setup.sh` should contain the following
```
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

* `Procfile` should contain
```
web: sh setup.sh && streamlit run app.py
```

## Credits 

* The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/jahnavipaliwal/mountains-vs-beaches-preference).
* ML operations are inspired by Orhan Serçe - under this link: https://www.kaggle.com/code/orhansere/mountains-vs-beaches-smote-classification


## Acknowledgements (optional)
* Thanks to my mentor - Mo Shami for guidance. Thanks to my family for their support. 