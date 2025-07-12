import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

# Load data
df_states = pd.read_csv("data/state_monthly_sales.csv")
df_cat = pd.read_csv("data/category_trends.csv")
df_forecast = pd.read_csv("data/forecast.csv")

# Aggregate for map
latest_month = df_states["Month"].max()
df_latest = df_states[df_states["Month"] == latest_month]

# U.S. state codes for choropleth
state_abbrev = {
    "California": "CA", "Texas": "TX", "New York": "NY", "Florida": "FL",
    "Illinois": "IL", "Ohio": "OH", "Georgia": "GA", "Pennsylvania": "PA",
    "North Carolina": "NC", "Michigan": "MI"
}
df_latest = df_latest.copy()
df_latest["StateCode"] = df_latest["State"].map(state_abbrev)

# Build plots
fig_map = px.choropleth(
    df_latest,
    locations="StateCode",
    locationmode="USA-states",
    color="Sales",
    scope="usa",
    title="Latest Monthly Sales by State",
    color_continuous_scale="Blues"
)

fig_category = px.line(
    df_cat,
    x="Month",
    y="Sales",
    color="Category",
    title="Monthly Sales Trend by Product Category"
)

fig_forecast = px.bar(
    df_forecast,
    x="Month",
    y="Forecasted_Sales",
    title="Forecasted Sales for Next 6 Months",
    text_auto=True
)

# Dash App Layout
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("E-commerce Regional Sales Dashboard", style={"textAlign": "center", "fontWeight": "bold"}),

    html.Div([
        dcc.Graph(figure=fig_map)
    ], style={"marginBottom": "40px"}),

    html.Div([
        dcc.Graph(figure=fig_category)
    ], style={"marginBottom": "40px"}),

    html.Div([
        dcc.Graph(figure=fig_forecast)
    ])
])

# Save dashboard as HTML and PNG
os.makedirs("outputs", exist_ok=True)
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Run app and export
if __name__ == "__main__":
    app.run(debug=False)
