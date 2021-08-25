import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_core_components.Dropdown import Dropdown
import dash_html_components as html
import pandas as pd
import plotly.express as px 
import pyrebase
from django_plotly_dash import DjangoDash
from django.contrib.staticfiles.storage import staticfiles_storage

app = DjangoDash('testdash')   # replaces dash.Dash
config = {
    "apiKey": "AIzaSyDJM6U2PhmhURsYaBOFZ-mWJO4rn5GhKL8",
    "authDomain": "highagriv6.firebaseapp.com",
    "databaseURL": "https://highagriv6-default-rtdb.firebaseio.com",
    "projectId": "highagriv6",
    "storageBucket": "highagriv6.appspot.com",
    "messagingSenderId": "902180705852",
    "appId": "1:902180705852:web:893176f34cffa29909d539"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
bb = database.child("").get().val()
pd.DataFrame(database.child("").get().val())

app.layout = html.Div([ 
 
    
    
    html.Div([
        html.Div([dcc.Dropdown(
            id = 'indexes',
            options = [
                {'label':'nitrogen', 'value': 'N'},
                {'label':'Phosphore', 'value': 'P'},
                {'label':'Potasse', 'value': 'K'},
                {'label':'Temperature', 'value': 'temperature'},
                {'label':'Soil Humidity', 'value': 'humidity'},
                {'label':'PH', 'value': 'ph'}
                
            ],
            placeholder="Select an index",
            style={'height': '60px','width': '900px','left': '180px','top': '365px'
}
)],style={'height': '60px','width': '900px','left': '180px','top': '365px'
}),
        dcc.Interval(
            id='interval-component',
            interval=1000, # in milliseconds
        ),
        html.Div([], id = 'graphs')
]),
], style={'position': 'absolute',
'width': '1440px',
'height': '401px',
'left': '0px',
'top':'0px',

'background': 'linear-gradient(91.19deg, #33A261 13.2%, #64C486 96.27%)'})
    
    

@app.callback(
    dash.dependencies.Output('graphs', 'children'),
    [dash.dependencies.Input('indexes', 'value'),
    dash.dependencies.Input('interval-component', 'n_intervals')],
    dash.dependencies.State('indexes','value'))

def update_graph(value, c1, c2):
    if value == 'N':
        return dcc.Graph(figure = px.line(pd.DataFrame(database.child("").get().val()), x='time', y='N'))
    if value == 'P':
        return dcc.Graph(figure =px.line(pd.DataFrame(database.child("").get().val()), x='time', y='P'))
    if value == 'K':
        return  dcc.Graph(figure =px.line(pd.DataFrame(database.child("").get().val()), x='time', y='K'))
    if value == 'temperature':
        return dcc.Graph(figure =px.line(pd.DataFrame(database.child("").get().val()), x='time', y='temperature'))
    if value == 'humidity':
        return dcc.Graph(figure =px.line(pd.DataFrame(database.child("").get().val()), x='time', y='humidity'))
    if value == 'ph':
        return dcc.Graph(figure =px.line(pd.DataFrame(database.child("").get().val()), x='time', y='ph'))
    
    
    
    
    
    
    
    
    
    
    import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_core_components.Dropdown import Dropdown
import dash_html_components as html
import pandas as pd
import plotly.express as px 
import pyrebase
from django_plotly_dash import DjangoDash
from django.contrib.staticfiles.storage import staticfiles_storage
import plotly.graph_objects as go

app = DjangoDash('testdash')   # replaces dash.Dash

config = {
    "apiKey": "AIzaSyDJM6U2PhmhURsYaBOFZ-mWJO4rn5GhKL8",
    "authDomain": "highagriv6.firebaseapp.com",
    "databaseURL": "https://highagriv6-default-rtdb.firebaseio.com",
    "projectId": "highagriv6",
    "storageBucket": "highagriv6.appspot.com",
    "messagingSenderId": "902180705852",
    "appId": "1:902180705852:web:893176f34cffa29909d539"}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

app.layout = html.Div([ 
 

    html.Div([
        html.Div([dcc.Dropdown(
            id = 'indexes',
            options = [
                {'label':'nitrogen', 'value': 'nitrogen_value'},
                {'label':'Phosphore', 'value': 'phosphorous_value'},
                {'label':'Potassium', 'value': 'potassium_value'},
                {'label':'Temperature', 'value': 'air_temperature'},
                {'label':'Humidité', 'value': 'air_humidity'},
                {'label':'Humidité de sol ', 'value': 'soil_moisture'},
                {'label':'PH', 'value': 'soil_ph'}
                
            ],
            placeholder="Select an index"
)]),
        #html.Button('nitrogen', id = 'nitrogen_value'),
        #html.Button('Phosphore', id =  'phosphorous_value'),
        #html.Button('Potassium', id =  'potassium_value'),
        #html.Button('Temperature', id =  'air_temperature'),
        #html.Button('Humidity', id = 'air_humidity'),
        #html.Button('Soil Moisture', id =  'soil_moisture'),
        #html.Button('PH', id = 'soil_ph')
        dcc.Interval(
            id='interval-component',
            interval=5000, # in milliseconds
        ),
        html.Div([], id = 'graphs')
])
])
@app.callback(
    dash.dependencies.Output('graphs', 'children'),
    [dash.dependencies.Input('indexes', 'value'),

    dash.dependencies.Input('interval-component', 'n_intervals')],
    dash.dependencies.State('indexes','value'))

def update_graph(value, c1, c2):
    if value == 'nitrogen_value':
        return dcc.Graph(figure = go.Figure(go.Scatter(x=list(dict(database.child("timer").get().val()).values())[-20:], 
                    y=list(dict(database.child("nitrogen_value").get().val()).values())[-20:],
                    mode='lines',
                    line=dict(width=2.5, color='blueviolet'),
                    stackgroup = 'one'))
)
    if value == 'phosphorous_value':
        return dcc.Graph(figure =go.Figure(go.Scatter(x=list(dict(database.child("timer").get().val()).values())[-20:], 
                    y=list(dict(database.child("phosphorous_value").get().val()).values())[-20:],
                    mode='lines',
                    line=dict(width=2.5, color='red'),
                    stackgroup = 'one')))
    if value == 'potassium_value':
        return  dcc.Graph(figure =go.Figure(go.Scatter(x=list(dict(database.child("timer").get().val()).values())[-20:], 
                    y=list(dict(database.child("potassium_value").get().val()).values())[-20:],
                    mode='lines',
                    line=dict(width=2.5, color='indianred'),
                    stackgroup = 'one')))

    if value == 'soil_ph':
        return dcc.Graph(figure =go.Figure(go.Scatter(x=list(dict(database.child("timer").get().val()).values())[-20:], 
                    y=list(dict(database.child("soil_ph").get().val()).values())[-20:],
                    mode='lines',
                    line=dict(width=2.5, color='olive'),
                    stackgroup = 'one')))
    if value == 'soil_moisture':
        return dcc.Graph(figure =go.Figure(go.Scatter(x=list(dict(database.child("timer").get().val()).values())[-20:], 
                    y=list(dict(database.child("soil_moisture").get().val()).values())[-20:],
                    mode='lines',
                    line=dict(width=2, color=' goldenrod'),
                    stackgroup = 'one')))
    if value == 'air_humidity':
        return dcc.Graph(figure =go.Figure(go.Scatter(x=list(dict(database.child("timer").get().val()).values())[-20:], 
                    y=list(dict(database.child("air_humidity").get().val()).values())[-20:],
                    mode='lines',
                    line=dict(width=2, color='cadetblue'),
                    stackgroup = 'one')))
    if value == 'air_temperature':
        return dcc.Graph(figure =go.Figure(go.Scatter(x=list(dict(database.child("timer").get().val()).values())[-20:], 
                    y=list(dict(database.child("air_temperature").get().val()).values())[-20:],
                    mode='lines',
                    line=dict(width=2, color='gold'),
                    stackgroup = 'one')))





    
