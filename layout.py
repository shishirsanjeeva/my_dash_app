from dash import html, dcc

def serve_layout():
    return html.Div([
        html.H2("Fatigue Formula Tool"),

        html.Div([
            html.Label("Select Formula"),
            dcc.Dropdown(
                id='formula-choice',
                options=[
                    {'label': 'GoodMan', 'value': 'GM'},
                    {'label': 'Soderberg', 'value': 'SB'}
                ],
                value='GM'
            ),
        ], style={"margin": "10px 0"}),

        html.Div([
            html.Label("Mean Stress"),
            dcc.Input(id='meanS', type='number', value=200, step=0.1),
        ], style={"margin": "10px 0"}),

        html.Div([
            html.Label("Alt Stress"),
            dcc.Input(id='altS', type='number', value=0, step=0.1),
        ], style={"margin": "10px 0"}),

        html.Div([
            html.Label("Strength"),
            dcc.Input(id='strength', type='number', value=250, step=0.1),
        ], style={"margin": "10px 0"}),

        html.Div([
            html.Label("Endurance Strength"),
            dcc.Input(id='end-strength', type='number', value=200, step=0.1),
        ], style={"margin": "10px 0"}),

        html.Hr(),
        dcc.Graph(id='output-graph')
    ])
