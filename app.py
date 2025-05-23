from dash import Dash, dcc, html, page_container, page_registry, callback, Input, Output, State
from dash_extensions.pages import setup_page_components
import dash_mantine_components as dmc


app = Dash(__name__, use_pages=True)

logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"

layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Image(src=logo, h=40),
                    dmc.Title("Demo App", c="blue"),
                ],
                h="100%",
                px="md",
            )
        ),

        dmc.AppShellNavbar(
            id="navbar",
            children=[
                "Navbar",
                *[dmc.NavLink(label=p['name'], href=p['path']) for p in page_registry.values()],
            ],
            p="md",
        ),

        dmc.AppShellMain(html.Div([page_container, setup_page_components()])),
    ],
    header={"height": 60},
    padding="md",
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    id="appshell",
)


app.layout = dmc.MantineProvider(layout)


@callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def navbar_is_open(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened}
    return navbar


if __name__ == "__main__":
    app.run(debug=True)
