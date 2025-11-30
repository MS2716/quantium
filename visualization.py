from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Dataset
df = pd.read_csv('./data/combined_daily_sales.csv')
df = df.sort_values(by='date')

# Get list of regions and add 'All'
regions = df['region'].unique().tolist()
regions.insert(0, 'All')

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualization"),

    dcc.RadioItems(
        id='region-radio',
        options=[{'label': i, 'value': i} for i in regions],
        value='All',
        labelStyle={'display': 'inline-block', 'margin-right': '10px', 'font-size': '20px', 'color': '#333'}
    ),

    dcc.Graph(id='line-chart')
])

@app.callback(
    Output('line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    if selected_region == 'All':
        fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales for All Regions")
    else:
        filtered_df = df[df['region'] == selected_region]
        fig = px.line(filtered_df, x="date", y="sales", title=f"Pink Morsel Sales for {selected_region}")
    return fig

if __name__ == '__main__':
    app.run(debug=True)