from dash import Dash, html, dcc
import dash

external_css = ["./styles.css" ]

app = Dash(__name__, pages_folder='pages', use_pages=True)

app.layout = html.Div([
	html.H1("Tennis Trivia",className="main-heading", style={'textAlign': 'center'}),
    html.Div(children=[
	    dcc.Link(page['name'], href=page["relative_path"], className="era-button")\
			  for page in dash.page_registry.values()], style={'display':'flex', 'flex-direction':'row'}
	),
	dash.page_container
], className="col-8 mx-auto main-div", style={'padding': '20px'})

if __name__ == '__main__':
	app.run(debug=True)