# Wildfire Analysis & Interactive Map 

This is a wildfire analysis project that helps identify wildfire causes using machine learning models with a combined dataset of wildfire and weather data. 

Team members: Jake Li, Jeffrey Ho, Melissa Chen, Min Khant Zaw, Osman Yardimci, Yang Hwi Kim 


## DESCRIPTION [Describe the package in a few paragraphs] 

Our wildfire analysis includes data preprocessing, exploratory data analysis (EDA), modeling, and prediction. We have two files called join_data.py and main.ipynb.  

- join_data.py brings 2 datasets from Kaggle and combines them into one merged CSV file.  

- main.ipynb is the main Jupyter notebook to process analysis and building the model using the merged CSV file that we created from join_data.py.  

main.ipynb:

In more detail of main.ipynb file, data preparation is done in the beginning to cleanse datasets and extract features to be used for modeling. Followed by Exploratory Data Analysis to get an overview of the data by creating visualizations of the data, such as the most frequent causes of wildfires, the number of wildfires per state, fire size distribution.  

For modeling, data is first split into training and testing sets. We used Random Forest Classifier model on the training data to predict wildfire causes based on features that we extracted earlier.  

The model achieved an accuracy rate of approximately 65.34%. Furthermore, feature importance analysis showed that longitude, latitude, and duration are the most influential features in predicting wildfire causes. 

We applied our prediction results to the original dataframe as a new column, "predicted_wildfire_cause_label", and exported the dataframe to a CSV file named final_df_with_results.csv. 

## INSTALLATION [How to install and setup your code] 

First, you need to install the dependencies from requirements.txt in order to run `join_data.py ` and `main.ipynb`. 

Steps 

1. Download datasets: 

- Wildfire: https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires (Rename to “wildfire.sqlite”) 

- Weather for wildfire: https://www.kaggle.com/datasets/leternnoz/188-million-us-wildfires-weather-data  

2. Run `join_data.py` to join the two datasets. 

3. Run `main.ipynb` to clean data, perform exploratory data analysis, and build the model.
Note: You can skip the section “Testing using Basic Model” to save some time. 

4. After running `main.ipynb`, you should be able to see our model results and performance. It should also create a csv file named “final_df_with_results”. This is the csv file we used to create the dashboard in Tableau.

5. Run the SQL query in `fips_edit_query` file to create a state_fips_codes table that we used to assist in creating the dashboard. Export the table as CSV.

6. Load the datasets into Tableau to start creating the dashboard.

## EXECUTION [How to run a demo on your code] 

We combined our prediction results to our dashboard on Tableau.  To see our Tableau dashboard, use the following link: https://public.tableau.com/shared/9GPZPY8FW?:display_count=n&:origin=viz_share_link  