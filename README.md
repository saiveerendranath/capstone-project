# Dynamic Property Price Prediction: A Predictive System for Smart Real-Estate Decision

## Project Overview
In today's dynamic real estate market, data-driven insights are essential for making informed property investment decisions. This project Dynamic Property Price Prediction employs machine learning techniques to predict property prices by incorporating not only property details but also key livability factors like proximity to transit, schools, healthcare, and retail amenities.

This repository is designed for data scientists, real estate analysts, and decision-makers who aim to leverage machine learning models and data science techniques for better property price forecasting.

## Demo
https://saiveerendranath.github.io/capstone-project/web-inf/dashboard.html

## Features

- 🔍 Livability Factor Analysis: Identify how location-based amenities like schools, transit, and healthcare impact property prices.
- 🤖 Price Prediction: Build machine learning models to predict residential sale prices.
- 📊 Model Evaluation: Assess and compare various machine learning algorithms' performance.
- 🌍 Geospatial Integration: Incorporate geolocation data and OpenStreetMap API to analyze location-based features.
- 📈 Advanced Modeling: Implement machine learning models like Random Forest, XGBoost, and LightGBM.

## Repository Structure

`Data\`: Raw and cleaned datasets.

`models_py/`: Jupyter Notebooks for model preprocessing, training, and evaluation.

`web-inf/`: Frontend (HTML, JavaScript, CSS) for the dashboard.

`HGBR_Pipeline.pkl`: Serialized model for easy deployment.

`Procfile`: Configuration for deployment platforms like Railway or Heroku.

`requirements.txt`: List of Python libraries needed for the project.

`app.py`: Backend logic for API interactions using FastAPI.

## Dataset Scope and Potential
The dataset used in this project spans residential property sales data from the city of Milwaukee, including property features like square footage, number of rooms, and sale prices, as well as livability data extracted from OpenStreetMap. The dataset offers a foundation for analyzing the relationship between property features and their prices, while also incorporating livability factors to improve prediction accuracy.

In the future, the scope of this dataset can be expanded to include additional cities or regions, which would provide more generalizable insights for property price forecasting across diverse geographic areas.

## Livability Factors

Livability factors refer to measurable elements of the surrounding environment that contribute to how comfortable, convenient, and desirable it is to live in a particular location. In real estate or property price prediction models, livability factors help assess neighborhood quality and accessibility to key amenities, which significantly influence property value.

| Column Name | Description                                                                      |
| ----------- | -------------------------------------------------------------------------------- |
| `TspNum`    | Number of transportation infrastructure points nearby (e.g., bus/train stations) |
| `TspDst`    | Average distance to nearby transportation infrastructure (in meters)             |
| `AtrNum`    | Number of tourist attractions near the property (e.g., parks, landmarks)         |
| `AtrDst`    | Average distance to nearby tourist attractions (in meters)                       |
| `EdcNum`    | Number of educational institutions near the property (e.g., schools, colleges)   |
| `EdcDst`    | Average distance to educational institutions (in meters)                         |
| `HthNum`    | Number of healthcare facilities nearby (e.g., hospitals, clinics)                |
| `HthDst`    | Average distance to healthcare facilities (in meters)                            |
| `RstNum`    | Number of restaurants near the property                                          |
| `RstDst`    | Average distance to nearby restaurants (in meters)                               |
| `RtlNum`    | Number of retail stores/shops in the surrounding area                            |
| `RtlDst`    | Average distance to nearby retail locations (in meters)                          |


## Project Workflow

📊 1. Livability Factor Analysis

-Objective: Identify how nearby amenities impact property prices.
- Methods: Used geolocation data and the OpenStreetMap API to extract proximity to amenities like transit, education, healthcare, and retail.
- Results: Identified significant livability factors that influence the residential sale price in urban areas.

🤖2. Price Prediction

- Objective: Build predictive models to estimate property prices.
- Models Used:
  - Random Forest
  - XGBoost
  - LightGBM
- Findings: Machine learning models such as Random Forest and XGBoost outperformed traditional models, achieving R² values above 0.7.

💵 3. Feature Importance

- Objective: Evaluate the importance of different features in predicting property prices.
- Methods: Generated feature importance plots to identify key predictors, including property size, location, and nearby amenities.
- Results: Features like `FinishedSqft` and district were identified as top predictors.

⏳ 4. Model Evaluation

- Objective: Assess the performance of the machine learning models.
- Evaluation Metrics: 
  - R² Score
  - Mean Squared Error (MSE)
- Findings: XGBoost consistently outperformed other models, achieving the highest R² on test data.

## Dashboard
The project features an interactive dashboard designed to deliver actionable insights into property pricing trends and livability factors. This dashboard provides dynamic visualizations that help stakeholders make informed decisions.
Key Features
-	Geographical Mapping: Interactive maps showing property price trends across the city.
-	Price Predictions: Forecast future property prices using advanced machine learning models.
-	Feature Importance: Visual representation of the most important predictors of property price.

## Future Directions
🌟 Expanding to More Cities:
-	Objective: Analyze data from other metropolitan regions to understand how livability factors influence property prices in different urban settings.
-	Why It Matters: Generalizing findings to different geographic regions will enhance the model’s adaptability and improve its predictive accuracy across various locations.

🔗 Inter-Feature Analysis:
-	Objective: Examine how interactions between different property features (e.g., square footage and district) impact property prices.
-	Why It Matters: Understanding feature interactions will help refine the model and provide more accurate predictions.

🎯 Time-Series Forecasting:
-	Objective: Implement time-series forecasting techniques to predict future property price trends.
-	Why It Matters: Providing forecasts for the next few months will help real estate investors and developers make proactive decisions.

💡 Geospatial Analysis:
-	Objective: Use clustering techniques to group properties by location and livability factors.
-	Why It Matters: Identify areas with similar property values and amenities, supporting targeted real estate investment strategies.

## Acknowledgements
We extend our gratitude to:
- Gayathri Galli
- Pavan Sidhartha Reddymasu
- Sai Veerendranath Naripireddy

Special thanks to **Professor Masoud Soroush**, a faculty member at the University of Maryland, Baltimore County (UMBC), for his invaluable guidance and mentorship throughout this project.

## Conclusion
The Dynamic Property Price Prediction project demonstrates how incorporating livability factors and machine learning models can improve the accuracy of property price predictions. By understanding both property features and surrounding amenities, this project offers valuable insights for real estate investors, home buyers, sellers, and urban planners.
Key Takeaways
-	Livability Factor Analysis: Highlighted the significant impact of livability factors, such as proximity to transit, healthcare, and schools, on property prices. This insight allows for more accurate property valuations and investment decisions.
-	Demand Prediction: Developed robust machine learning models (Random Forest, XGBoost, LightGBM) that identified key predictors of property prices, providing valuable insights for pricing strategies and investment decisions.
-	Feature Importance: Quantified the importance of various features, such as FinishedSqft, district, and nearby amenities, in predicting property prices. These insights can help prioritize the most impactful factors for property valuation.
-	Geospatial Insights: Integrated geospatial data, including proximity to amenities using the OpenStreetMap API, to enhance property price predictions. This enables location-based decision-making for real estate investors and urban planners.

## Impact
-	Optimized Property Investment: Enhances the accuracy of property price predictions, helping investors make informed decisions.
-	Improved Pricing Strategies: Supports real estate agencies in setting competitive prices, improving sales and profitability.
-	Efficient Resource Allocation: Assists urban planners in guiding infrastructure development and zoning in high-demand areas.
-	Data-Driven Decision Making: Provides real-time insights for developers, homebuyers, and sellers to align strategies with market trends.
-	Scalable Approach: Enables the expansion to more cities, offering insights for diverse real estate markets and localized decision-making.

## License
Copyright (c) 2025 Property Price Prediction, Inc.
