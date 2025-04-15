from dash import html, dcc

def serve_layout():
    return html.Div([
        html.H1("Interactive Formula Tool"),

        html.Div([
            html.Label("Select Formula"),
            dcc.Dropdown(
                id='formula-choice',
                options=[
                    {'label': 'y = a * x + b', 'value': 'linear'},
                    {'label': 'y = a * x^2 + b * x + c', 'value': 'quadratic'}
                ],
                value='linear'
            ),
        ], style={"margin": "10px 0"}),

        html.Div([
            html.Label("Coefficient a"),
            dcc.Input(id='a-input', type='number', value=1, step=0.1),
        ], style={"margin": "10px 0"}),

        html.Div([
            html.Label("Coefficient b"),
            dcc.Input(id='b-input', type='number', value=0, step=0.1),
        ], style={"margin": "10px 0"}),

        html.Div([
            html.Label("Coefficient c (only for quadratic)"),
            dcc.Input(id='c-input', type='number', value=0, step=0.1),
        ], style={"margin": "10px 0"}),

        html.Hr(),
        dcc.Graph(id='output-graph')
    ])
