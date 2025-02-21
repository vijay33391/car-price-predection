Here's the updated **README** file with the **Hyperparameter Tuning** and the addition of **Decision Tree** and **Random Forest** models in the **Problem Workflow**:

---

# Car Market Analysis and Price Prediction

## Problem Statement

A car company is expanding into the USA market and aims to predict car prices based on various factors like car features, specifications, and brand reputation. To solve this problem, we built a machine learning pipeline using exploratory data analysis (EDA), feature engineering, and model selection to develop a price prediction model. The model was deployed on Streamlit Cloud for easy access and use. We began with a Linear Regression model, then improved the model using various techniques such as L1 (Lasso), L2 (Ridge), SVM (Support Vector Machine), Decision Tree, Random Forest, and ensemble methods to achieve a significant accuracy improvement.

The final model achieved an accuracy improvement from 80% to 91%, showing the power of advanced feature engineering, model selection, and hyperparameter tuning in predicting car prices effectively.

## Technologies Used

- **Machine Learning**: Linear Regression, Lasso (L1), Ridge (L2), SVM, Decision Tree, Random Forest, Ensemble methods
- **Data Analysis**: Python, Pandas, Numpy, Matplotlib, Seaborn
- **Model Deployment**: Streamlit
- **Libraries**: Scikit-learn, XGBoost, LightGBM, etc.

## Problem Workflow

1. **Data Preprocessing**:
   - Clean the data to handle missing values, outliers, and categorical variables.
   - Normalize or scale numerical features for better model performance.

2. **Exploratory Data Analysis (EDA)**:
   - Analyze trends, relationships, and patterns in the dataset using visualization tools.
   - Identify important features that influence car pricing.

3. **Feature Engineering**:
   - Create new features based on the existing data (e.g., combining car features or encoding categorical data).
   - Select the most important features using feature importance techniques.

4. **Model Selection and Benchmarking**:
   - Start with **Linear Regression** as a baseline model.
   - Add **Decision Tree** and **Random Forest** models to the pipeline for more complex decision-making.
   - Compare model performance using evaluation metrics (e.g., R-squared, MAE, MSE).

5. **Hyperparameter Tuning**:
   - Use techniques like **Grid Search** and **Random Search** to fine-tune the hyperparameters of models such as Decision Tree, Random Forest, and other selected algorithms to improve performance.
   - Hyperparameters tuned include tree depth, number of estimators, learning rate, etc.

6. **Improvement of Model Performance**:
   - Apply **L1 (Lasso)** and **L2 (Ridge)** regularization techniques to prevent overfitting.
   - Use **SVM** to model complex, non-linear relationships.
   - Implement ensemble methods like **XGBoost**, **LightGBM** to combine weaker models for higher accuracy.

7. **Deployment**:
   - Deploy the model using **Streamlit Cloud** for easy user interaction and real-time prediction.

## Data Dictionary

| Column Name         | Description                                                                                 | Type        |
|---------------------|---------------------------------------------------------------------------------------------|-------------|
| **Car_ID**           | Unique identifier for each observation                                                      | Integer     |
| **Symboling**        | Assigned insurance risk rating. +3 is high risk, -3 is low risk                             | Categorical |
| **carCompany**       | Name of the car manufacturer                                                                 | Categorical |
| **fueltype**         | Type of fuel used by the car (e.g., gas or diesel)                                          | Categorical |
| **aspiration**       | Type of aspiration used in the car (e.g., turbo or standard)                                | Categorical |
| **doornumber**       | Number of doors on the car                                                                   | Categorical |
| **carbody**          | Style of the car body (e.g., sedan, hatchback)                                               | Categorical |
| **drivewheel**       | Type of drive wheel configuration (e.g., front-wheel, rear-wheel, or all-wheel drive)      | Categorical |
| **enginelocation**   | Location of the car's engine (front or rear)                                                | Categorical |
| **wheelbase**        | Distance between the front and rear axles of the car                                        | Numeric     |
| **carlength**        | Total length of the car                                                                      | Numeric     |
| **carwidth**         | Total width of the car                                                                       | Numeric     |
| **carheight**        | Total height of the car                                                                      | Numeric     |
| **curbweight**       | Weight of the car without passengers or baggage                                              | Numeric     |
| **enginetype**       | Type of engine used in the car (e.g., DOHC, SOHC)                                            | Categorical |
| **cylindernumber**   | Number of cylinders in the engine                                                            | Categorical |
| **enginesize**       | Displacement of the engine (in cubic inches or liters)                                       | Numeric     |
| **fuelsystem**       | Type of fuel system used in the car (e.g., MPFI, carburetor)                                | Categorical |
| **boreratio**        | Ratio of the bore (diameter) of the cylinder                                                 | Numeric     |
| **stroke**           | Length of the stroke within the engine cylinder                                             | Numeric     |
| **compressionratio** | Ratio of the volume of the combustion chamber from its largest to smallest capacity          | Numeric     |
| **horsepower**       | Power output of the engine (in horsepower)                                                   | Numeric     |
| **peakrpm**          | Maximum revolutions per minute (RPM) of the engine                                           | Numeric     |
| **citympg**          | Fuel efficiency in city driving conditions (in miles per gallon)                             | Numeric     |
| **highwaympg**       | Fuel efficiency on highways (in miles per gallon)                                            | Numeric     |
| **price**            | Market price of the car (Dependent variable)                                                | Numeric     |

