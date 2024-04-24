# app.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Sample data for Era 1, Era 2, and Era 3
era1_data = {'player': ['Player A', 'Player B', 'Player C'],
             'matches_won': [50, 60, 70]}

era2_data = {'player': ['Player X', 'Player Y', 'Player Z'],
             'matches_won': [55, 65, 75]}

era3_data = {'player': ['Player M', 'Player N', 'Player O'],
             'matches_won': [45, 55, 65]}

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Tennis Trivia", style={'textAlign': 'center'}),
    html.Div(id='era-selector', children=[
        html.Button('Era 1', id='era1-btn', n_clicks=0, className='era-button'),
        html.Button('Era 2', id='era2-btn', n_clicks=0, className='era-button'),
        html.Button('Era 3', id='era3-btn', n_clicks=0, className='era-button')
    ]),
    html.Div(id='era-content')
], className='dark-theme')

# Callback to update the content based on the selected era
@app.callback(
    Output('era-content', 'children'),
    [Input('era1-btn', 'n_clicks'),
     Input('era2-btn', 'n_clicks'),
     Input('era3-btn', 'n_clicks')]
)
def update_era_content(era1_clicks, era2_clicks, era3_clicks):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'era1-btn':
        era_data = era1_data
    elif button_id == 'era2-btn':
        era_data = era2_data
    else:
        era_data = era3_data

    return html.Div([
        html.H2(f"Era {button_id[-1]} Performance"),
        dcc.Graph(
            figure={
                'data': [
                    {'x': era_data['player'], 'y': era_data['matches_won'], 'type': 'bar', 'name': 'Matches Won'}
                ],
                'layout': {
                    'title': f'Era {button_id[-1]} Performance',
                    'xaxis': {'title': 'Player'},
                    'yaxis': {'title': 'Matches Won'}
                }
            }
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
