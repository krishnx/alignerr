import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)
np.random.seed(42)

states = ["California", "Texas", "New York", "Florida", "Illinois", "Ohio", "Georgia", "Pennsylvania", "North Carolina", "Michigan"]
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"]

months = pd.date_range("2023-01-01", "2024-12-01", freq="MS").strftime("%Y-%m").tolist()

# Monthly Sales per State
state_sales_data = []
for state in states:
    for month in months:
        sales = np.random.randint(50000, 200000)
        state_sales_data.append([state, month, sales])

df_states = pd.DataFrame(state_sales_data, columns=["State", "Month", "Sales"])
df_states.to_csv("data/state_monthly_sales.csv", index=False)

# Category Sales Trends
category_trend_data = []
for category in categories:
    for month in months:
        sales = np.random.randint(20000, 100000)
        category_trend_data.append([category, month, sales])

df_cat = pd.DataFrame(category_trend_data, columns=["Category", "Month", "Sales"])
df_cat.to_csv("data/category_trends.csv", index=False)

# Forecast Data (dummy future predictions)
forecast_data = []
for month in pd.date_range("2025-01-01", "2025-06-01", freq="MS").strftime("%Y-%m"):
    sales = np.random.randint(300000, 500000)
    forecast_data.append([month, sales])

df_forecast = pd.DataFrame(forecast_data, columns=["Month", "Forecasted_Sales"])
df_forecast.to_csv("data/forecast.csv", index=False)
