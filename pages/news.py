import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import pandas as pd
import requests


dash.register_page(__name__, path='/news', name="RECENT NEWS")


# api_key = "fad10f0941c470a19bf01b5f51419968"
#In case the above api doesn't work, please use
api_key = "87ae556dd203782a4fb6d957cd016698"

# Loading the data..
def fetch_tennis_news(start_date, end_date):
    gnews_url = f"https://gnews.io/api/v4/search?q=tennis&from={start_date}&to={end_date}&lang=en&token={api_key}"
    print(gnews_url)
    response = requests.get(gnews_url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        return articles
    else:
        return []


# Frontend layout
layout = html.Div([
    html.H1("Tennis News", className="era-h1", style={'textAlign': 'center'}),
    dcc.RangeSlider(
        id='date-slider',
        min=0,
        max=120, 
        step=1,
        value=[0, 30], 
        marks={i: f'{i} days ago' for i in range(0, 121, 10)},
    ),
    html.Div(id='news-container')
])

# Callback
@callback(
    Output('news-container', 'children'),
    [Input('date-slider', 'value')]
)

# Backend..

def update_news_articles(date_range):
    start_date = (pd.Timestamp.today() - pd.DateOffset(days=date_range[1]))
    end_date = pd.Timestamp.today() - pd.DateOffset(days=date_range[0])
    start_date = start_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_date = end_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    # print(start_date, end_date)
    
    articles = fetch_tennis_news(start_date, end_date)

    if articles:
        news_list = []
        for article in articles:
            title = article['title']
            description = article['description']
            content = article['content']
            source_name = article['source']['name']
            published_at = article['publishedAt']
            image_url = article.get('image', '')
            article_url = article['url']
            article_html = html.Div([
                html.H3(title, className="era-h1"),
                html.P([html.B(f"Source: {source_name} | Published At: {published_at}")], className='news-p'),
                html.Div(id='news-content',children =[
                    html.Img(src=image_url, className="news-image", style={'width': '50%', 'height': '300px', 'padding-right': '10px'}),
                    html.Div(id='news-text', children=[
                        html.P(html.B(description), className="news-p", style = {'width': '50%'}),
                        html.P(content, className="news-p", style = {'width': '50%'})
                    ])
                ], style = {'width': '70%', 'display': 'flex', 'flex-direction': 'row'}),
                html.A("Read more", href=article_url, target="_blank", className='news-button'),
                html.Hr()
            ]) 
            news_list.append(article_html)
        return news_list
    else:
        return html.P("No news articles found.")


