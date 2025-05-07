from dash import html, register_page, callback, Input, Output
from dash.exceptions import PreventUpdate
from pages.components import sunburst_graph, grid
import dash_mantine_components as dmc

register_page(
    __name__,
    path='/',
    page_components=[sunburst_graph, grid],
    page_properties={
        grid: {'style': {'display': 'none'}},
    }
)

btn = dmc.Button('Click', id='btn')


@callback(
    Output('get-started-example-basic', 'rowTransaction', allow_duplicate=True),
    Input('btn', 'n_clicks'),
    prevent_initial_call=True,
)
def add_row(nc):
    if not nc:
        raise PreventUpdate
    row = {'direction': 'FIRST PAGE', 'strength': '99++', 'frequency': 0.1}
    return {'add': [row]}


layout = html.Div([html.H2("Sunburst"), btn])
