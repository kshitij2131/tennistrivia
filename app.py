import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import era1
import era2
import era3
import news

app = dash.Dash(__name__)

nav_buttons = html.Div([
    html.Button('Era 1', id='era1-button', n_clicks=0, style={'margin-right': '10px'}),
    html.Button('Era 2', id='era2-button', n_clicks=0, style={'margin-right': '10px'}),
    html.Button('Era 3', id='era3-button', n_clicks=0, style={'margin-right': '10px'}),
    html.Button('Recent News', id='news-button', n_clicks=0)
], style={'margin-bottom': '20px'})

page_content = era1.app.layout

app.layout = html.Div([
    nav_buttons,
    html.Div(id='page-content', children=page_content)
])

#era1
@app.callback(
    Output('page-content', 'children'),
    Input('era1-button', 'n_clicks')
)
def display_era1_layout(n_clicks):
    if n_clicks > 0:
        return era1.app.layout


#era2
@app.callback(
    Output('page-content', 'children'),
    Input('era2-button', 'n_clicks')
)
def display_era2_layout(n_clicks):
    if n_clicks > 0:
        return era2.app.layout
    

#era3
@app.callback(
    Output('page-content', 'children'),
    Input('era3-button', 'n_clicks')
)
def display_era3_layout(n_clicks):
    if n_clicks > 0:
        return era3.app.layout

#news.py
@app.callback(
    Output('page-content', 'children'),
    Input('news-button', 'n_clicks')
)
def display_news_layout(n_clicks):
    if n_clicks > 0:
        return news.app.layout

if __name__ == '__main__':
    app.run_server(debug=True)
