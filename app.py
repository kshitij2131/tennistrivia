from dash import Dash, html, dcc
import dash

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=external_css)

app.layout = html.Div([
	html.H1("Tennis Trivia", style={'textAlign': 'center'}),
    html.Div(children=[
	    dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5")\
			  for page in dash.page_registry.values()]
	),
	dash.page_container
], className="col-8 mx-auto")

if __name__ == '__main__':
	app.run(debug=True)