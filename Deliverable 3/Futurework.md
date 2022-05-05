## Data Uniqueness
This dataset provides daily updates on the volume of US job listings filtered by geography industry job family and role; normalized to pre-covid levels. On average data from 70% of all new US jobs are captured, and the dataset currently contains data from 3.3 million hiring organizations. The data set is configured into 7 csv files comprising 9.2+MB data with 394393 valid Records.

## Data understanding and Exploratory Data Analysis
- Data type, data range constraints
- Looking for missing data
- Looking for inconsistencies in data
- Visualizing the above to get a better insight in the uniformity or the inconsistencies
- Understanding and comparing distribution through histograms, CDF, Q-plots
- Visualizing relationships between the variables

## Data Preparation
 - Handling missing data with imputation or deletion (preferably imputation)
- Handling the scaling and normalizing of the data
- Dealing with pre-processing feature engineering: encoding, handling numerical and date variables
- Removing the redundancy
- Checking correlation via a matrix and plot to understand which variables to select

## Machine Learning (Supervised)
Supervised learning models to forecast the overall favorability of the job market for job seekers.

## Evaluation 
Linear regression model has been implemented based on geography, industry, job_family and overall to analyse the impact of covid-19 on the job market. Evaluation shows improvement in the job market. We considered month vise variation in the data in different catogories. Our linear regression model gives us an accuracy of 71.2%.

## Future Work
- Capital Ventures to give more insight into the best industries to invest in.
- To give insights on the best location and industries for start-ups.
- For students who want to pursue their careers, we can give an insight into how each industry is trending in each location and help choose their concentration based on the data.