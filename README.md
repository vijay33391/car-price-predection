# Car Market Analysis and Price Prediction

## Problem Statement

A car company is expanding into the USA market and aims to predict car prices based on various factors like car features, specifications, and brand reputation. To solve this problem, we built a machine learning pipeline using exploratory data analysis (EDA), feature engineering, and model selection to develop a price prediction model. The model was deployed on Streamlit Cloud for easy access and use. We began with a Linear Regression model, then improved the model using various techniques such as L1 (Lasso), L2 (Ridge), SVM (Support Vector Machine), and ensemble methods to achieve a significant accuracy improvement.

The final model achieved an accuracy improvement from 80% to 91%, showing the power of advanced feature engineering and model selection in predicting car prices effectively.

## Technologies Used

- **Machine Learning**: Linear Regression, Lasso (L1), Ridge (L2), SVM, Ensemble methods
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
   - Start with Linear Regression as a baseline model.
   - Compare model performance using evaluation metrics (e.g., R-squared, MAE, MSE).
   
5. **Improvement of Model Performance**:
   - Use L1 (Lasso) and L2 (Ridge) regularization techniques to prevent overfitting.
   - Apply Support Vector Machines (SVM) for more complex decision boundaries.
   - Implement ensemble methods like XGBoost, LightGBM to increase accuracy.

6. **Deployment**:
   - Deploy the model using Streamlit Cloud for easy user interaction and real-time prediction.

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
2. **L1 (Lasso)**: Regularization technique used to reduce overfitting and improve model generalization.
3. **L2 (Ridge)**: Another regularization technique to penalize large coefficients and prevent overfitting.
4. **SVM**: A more advanced model for predicting non-linear relationships, improving accuracy.
5. **Ensemble Methods**: Techniques like XGBoost and LightGBM were used to combine predictions of weaker models and boost performance, increasing the accuracy to 91%.

## Results

- Initial accuracy: 80%
- Improved accuracy after model tuning: 91%

## Deployment

The final model was deployed on **Streamlit Cloud** to allow users to input car features and predict the market price. The application is user-friendly and provides real-time predictions.

### Link to Application: [Streamlit Model Deployment](https://your-streamlit-link.com)

---

## Conclusion

Through extensive model selection and feature engineering, we have developed a robust car price prediction model. By implementing various techniques like Lasso, Ridge, SVM, and ensemble methods, we achieved a significant increase in accuracy, moving from 80% to 91%. The model is now deployed and available for use via Streamlit Cloud. 

