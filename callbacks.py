from dash import Input, Output
import numpy as np
import plotly.graph_objs as go

def register_callbacks(app):
    @app.callback(
        Output('output-graph', 'figure'),
        Input('formula-choice', 'value'),
        Input('a-input', 'value'),
        Input('b-input', 'value'),
        Input('c-input', 'value')
    )
    def update_graph(formula, a, b, c):
        x = np.linspace(-10, 10, 200)
        if formula == 'linear':
            y = a * x + b
        elif formula == 'quadratic':
            y = a * x**2 + b * x + c
        else:
            y = x

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y'))
        fig.update_layout(title='Formula Output', xaxis_title='x', yaxis_title='y')
        return fig
    