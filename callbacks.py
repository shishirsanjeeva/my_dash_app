from dash import Input, Output
import numpy as np
import plotly.graph_objs as go
from formulas import calculate_y

def register_callbacks(app):
    @app.callback(
        Output('output-graph', 'figure'),
        
        Input('formula-choice', 'value'),
        Input('meanS', 'value'),
        Input('altS', 'value'),
        Input('strength', 'value'),
        Input('end-strength', 'value')
    )
    def update_graph(formula, sigma_mean, sigma_alt, strength, endurance_strength):
        sigma_mean = float(sigma_mean)
        fatigue_limit = calculate_y(formula, sigma_mean, sigma_alt, strength)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[sigma_mean,0], y=[0, fatigue_limit], mode='lines', name='New-Fatigue limit'))
        fig.add_trace(go.Scatter(x=[sigma_mean,0], y=[0, endurance_strength], mode='lines', name='Limit'))
        #fig.add_trace(go.Scatter(x=x, y=fatigue_limit, mode='lines', name='y'))
        fig.update_layout(title='Formula Output', xaxis_title='x', yaxis_title='y')
        return fig
    