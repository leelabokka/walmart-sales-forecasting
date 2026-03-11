# 🛒 Walmart Sales Forecasting Using Machine Learning

Real-time prediction of Walmart weekly sales using **Machine Learning algorithms** to analyze historical data and forecast future trends.

---

## 📌 Project Description

Retail businesses rely heavily on accurate sales predictions to manage inventory and optimize operations. This project forecasts weekly store sales for Walmart using machine learning techniques.

It analyzes historical sales data along with various economic and environmental factors such as:

- Temperature 🌡️  
- Fuel prices ⛽  
- CPI (Consumer Price Index) 📈  
- Unemployment rate 📊  
- Holiday indicators 🎉  

By identifying patterns, the model predicts future sales trends, helping businesses make better decisions for **inventory management** and **demand planning**.

---

## 🚀 Features

### Sales Forecasting
- Predicts weekly Walmart store sales  
- Uses historical sales data for training  
- Helps in inventory and demand management  

### Data Processing
- Data cleaning and preprocessing 🧹  
- Date conversion and feature extraction 📅  
- Handling economic indicators  

### Machine Learning Model
- **Random Forest Regression** algorithm 🌲  
- Handles large datasets efficiently  
- Reduces overfitting  

### Visualization
- Graph showing **Actual vs Predicted Sales** 📊  
- Helps understand model performance  

---

## 📂 Dataset

The dataset includes:

| Attribute | Description |
|-----------|-------------|
| Store ID | Unique identifier for the store |
| Date | Week of sales data |
| Weekly Sales | Target variable |
| Holiday Flag | Whether the week includes a holiday |
| Temperature | Average weekly temperature |
| Fuel Price | Fuel cost per gallon |
| CPI | Consumer Price Index |
| Unemployment Rate | Unemployment percentage |

---

## 🛠 Technologies Used

- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Machine Learning (Random Forest Regression)  

---

## 🧩 Machine Learning Model

**Random Forest Regression** was used to train the model and predict weekly sales. Advantages:

- Works well with structured data  
- Handles nonlinear relationships  
- Provides high prediction accuracy  

---

## 📈 Model Evaluation

| Metric | Value |
|--------|-------|
| Mean Squared Error (MSE) | 13,020,256,696.91 |
| Root Mean Squared Error (RMSE) | 114,106.33 |
| R² Score | 0.96 |

✅ **R² Score of 0.96** indicates strong predictive performance.

---

## 📁 Project Structure


walmart-sales-forecasting/
│
├── main.py
├── Walmart.csv
├── requirements.txt
└── README.md


---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/leelabokka/walmart-sales-forecasting.git

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py
🔮 Future Improvements

Implement additional ML algorithms

Create a web dashboard for predictions

Add real-time sales forecasting

Deploy the model as a web application