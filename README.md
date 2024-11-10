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
7. [Unfixed Bugs](#7-unfixed-bugs)
8. [Deployment](#8-deployment)
9. [Main Data Analysis and Machine Learning Libraries](#9-main-data-analysis-and-machine-learning-libraries)
10. [Credits](#10-credits)

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

#### **Regression Model**

- **Model:** Random Forest Classifier
