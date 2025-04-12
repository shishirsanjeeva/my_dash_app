from dash import Dash
from layout import serve_layout
from callbacks import register_callbacks

app = Dash(__name__)
app.title = "Formula Calculator"
app.layout = serve_layout()

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)