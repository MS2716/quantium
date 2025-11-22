from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

# Dataset 
df = pd.read_csv('./data/combined_daily_sales.csv')

app = Dash(__name__)

# Using plotly.express is simpler for this task.
# It automatically handles mapping the 'region' column to different colors and creates a legend.
fig = px.line(df, x="date", y="sales", color="region", title="Daily Sales")

# The original approach with graph_objects would require looping through regions
# fig = go.Figure(data=go.Scatter(x=df['date'], y=df['sales'], mode='markers', marker=dict(color=df['region'])), layout=go.Layout(title='Daily Sales'))

app.layout = html.Div([
        html.H1("Soul Foods Sales Dashboard"),
        dcc.Graph(id='line-chart', figure=fig)
    ])

if __name__ == '__main__':
    app.run(debug=True)