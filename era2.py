import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import base64
import era1, era3, news

app = dash.Dash(__name__)

surfaces = ['Grass', 'Clay', 'Hard']
tournaments = ['Australian_Open', 'French_Open', 'Wimbledon', 'US_Open']
players = ['Agassi', 'Becker', 'Edberg', 'Sampras']

tournament_options = [
    {'label': 'Australian Open', 'value': 'Australian_Open'},
    {'label': 'French Open', 'value': 'French_Open'},
    {'label': 'Wimbledon', 'value': 'Wimbledon'},
    {'label': 'US Open', 'value': 'US_Open'}
]
player_options = [
    {'label': 'Andre Agassi', 'value': 'Agassi'},
    {'label': 'Boris Becker', 'value': 'Becker'},
    {'label': 'Stefan Edberg', 'value': 'Edberg'},
    {'label': 'Pete Sampras', 'value': 'Sampras'}
]

def read_image(filename):
    with open(filename, 'rb') as f:
        image = base64.b64encode(f.read()).decode('ascii')
    return f'data:image/png;base64,{image}'

def read_surfaceRecords(player_name):
    filename = f"data/era2/surfaceRecords/{player_name}.csv"
    player_data = pd.read_csv(filename)
    return player_data

def read_grandSlams(player_name):
    filename = f"data/era2/grandSlams/{player_name}.csv"
    player_data = pd.read_csv(filename, names=['Year', 'Australian_Open', 'French_Open', 'Wimbledon', 'US_Open', 'Total'])
    return player_data

def read_head_to_head(player1, player2):
    p1, p2 = sorted([player1, player2])
    filename = f"data/era2/headToHead/{p1}{p2}.csv"
    head_to_head_data = pd.read_csv(filename, index_col='Surface')
    return head_to_head_data

