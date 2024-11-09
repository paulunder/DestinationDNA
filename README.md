## DestinationDNA - Predicting Vacation Destination Preferences

<div align="center">
	<img src="docs/images/mountainsVSbeaches.webp">
</div>

## Business Requirements

- The customer is interested in understanding the relationship between their destination and the guest/customer persona. So they can target the right customer with the right marketing.

* Business Requirement 1: The customer wants to understand the relationship between the destination and the customer persona.
* Business Requirement 2: The customer wants to predict the probability of a customer booking a destination based on their persona.

## Hypothesis and how to validate?

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
