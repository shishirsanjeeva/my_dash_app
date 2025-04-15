from dash import Input, Output
import numpy as np
import plotly.graph_objs as go

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
        #x = np.linspace(1, sigma_mean)
        if formula == 'GM':
            fatigue_limit = sigma_alt / (1 - (sigma_mean / strength))
        elif formula == 'SB':
            fatigue_limit = x
        else:
            y = x

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[sigma_mean,0], y=[0, fatigue_limit], mode='lines', name='New-Fatigue limit'))
        fig.add_trace(go.Scatter(x=[sigma_mean,0], y=[0, endurance_strength], mode='lines', name='Endurance Strength'))
        #fig.add_trace(go.Scatter(x=x, y=fatigue_limit, mode='lines', name='y'))
        fig.update_layout(title='Formula Output', xaxis_title='x', yaxis_title='y')
        return fig
    