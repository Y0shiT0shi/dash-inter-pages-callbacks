from dash import html, register_page, callback, Input, Output
from dash.exceptions import PreventUpdate
from pages.components import sunburst_graph, grid
import dash_mantine_components as dmc


title = "Sunburst and Bar"

register_page(
    __name__,
    path=f'/bar',
    page_components=[sunburst_graph, grid],
)

btn = dmc.Button('Click', id='btn2')


@callback(
    Output('get-started-example-basic', 'rowTransaction', allow_duplicate=True),
    Input('btn2', 'n_clicks'),
    prevent_initial_call=True,
)
def add_row2(nc):
    if not nc:
        raise PreventUpdate
    row = {'direction': 'SECOND PAGE', 'strength': '99++', 'frequency': 0.1}
    return {'add': [row]}


layout = html.Div([html.H2(title), btn])
