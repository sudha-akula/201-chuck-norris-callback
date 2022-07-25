######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices2=['Yes-absolutely!', 'No-dont be ridiculous!']
list_of_cats=['FalmePoint','Tuxedo'.'Calico','OrangeTabby',/'TigerTabby']
##githublink = 'https://github.com/austinlasseter/chuck_norris_execution'
githublink = 'https://github.com/sudha-akula/201-chuck-norris-callback'

image2='Lily_has_a_twin.jpg'
image3='calico_sweetie.jpg'
heading2='Does Lily have a twin? You tell me..'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Chuck'

####### Layout of the app ########
app.layout = html.Div([    
    html.H2(heading2),
    html.Img(src=app.get_asset_url(image3), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here2',
                options=[{'label': i, 'value': i} for i in list_of_choices2],
                value='Yes-absolutely!',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here2', children=''),
    
    
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here2', 'children'),
              [dash.dependencies.Input('your-input-here2', 'value')])
def display_value(whatever_you_chose2):
    return f'Does Lily have a twin? {whatever_you_chose2}.'

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
