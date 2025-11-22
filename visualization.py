from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

# Dataset 
df = pd.read_csv('./data/combined_daily_sales.csv')
df = df.sort_values(by='date')

app = Dash(__name__)

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales")

app.layout = html.Div([
        html.H1("Soul Foods Pink Morsel Sales Visualization"),
        dcc.Graph(id='line-chart', figure=fig)
    ])

if __name__ == '__main__':
    app.run(debug=True)