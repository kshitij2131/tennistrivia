import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import base64


dash.register_page(__name__, path='/era2', name="ERA 2")

surfaces = ['Grass', 'Clay', 'Hard']
tournaments = ['Australian_Open', 'French_Open', 'Wimbledon', 'US_Open']
players = ['Agassi', 'Becker', 'Edberg', 'Sampras']
frm = 1985
to = 2003

player_full_names = {
    'Edberg': 'Stefan Edberg',
    'Wilander': 'Mats Wilander',
    'Becker': 'Boris Becker',
    'Lendl': 'Ivan Lendl',
    'Cash': 'Pat Cash',
    'Gomez': 'Andres Gomez',
    'Sampras': 'Pete Sampras',
    'Chang': 'Michael Chang',
    'Courier': 'Jim Courier',
    'Stich': 'Michael Stich',
    'Agassi': 'Andre Agassi',
    'Bruguera': 'Sergi Bruguera',
    'Muster': 'Thomas Muster',
    'Kafelnikov': 'Yevgeny Kafelnikov',
    'Kuerten': 'Gustavo Kuerten',
    'Rafter': 'Patrick Rafter',
    'Korda': 'Petr Korda',
    'Moya': 'Carlos Moya',
    'Safin': 'Marat Safin',
    'Ivanisevic': 'Goran Ivanisevic',
    'Hewitt': 'Lleyton Hewitt',
    'Johansson': 'Thomas Johansson',
    'Costa': 'Albert Costa',
    'Ferrero': 'Juan Carlos Ferrero',
    'Roddick': 'Andy Roddick'
}

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

#Loading the data..

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

def read_serve_stats():
    filename = f"data/era2/serve/serveStats.csv"
    serve_stats = pd.read_csv(filename)
    return serve_stats

def read_gs_wins():
    filename = f"data/era2/yearwiseSlamWinners/yearwiseSlamWinners.csv"
    serve_stats = pd.read_csv(filename)
    return serve_stats

#frontend..

