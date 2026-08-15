import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load the formatted sales data
data = pd.read_csv("data/formatted_sales_data.csv")

# Make sure the data is sorted by date
data = data.sort_values("Date")

# Create the line chart
fig = px.line(
    data,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Sales ($)"}
)

# Build the Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Pink Morsel Sales Visualiser"),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)