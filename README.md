Churn Analysis - Exploratory Data Analysis (EDA)
Introduction
This project involves performing Exploratory Data Analysis (EDA) on a customer churn dataset. The goal is to uncover trends, patterns, and insights related to customer churn to help identify factors contributing to churn and provide actionable insights. This README details the process, methodology, and key steps involved in this EDA process.

Steps in EDA
1. Data Loading and Exploration
The dataset is first loaded and basic inspection is performed to understand its structure:
telco_data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
Key information like data types, null values, and summary statistics are observed using functions like .info(), .describe(), and .head().

2. Data Cleaning
Handle missing values:
TotalCharges column had missing or incorrect values, which were treated by removing rows with null values or transforming them.
Rows where TotalCharges are null are likely due to new customers without sufficient history for calculation.
Conversion to numerical types when necessary:

telco_data['TotalCharges'] = pd.to_numeric(telco_data['TotalCharges'], errors='coerce')

3. Feature Engineering
Categorical Variables: Convert categorical variables like gender, Partner, Dependents into numerical forms using dummy encoding.
telco_data_dummies = pd.get_dummies(telco_data)

Target Variable: The target variable Churn is transformed into binary format for easy analysis:

telco_data['Churn'].replace({'Yes': 1, 'No': 0}, inplace=True)

4. Univariate Analysis
Understanding Distribution of Features:
Visualization techniques are used to analyze the distribution of key features. Histograms and count plots are generated for features like SeniorCitizen, gender, tenure, and others.
Code examples:

sns.countplot(x='Churn', data=telco_data)
sns.histplot(telco_data['tenure'], kde=True)

5. Bivariate Analysis
Understanding relationships between variables:
Relationships between Churn and other features (like Contract, PaymentMethod, etc.) are explored through visualizations:
Count plots are used to see the impact of categorical features on churn:

sns.countplot(x='Contract', hue='Churn', data=telco_data)

Distribution plots for numerical features like MonthlyCharges:

sns.kdeplot(telco_data[telco_data['Churn'] == 1]['MonthlyCharges'], shade=True)

6. Correlation Analysis
Correlation Matrix:
The Pearson correlation coefficient is calculated to observe the correlation between numerical variables:

corr_matrix = telco_data.corr()
sns.heatmap(corr_matrix, annot=True)

Key insights:
Churn is positively correlated with MonthlyCharges but negatively correlated with tenure.

7. Insights from Data
Insights Derived:
Payment Method: Electronic check payment methods show higher churn rates.
Contract Type: Monthly customers have the highest churn due to flexibility in contracts.
Online Security and Tech Support: Customers without these services show higher churn rates.
Senior Citizens: Non-senior citizens have a higher churn rate.

8. Visualizations
Detailed Visualizations:
Various visualizations are created to better understand the data, including:
Bar plots for categorical features
KDE plots for continuous features
Heatmaps for correlations

Example: Distribution of churn across contract types:
sns.countplot(x='Contract', hue='Churn', data=telco_data)

Example: Correlation heatmap:
sns.heatmap(telco_data.corr(), annot=True, fmt='.2f')

Tools Used
Python: The entire EDA is conducted using Python.

Libraries:
pandas for data manipulation.
numpy for numerical operations.
matplotlib and seaborn for data visualization.
sklearn for preprocessing and feature scaling.

Conclusion
The EDA revealed key factors associated with customer churn, such as the method of payment, contract types, and service features. The visualizations and analysis helped uncover important insights that can be used to inform retention strategies.

Key Insights:

Electronic check payments have the highest churn rate.
Monthly contract customers are more likely to churn.
Lack of online security and technical support increases the likelihood of churn.
Non-senior citizens are more prone to churn.
The EDA process provides a foundational understanding of the data and prepares the way for further analysis, such as building predictive models to forecast churn.

Files
Churn Analysis - EDA.ipynb: Contains the complete EDA code.
tel_churn.csv: The cleaned and preprocessed dataset after the EDA.

# Code-Crusaders
SPIT Hackathon Customer Churn Analysis.
![Screenshot 2024-03-23 175745](https://github.com/Ajinkya2101/Code-Crusaders/assets/73093700/f8ac928f-3330-4a1e-94d7-556052149773)
![Screenshot 2024-03-23 175734](https://github.com/Ajinkya2101/Code-Crusaders/assets/73093700/d0b5304e-6b0a-4a47-8039-26eb29fc1670)
![Screenshot 2024-03-23 175704](https://github.com/Ajinkya2101/Code-Crusaders/assets/73093700/7082a805-bc18-48be-90a0-03cd994e68eb)
![Screenshot 2024-03-23 175648](https://github.com/Ajinkya2101/Code-Crusaders/assets/73093700/0b0495a8-8c5e-43d0-9dd1-1c73fe111ded)
![Screenshot 2024-03-23 175622](https://github.com/Ajinkya2101/Code-Crusaders/assets/73093700/2f824690-4bbe-4963-b8d4-14b3068beddf)
![Screenshot 2024-03-23 180354](https://github.com/Ajinkya2101/Code-Crusaders/assets/73093700/2e5bac2e-61a0-4f34-a8cb-17bc4e291262)


