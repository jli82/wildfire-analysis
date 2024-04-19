# Wildfire Analysis.

This is a wildfire analysis project that helps identify wildfire causes using machine learning models with a combined dataset of wildfire and weather data. <br />

## by Team 173

- Jake Li
- Jeffrey Ho
- Melissa Chen
- Min Khant Zaw
- Osman Yardimci
- Yang Hwi Kim 

## DESCRIPTION
Our wildfire analysis includes data preprocessing, exploratory data analysis (EDA), model training, and prediction. 
In the package, we have two files called join_data.py and main.ipynb. join_data.py brings 2 datasets from Kaggle and combines them into one merged CSV file. main.ipynb is the main Jupyter notebook to process analysis using the merged CSV file that we created from join_data.py. The analysis provides insights into the most frequent causes of wildfires, the distribution of wildfires across states, and the impact of environmental factors on wildfire occurrence. 

In more detail of main.ipynb file, data preparation is done in the beginning to cleanse datasets and extract features to be used for modeling. Exploratory Data Analysis is proceeded to get visualizations of the data, such as the most frequent causes of wildfires, the number of wildfires per state, fire size distribution. For modeling, data is first split into training and testing sets. We used Random Forest Classifier model on the training data to predict wildfire causes based on features that we extracted earlier. The model achieved an accuracy rate of approximately 65.34%. Furthermore,feature importance analysis showed that longitude, latitude, and duration are the most influential features in predicting wildfire causes.

We applied above results to the dataframe, and a new column "predicted_wildfire_cause_label" is created.
The dataframe with the results got exported to a CSV file named final_df_with_results.csv.

## INSTALLATION

  ### 1. Download 2 data sets from Kaggle
    [weather dataset](https://www.kaggle.com/datasets/leternnoz/188-million-us-wildfires-weather-data)
    [wildfire dataset](https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires)
  
  ### 2. Install dependencies
    Ensure you have Python installed. Then, install the required Python packages using pip:
    ```bash
    pip install pandas matplotlib seaborn numpy scikit-learn xgboost imbalanced-learn statsmodels
    ```

## Execution

  ### 1. Obtain merged dataset
    Run the join_data.py script to merge datasets:
    ```bash
    python join_data.py
    ```
    * You may have to change file name or path accordingly
    This script will generate a file named merged_df.csv containing the merged dataset from 2 data from Kaggle.
  
  ### 2. Execute main.ipynb
    Open Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
  Then navigate to the location of main.ipynb and open the file in Jupyter Notebook.
  Execute cells accordingly to get the analysis and modeling results. In the end, it will export the results to a CSV file named final_df_with_results.csv and display various        plots analyzing the data temporally (by month, week, and season).