## Model Evaluation

The following models were tested:

1. **Linear Regression**: Initial baseline model, providing 80% accuracy.
2. **Decision Tree**: A tree-based algorithm that splits data based on feature values to make predictions.
3. **Random Forest**: An ensemble of Decision Trees that aggregates predictions for better accuracy.
4. **L1 (Lasso)**: Regularization technique used to reduce overfitting and improve model generalization.
5. **L2 (Ridge)**: Another regularization technique to penalize large coefficients and prevent overfitting.
6. **SVM**: A more advanced model for predicting non-linear relationships, improving accuracy.
7. **Ensemble Methods**: Techniques like XGBoost and LightGBM were used to combine predictions of weaker models and boost performance, increasing the accuracy to 91%.

## Hyperparameter Tuning

To improve the model's performance, hyperparameter tuning was performed using techniques like **Grid Search** and **Random Search**. Key hyperparameters tuned include:

- **Decision Tree**:
  - Maximum depth of the tree (`max_depth`)
  - Minimum samples required to split a node (`min_samples_split`)
  - Minimum samples required at each leaf node (`min_samples_leaf`)

- **Random Forest**:
  - Number of trees in the forest (`n_estimators`)
  - Maximum depth of the trees (`max_depth`)
  - Minimum samples required to split a node (`min_samples_split`)

- **SVM**:
  - Regularization parameter (`C`)
  - Kernel type (`kernel`)
  - Gamma parameter for non-linear kernels (`gamma`)

- **Ensemble Methods (XGBoost, LightGBM)**:
  - Learning rate (`learning_rate`)
  - Number of estimators (`n_estimators`)
  - Maximum depth (`max_depth`)
  - Subsample ratio (`subsample`)

By performing hyperparameter tuning, we were able to find the best set of parameters for each model, leading to improved accuracy and better performance.

## Conclusion: Exploratory Data Analysis (EDA)

Through the EDA process, several key insights were gained that helped shape the understanding of the relationships between features and car prices:

1. **Engine Size and Price**:
   - There is a strong positive correlation (0.9) between engine size and price. Larger engine sizes typically lead to higher prices, emphasizing the importance of engine specifications in determining a car's value.

2. **Fuel Efficiency**:
   - Diesel cars generally exhibit better fuel efficiency than gasoline cars, making them a more economical choice for long-distance travel. This insight is valuable when considering both price and operating costs for different types of vehicles.

3. **Horsepower and City Mileage**:
   - A negative correlation (-0.7) was observed between horsepower and city mileage. Cars with higher horsepower tend to have lower fuel efficiency in city driving conditions, highlighting the trade-off between performance and fuel economy.

4. **Drivewheel Configuration**:
   - Sedans are more likely to feature front-wheel drive compared to Hardtops, suggesting that sedans prioritize practicality and efficiency, which can impact their pricing and consumer preference.

5. **Weight and Acceleration**:
   - There is a significant negative correlation (-0.8) between a car's weight and its acceleration. Heavier cars generally accelerate slower, which can influence the car's market position, especially for those seeking higher performance.

6. **Car Body and Price**:
   - Convertibles tend to be associated with the highest prices among car body types. This is likely due to their appeal as luxury vehicles and their design, which influences their higher market value.

7. **Engine Type and Price**:
   - The type of engine in a car significantly influences its price. Specifically, OHV (Overhead Valve) engines have the most significant impact on price increases, underlining how engine technology affects a car's cost.

These insights from EDA were crucial in guiding the feature engineering process and refining the models to predict car prices more accurately.

## Results

- Initial accuracy: 80%
- Improved accuracy after model tuning: 91%

## Deployment

The final model was deployed on **Streamlit Cloud** to allow users to input car features and predict the market price. The application is user-friendly and provides real-time predictions.

### Link to Application: [Streamlit Model Deployment](https://car-price-predection-dx2zae5hc3xqh7uydgpnh8.streamlit.app/)

---

## Conclusion

Through extensive model selection, hyperparameter tuning, and feature engineering, we have developed a robust car price prediction model. By implementing various techniques like Lasso, Ridge, SVM, Decision Trees, Random Forests, and ensemble methods, we achieved a significant increase in accuracy, moving from 80% to 91%. The model is now deployed and available for use via Streamlit Cloud. 