app.layout = html.Div([

    html.H1("Tennis Trivia", style={'textAlign': 'center'}),

    # Navigation
    html.Div([
        html.Button('Era 1', id='era1-button', n_clicks=0, style={'margin-right': '10px'}),
        html.Button('Era 2', id='era2-button', n_clicks=0, style={'margin-right': '10px'}),
        html.Button('Era 3', id='era3-button', n_clicks=0, style={'margin-right': '10px'}),
        html.Button('Recent News', id='news-button', n_clicks=0)
    ], style={'margin-bottom': '20px'}),


    # Display
    html.Div(id='page-content-era2', children=[
        html.Div([

            #surfaceRecords
            html.Div([
                html.Div(id='player-selector', children=[
                    dcc.Dropdown(
                        id='player-dropdown-surfaceRecords',
                        options=player_options,
                        value='Agassi'
                    )
                ], style={'width': '20%'}),

                html.Div(id='surface-stats', style={'display': 'flex', 'flexDirection': 'row'})
            ], style={'width': '50%'}),

            #headToHead
            html.Div([
                html.Div(id='player-selectors', children=[
                    html.Div(id='player1-selector', children=[
                        dcc.Dropdown(
                            id='player1-dropdown',
                            options=player_options,
                            value='Agassi'
                        )
                    ], style={'width': '20%', 'padding-right': '20px'}),

                    html.Div(id='player2-selector', children=[
                        dcc.Dropdown(
                            id='player2-dropdown',
                            options=player_options,
                            value='Sampras'
                        )
                    ], style={'width': '20%', 'padding-left': '20px'}),
                ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center'}),


                html.Div([
                    html.Div(id='player1-image', style={'display': 'inline-block', 'margin-top': '20px', 'padding-right': '10px', 'margin-bottom': '20px'}),
                    html.Div(id='player2-image', style={'display': 'inline-block', 'margin-top': '20px', 'padding-left': '10px', 'margin-bottom': '20px'})
                ], style={'display': 'flex', 'flex-direction': 'horizontal', 'justify-content': 'center'}),


                html.Div(id='head-to-head-table', style={'justify-content': 'center', 'text-align': 'center'})
            ], style={'width': '50%', 'justify-content': 'center', 'align-items': 'center'})
        ], style={'width': '100%', 'display': 'flex', 'flex-direction': 'row'}),


        # grandSlams
        html.Div([  
            html.Div([
                html.Div(id='selectors', children=[
                    dcc.Dropdown(
                        id='tournament-dropdown',
                        options=tournament_options,
                        value=tournaments,
                        multi=True
                    ),
                    dcc.Dropdown(
                        id='player-dropdown-grandSlams',
                        options=player_options,
                        value=players,
                        multi=True
                    )
                ]),
            ], style={'width': '40%'}),

            html.Div(id='line-chart', style={'width': '50%', 'height': '50%'})

            

        ]),
        

        html.Div(id='page-content-era1'),
        html.Div(id='page-content-era3'),
        html.Div(id='page-content-news')

        

    ], className='dark-theme')
])

#era1
@app.callback(
    Output('page-content-era1', 'children'),
    Input('era1-button', 'n_clicks')
)
def display_era1_layout(n_clicks):
    return era1.app.layout if n_clicks > 0 else dash.no_update

#era3
@app.callback(
    Output('page-content-era3', 'children'),
    Input('era3-button', 'n_clicks')
)
def display_era3_layout(n_clicks):
    return era3.app.layout if n_clicks > 0 else dash.no_update

#news
@app.callback(
    Output('page-content-news', 'children'),
    Input('news-button', 'n_clicks')
)
def display_news_layout(n_clicks):
    return news.app.layout if n_clicks > 0 else dash.no_update



# Backend..

@app.callback(
    Output('surface-stats', 'children'),
    Output('line-chart', 'children'),
    Output('head-to-head-table', 'children'),
    Output('player1-image', 'children'),
    Output('player2-image', 'children'),
    [Input('player-dropdown-surfaceRecords', 'value'),
     Input('player-dropdown-grandSlams', 'value'),
     Input('tournament-dropdown', 'value'),
     Input('player1-dropdown', 'value'),
     Input('player2-dropdown', 'value')]
)
def update(selected_player_sr, selected_players_gs, selected_tournaments, player1, player2):
    surface_stats = update_surface_stats(selected_player_sr)
    line_chart = update_line_chart(selected_players_gs, selected_tournaments)
    h2h_table = update_head_to_head_table(player1, player2)
    player1_img, player2_img = update_player_images(player1, player2)

    return surface_stats, line_chart, h2h_table, player1_img, player2_img

def update_surface_stats(selected_player):
    player_data = read_surfaceRecords(selected_player)

    surface_colors = {'Grass': 'green', 'Clay': 'orange', 'Hard': 'blue'}

    surface_donuts = []
    for surface in surfaces:
        wins = player_data[player_data['Surface'] == surface]['Win'].iloc[0]
        losses = player_data[player_data['Surface'] == surface]['Loss'].iloc[0]

        surface_donut = go.Figure(go.Pie(
            labels=['Wins', 'Losses'],
            values=[wins, losses],
            hole=0.5,
            marker=dict(colors=[surface_colors[surface], 'grey']),
            name=surface,
            showlegend=False
        ))
        surface_donut.update_layout(title_text=surface, title_x=0.5, title_y=0.5, margin=dict(t=0, b=0, l=40, r=40), height=300, width=250)
        surface_donuts.append(html.Div(dcc.Graph(figure=surface_donut), style={'width': '33%'}))

    return surface_donuts

def update_line_chart(selected_players, selected_tournaments):
    data = []
    for player in selected_players:
        player_data = read_grandSlams(player)

        total_wins = player_data[selected_tournaments].apply(pd.to_numeric, errors='coerce').sum(axis=1).astype(int)

        trace = go.Scatter(
            x=player_data['Year'],
            y=total_wins,
            mode='lines+markers',
            name=f"{player}",
            line=dict(width=2)
        )
        data.append(trace)

    layout = go.Layout(
        title='Grand Slams Won by Players Over the Years',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Total Tournaments Won'),
        hovermode='closest',
        legend=dict(orientation='h')
    )

    line_chart = dcc.Graph(
        id='line-chart-graph',
        figure={'data': data, 'layout': layout}
    )

    return line_chart

def update_head_to_head_table(player1, player2):
    if player1 == player2:
        return html.Div("Please select different players.", style={'text-align': 'center', 'margin-top': '20px'})
    head_to_head_data = read_head_to_head(player1, player2)

    table_style = {
        'width': '60%',
        'border-collapse': 'collapse',
        'margin': 'auto',
        'text-align': 'center',
        'font-size': '16px'
    }
    header_style = {
        'background-color': '#f2f2f2',
        'border': '1px solid #ddd',
        'padding': '8px'
    }
    cell_style = {
        'border': '1px solid #ddd',
        'padding': '8px'
    }

    table_content = [html.Tr([html.Th(player1, style=header_style), html.Th('Surface', style=header_style), html.Th(player2, style=header_style)])]

    for attribute, values in head_to_head_data.iterrows():
        table_content.append(html.Tr([html.Td(values[player1], style=cell_style), html.Td(attribute, style=cell_style), html.Td(values[player2], style=cell_style)]))

    head_to_head_table = html.Table(table_content, style=table_style, className='head-to-head-table')

    return head_to_head_table

def update_player_images(player1, player2):
    if player1 and player2:
        player1_image = html.Img(src=read_image(f"data/era2/pictures/{player1}.png"), style={'width': '100px', 'height': '100px'})
        player2_image = html.Img(src=read_image(f"data/era2/pictures/{player2}.png"), style={'width': '100px', 'height': '100px'})
        return player1_image, player2_image
    else:
        return None, None

if __name__ == '__main__':
    app.run_server(debug=True)
