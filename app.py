import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load the formatted sales data
data = pd.read_csv("data/formatted_sales_data.csv")
data = data.sort_values("Date")

# Build the Dash app
app = Dash(__name__)

# Colours used for styling
colors = {
    "background": "#fdf6f0",
    "header": "#d1477a",
    "text": "#3a2e39"
}

app.layout = html.Div(
    style={
        "backgroundColor": colors["background"],
        "fontFamily": "Verdana, sans-serif",
        "padding": "40px"
    },
    children=[
        html.H1(
            children="Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": colors["header"]
            }
        ),

        html.Div(
            children="Explore Pink Morsel sales before and after the price increase on 15 Jan 2021.",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "marginBottom": "30px",
                "fontSize": "16px"
            }
        ),

        html.Div(
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold", "marginRight": "10px"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    inputStyle={"marginRight": "5px", "marginLeft": "15px"}
                )
            ],
            style={"textAlign": "center", "marginBottom": "20px"}
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["Region"] == selected_region]

    fig = px.line(
        filtered_data,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})",
        labels={"Date": "Date", "Sales": "Sales ($)"}
    )

    fig.update_traces(line_color=colors["header"])
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor=colors["background"],
        font_color=colors["text"]
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)