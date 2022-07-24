######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices1=['punch', 'body-slam', 'round-house kick to the face']
list_of_choices2=['Yes-absolutely!', 'No-dont be ridiculous!']
##githublink = 'https://github.com/austinlasseter/chuck_norris_execution'
githublink = 'https://github.com/sudha-akula/201-chuck-norris-callback'
image1='chucknorris.jpg'
heading1='Chuck Norris execution method'

image2='Lily_has_a_twin.jpg'
heading2='Does Lily have a twin? You tell me..'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Chuck'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(src=app.get_asset_url(image1), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i, 'value': i} for i in list_of_choices1],
                value='punch',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    
    html.H2(heading2),
    html.Img(src=app.get_asset_url(image2), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here2',
                options=[{'label': i, 'value2': i} for i in list_of_choices2],
                value='Yes-absolutely!',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here2', children=''),
    
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'Chuck Norris will now execute you with a {whatever_you_chose}.'

@app.callback(dash.dependencies.Output('your-output-here2', 'children'),
              [dash.dependencies.Input('your-input-here2', 'value')])
def display_value(whatever_you_chose2):
    return f'Does Lily have a twin? {whatever_you_chose2}.'

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
