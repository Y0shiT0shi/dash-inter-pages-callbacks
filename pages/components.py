import plotly.express as px
from dash import dcc
import dash_ag_grid as dag
import pandas as pd


df_iris = px.data.iris()

# Sunburst graph.
fig = px.sunburst(df_iris, path=['species', 'sepal_width', 'sepal_length'])
sunburst_graph = dcc.Graph(figure=fig)


# Bar graph.
fig = px.bar(df_iris, x="sepal_width", y="sepal_length")
bar_graph = dcc.Graph(figure=fig)


df_grid = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv").head(5)

columnDefs = [
    { 'field': 'direction' },
    { 'field': 'strength' },
    { 'field': 'frequency'},
]

grid = dag.AgGrid(
    id="get-started-example-basic",
    rowData=df_grid.to_dict("records"),
    columnDefs=columnDefs,
    persistence=True,
    persisted_props=['rowData'],
    persistence_type='local'
)
