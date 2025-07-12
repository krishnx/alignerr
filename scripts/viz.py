import pandas as pd
import plotly.express as px
import os

df = pd.read_csv("data/sales_hierarchy.csv")

# Create Sunburst chart
fig = px.sunburst(
    df,
    path=["Category", "Subcategory", "Region"],
    values="Sales",
    color="Category",
    color_discrete_sequence=px.colors.qualitative.Set2,
    title="Sales Distribution by Category, Subcategory, and Region"
)

# Save visual output
os.makedirs("outputs", exist_ok=True)
fig.write_html("outputs/dashboard.html")
fig.write_image("outputs/screenshot.png")