layout = html.Div([

    html.H1("ERA 2 (1985-2003)", className="era-h1", style={'textAlign': 'center'}),

    html.Div(id='page-content', children=[
        html.Div([

            #surfaceRecords
            html.Div([
                html.H3("Surface Records", className="era-h3", style={'textAlign': 'center'}),
                html.Div(id='player-selector', className = "dropdown", children=[
                    dcc.Dropdown(
                        id='player-dropdown-surfaceRecords-era2',
                        options=player_options,
                        value='Agassi',
                        clearable=False,
                    )
                ], style={'width': '40%'}),

                html.Div(id='surface-stats-era2', style={'display': 'flex', 'flexDirection': 'row'})
            ], style={'width': '33%'}),

            #headToHead
            html.Div([
                html.H3("Head to Head", className="era-h3", style={'textAlign': 'center'}),
                html.Div(id='player-selectors',className = "dropdown", children=[
                    html.Div(id='player1-selector', children=[
                        dcc.Dropdown(
                            id='player1-dropdown-era2',
                            options=player_options,
                            value='Agassi',
                            clearable=False,
                        )
                    ], style={'width': '20%', 'padding-right': '20px'}),

                    html.Div(id='player2-selector', children=[
                        dcc.Dropdown(
                            id='player2-dropdown-era2',
                            options=player_options,
                            value='Sampras',
                            clearable=False,
                        )
                    ], style={'width': '20%', 'padding-left': '20px'}),
                ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center'}),


                html.Div([
                    html.Div(id='player1-image-era2', style={'display': 'inline-block', 'margin-top': '20px', 'padding-right': '10px', 'margin-bottom': '20px'}),
                     html.P("vs", style={'justify-content': 'center', 'align-items': 'center', 'display': 'flex', 'flex-direction': 'row', 'font-family': '"Monaco", "Courier New", monospace', 'font-weight': 'bold'}),
                    html.Div(id='player2-image-era2', style={'display': 'inline-block', 'margin-top': '20px', 'padding-left': '10px', 'margin-bottom': '20px'})
                ], style={'display': 'flex', 'flex-direction': 'horizontal', 'justify-content': 'center'}),


                html.Div(id='head-to-head-table-era2', style={'justify-content': 'center', 'text-align': 'center'})
            ], style={'width': '33%', 'justify-content': 'center', 'align-items': 'center'}),

            #serveStats
            html.Div([
                html.H3("Serve Stats", className="era-h3", style={'textAlign': 'center'}),
                html.Div(id = 'stat-selector', className='dropdown', children = [
                    dcc.Dropdown(
                    id='stat-dropdown-era2',
                        options=[
                            {'label': 'Aces', 'value': 'Aces'},
                            {'label': 'Double Faults', 'value': 'Double Faults'},
                            {'label': 'First Serve Percentage', 'value': 'First Serve Percentage'}
                        ],
                        value='Aces',
                        clearable=False,
                    ),
                ], style = {'width':'40%'}),
                
                html.Br(),
                html.Div(id='bar-container-era2')
            ], style = {'width':'33%'}),

        ], style={'width': '100%', 'height':'400px','display': 'flex', 'flex-direction': 'row'}),


        html.Div([

            # grandSlams
            html.Div([  
                html.H3("Grand Slams Timeline", className="era-h3", style={'textAlign': 'center'}),
                html.Div([
                    html.Div(id='selectors', className = "dropdown" ,children=[
                        dcc.Dropdown(
                            id='tournament-dropdown-era2',
                            options=tournament_options,
                            value=tournaments,
                            multi=True,
                            clearable=False,
                        ),
                        dcc.Dropdown(
                            id='player-dropdown-grandSlams-era2',
                            options=player_options,
                            value=players,
                            multi=True,
                            clearable=False,
                        )
                    ]),
                ], style={'width': '70%'}),

                html.Div(id='line-chart-era2')
            ], style = {'width': '50%'}),

            # Grand Slam Winners Yearwise.. 
            html.Div([
                html.H3("Grand Slam Winners", className="era-h3", style={'textAlign': 'center', 'margin-top': '200px'}),
                html.Div(id='slam-winners-info'),
                html.Div(id='gs-year-selector', children=[
                    dcc.Slider(
                        id='year-slider-era2',
                        min=frm,
                        max=to,
                        value=frm,
                        marks={year: str(year) for year in range(frm, to+1)},
                        step=None,
                        
                    )
                ], style={'width': '100%'})
            ], style={'width': '50%'})

        ], style={'width': '100%', 'display': 'flex', 'flex-direction': 'row', 'height':'400px'})

    ], )
])




#Callbacks..

@callback(
    Output('surface-stats-era2', 'children'),
    Output('line-chart-era2', 'children'),
    Output('head-to-head-table-era2', 'children'),
    Output('player1-image-era2', 'children'),
    Output('player2-image-era2', 'children'),
    Output('bar-container-era2', 'children'),
    Output('slam-winners-info', 'children'),
    [Input('player-dropdown-surfaceRecords-era2', 'value'),
     Input('player-dropdown-grandSlams-era2', 'value'),
     Input('tournament-dropdown-era2', 'value'),
     Input('player1-dropdown-era2', 'value'),
     Input('player2-dropdown-era2', 'value'),
     Input('stat-dropdown-era2', 'value'),
     Input('year-slider-era2', 'value')]
)

#Backend..

def update(selected_player_sr, selected_players_gs, selected_tournaments, player1, player2, stat_dropdown, selected_year):
    surface_stats = update_surface_stats(selected_player_sr)
    line_chart = update_line_chart(selected_players_gs, selected_tournaments)
    h2h_table = update_head_to_head_table(player1, player2)
    player1_img, player2_img = update_player_images(player1, player2)
    serve_bar = update_serve_bar(stat_dropdown)
    gs_winners = update_winners_info(selected_year)

    return surface_stats, line_chart, h2h_table, player1_img, player2_img, serve_bar, gs_winners

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
        font=dict(
            size=16,
            family = '"Monaco", "Courier New", monospace'
        ),  
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
        return html.Div("Please select different players.", style={'text-align': 'center', 'margin-top': '20px',
                                                                    'font-family': '"Monaco", "Courier New", monospace'})
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
        player1_image = html.Img(src=read_image(f"data/era2/pictures/{player1}.png"), style={'width': '150px', 'height': '150px'})
        player2_image = html.Img(src=read_image(f"data/era2/pictures/{player2}.png"), style={'width': '150px', 'height': '150px'})
        return player1_image, player2_image
    else:
        return None, None

def update_serve_bar(selected_stat):
    df = read_serve_stats()
    sorted_df = df.sort_values(by=selected_stat, ascending=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=sorted_df[selected_stat],
        y=sorted_df['Player'],
        orientation='h',
        marker=dict(color='#eb3434')
    ))
    fig.update_layout(
        title=f'{selected_stat} by Player',
        xaxis_title=selected_stat,
        yaxis_title='Player',
        font=dict(
            size=16,
            family = '"Monaco", "Courier New", monospace'
            ),  
        plot_bgcolor='#ffffff', 
        paper_bgcolor='#ffffff', 
    )

    return html.Div(dcc.Graph(figure=fig))

def update_winners_info(selected_year):
    slam_winners_df = read_gs_wins()
    year_data = slam_winners_df[slam_winners_df['Year'] == selected_year]

    winners_info = []

    for _, row in year_data.iterrows():
        tournament = row[['Australian Open', 'French Open', 'Wimbledon', 'US Open']]
        grand_slams = ['Australian Open', 'Roland Garros', 'Wimbledon', 'US Open']
        for winner, grand_slam in zip(tournament, grand_slams):
            if winner and not pd.isna(winner):
                winner_name = player_full_names.get(winner, winner)
                winner_image = html.Img(src=read_image(f"data/era2/pictures/{winner}.png"), style={'width': '150px', 'height': '150px'})
                winners_info.append(html.Div([
                                            html.H3(f"{grand_slam}", style = {'font-family': '"Monaco", "Courier New", monospace', 'text-align':'center'}), 
                                            winner_image, 
                                            html.H3(f"{winner_name}", style = {'font-family': '"Monaco", "Courier New", monospace'})
                                            ], style= {'width':'25%', 'display':'flex', 'flex-direction':'column','justify-content': 'center', 'align-items': 'center'}))
            else:
                winners_info.append(html.Div([html.H3(f"{grand_slam} Grand Slam did not happen😞")],
                                            style = {'font-family': '"Monaco", "Courier New", monospace'}))

    return html.Div(winners_info, style={'width': '100%', 'display': 'flex', 'flex-direction': 'row','margin-top':'200px', 'margin-top':'0'})