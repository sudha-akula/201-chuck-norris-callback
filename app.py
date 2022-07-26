######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices2=['Yes-absolutely!', 'No-dont be ridiculous!']
list_of_cats=['FlamePoint','Calico','Tortie','Tuxedo','Tabby','OrangeTabby','TigerTabby']
list_of_cat_images=['flamepoint_simba_resize.jpg','calico_sweetie_resize.jpg','tortie-iris-baby_resize.jpg', 
                    'tuxedo_chinni_resize.jpg','tabby_juno_resize.jpg','orange_tabby_haley_resize.jpg','tiger_remo_resize.jpg']
list_of_cat_names=['Flamepoint Simba!','Calico Sweetie!','Tortie Iris!','Tuxedo Cinni!', 'Tabby Juno!','Orange Tabby Haley!','Tiger Remo!']
##githublink = 'https://github.com/austinlasseter/chuck_norris_execution'
githublink = 'https://github.com/sudha-akula/201-chuck-norris-callback'

image2='Lily_has_a_twin_resize.jpg'
heading2='Does Lily have a twin? You tell me..'
heading3='Cats.. Cats.. My Cats!'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Cats'

####### Layout of the app ########
app.layout = html.Div([    
    html.H2(heading2),
    html.Img(src=app.get_asset_url(image2), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here2',
                options=[{'label': i, 'value': i} for i in list_of_choices2],
                value='Yes-absolutely!',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here2', children=''),
    
    html.H2(heading3),
    dcc.Dropdown(id='your-input-cat',
                options=[{'label': i, 'value': i} for i in list_of_cats],
                value='FlamePoint',
                style={'width': '500px'}),
    
    
    html.Br(),
    html.Div(id='cat-name', children=''),
    
    html.Br(),
    html.Img(id='cat-image',src=app.get_asset_url('flamepoint_simba_resize.jpg'), style={'width': 'auto', 'height': '10%'}),
    
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here2', 'children'),
              [dash.dependencies.Input('your-input-here2', 'value')])
def display_value(whatever_you_chose2):
    return f'Does Lily have a twin? {whatever_you_chose2}.'

@app.callback(dash.dependencies.Output('cat-name', 'children'),dash.dependencies.Output('cat-image','src'),
              [dash.dependencies.Input('your-input-cat', 'value')])

def display_value2(select_cat):
              
    return (f'Here is my {list_of_cat_names[list_of_cats.index(select_cat)]}',
            app.get_asset_url(list_of_cat_images[list_of_cats.index(select_cat)]))

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
