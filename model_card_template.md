# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model uses a Random Forest Classifier, trained on publicly available U.S. Census data. It predicts whether an individual’s income exceeds $50,000 based on demographic and economic features.

## Intended Use
This model handles datasets with mixed data types well, including those with missing values. However, it is unsuitable for real-time predictions on extremely large datasets due to speed and cost concerns. Created for a class project, it is intended for general use, not decision-making.

## Training Data
80% of the data is used to train this model.

## Evaluation Data
The model was evaluated on a test set comprised of 20% of publicly available U.S. Census dataset. It underwent the same preprocessing as the training data, ensuring consistency in feature transformation and an unbiased performance assessment.

## Metrics
The model’s performance was evaluated using these three key metrics:

Precision: 0.7962 | Recall: 0.5372 | F1: 0.6416

This model had the following parameters:
    n_estimators = 100,
    max_depth = 10,
    random_state = 42

## Ethical Considerations
The model utilizes demographic features like race, sex, and native country, which may introduce bias. Efforts were made to evaluate performance across these features, but users should ensure ethical application to prevent reinforcing societal inequalities. Transparency and bias monitoring are essential.

## Caveats and Recommendations
The model has limitations, including potential biases in the training data, the use of default hyperparameters, and assumptions about stable feature-target relationships over time. To improve performance, periodic retraining, fairness analyses, and hyperparameter tuning are recommended. This model is best suited for educational or exploratory analysis.