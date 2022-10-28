import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


dfEvaluations = pd.read_excel("assets/evaluations.xlsx")
dfEnseignements = pd.read_excel("assets/enseignements.xlsx")

app = dash.Dash(external_stylesheets=[dbc.themes.MATERIA], suppress_callback_exceptions=True)

#---------------------------------------ENTETE-----------------------------------------------------------
entete = html.Div([
    dbc.Row([
        dbc.Col([
            html.H5("ENSAE Dakar / ISE3-2023")
        ], style={'color':'aliceblue'})
    ], style={'margin':'20px 0px 5px 0px'}),
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Accueil", active="exact", href="/accueil")),
                dbc.NavItem(dbc.NavLink("Evaluations", active="exact", href="/evaluations")),
                dbc.NavItem(dbc.NavLink("Enseignements", active="exact", href="/enseignements")),
                dbc.NavItem(dbc.NavLink("A Propos", active="exact", href="/apropos")),
            ], pills=True, fill=True, style={'float': 'right', 'color': 'goshwhite'})
        ])
    ])
], style={
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'right': 0,
    'height': '100px',
    'background': 'black',
    'font-family': 'serif'
})

#---------------------------------------ACCUEIL-----------------------------------------------------------
accueil = html.Div([
    dbc.Row([
        dbc.Col([
            html.H3("Planning des tâches à réaliser et suivi des enseignements.")
        ], style={'text-align': 'center'})
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Travaux à rendre"),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([html.H5("Econométrie des données de panel")],
                                       style={'background': 'RoyalBlue', 'color': 'GhostWhite'}),
                        dbc.CardBody([html.P("Préparer une présentataion sur le modèle linéaire :"
                                             "ses hypothèses, les tests de validations et les "
                                             "types de modèle.")]),
                        dbc.CardFooter([html.H6("Date limite : 29/10/2022")],
                                       style={'background': 'RoyalBlue', 'color': 'GhostWhite'})
                    ])
                ]),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([html.H5("Traitement des données")],
                                       style={'background': 'RoyalBlue', 'color': 'GhostWhite'}),
                        dbc.CardBody([html.P("Détection et traitement des outliers avec R, Python et Stata."
                                             " Travail individuel à préparer avant la fin du module")]),
                        dbc.CardFooter([html.H6("Date limite : Non précisée")],
                                       style={'background': 'RoyalBlue', 'color': 'GhostWhite'})
                    ])
                ]),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([html.H5("Evaluation d'impact ")],
                                       style={'background': 'RoyalBlue', 'color': 'GhostWhite'}),
                        dbc.CardBody([html.P("Compléter le dofile débuté en classe sur Empirical Exercise 8"
                                             " le jeudi 27/10/2022 et envoyer au professeur.")]),
                        dbc.CardFooter([html.H6("Date limite : 30/10/2022")],
                                       style={'background': 'RoyalBlue', 'color': 'GhostWhite'})
                    ])
                ])
            ])
        ])
    ], style={'margin-top': '10px'}),
    dbc.Row([
        dbc.Col([
            html.H4("Emploi du temps de la semaine du  : 24 au 29 Octobre 2022"),
            html.Hr(),
            html.Img(src="assets/emp2428oct22.PNG")
        ])
    ], style={'margin-top': '50px'})
], style={'font-family': 'serif'})

#---------------------------------------EVALUATIONS-----------------------------------------------------------
evaluations = html.Div([
    dbc.Row([
        dbc.Col([
            html.H3("Planning des évaluations."),
            html.Hr(),
            dbc.Card([
                dbc.CardHeader([html.H5("Date des évaluations prévues")],
                               style={'background': '#4169E1', 'color': 'white'}),
                dbc.CardBody([
                    html.Div([
                        dash_table.DataTable(data=dfEvaluations.to_dict("records"),
                                             columns=[{'name': i, 'id': i} for i in dfEvaluations.columns],
                                             fixed_rows={'headers': True}, fixed_columns={'headers': True, 'data': 1},
                                             style_cell={'textAlign': 'left', 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',},
                                             style_data={'color': 'black', 'backgroundColor': 'white', 'font-family': 'calibri'},
                                             style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#F8F8FF'}],
                                             style_header={'backgroundColor': '#4169E1', 'color': 'white', 'fontWeight': 'bold', 'font-family': 'calibri'},
                                             style_table={'height': '180px', 'minWidth': '100%', 'overflowY': 'auto','overflowX': 'auto'})
                    ])
                ])
            ])

        ], style={'text-align': 'center'})
    ])
])

#---------------------------------------ENSEIGNEMENTS-----------------------------------------------------------
enseignements = html.Div([
    dbc.Row([
        dbc.Col([
            html.H3("Suivi des enseignements"),
            html.Hr(),
            dbc.Card([
                dbc.CardHeader([html.H5("Suivi des heures réalisées par enseignement")],
                               style={'background': '#4169E1', 'color': 'white'}),
                dbc.CardBody([
                    html.Div([
                        dash_table.DataTable(data=dfEnseignements.to_dict("records"),
                                             columns=[{'name': i, 'id': i} for i in dfEnseignements.columns],
                                             fixed_rows={'headers': True}, fixed_columns={'headers': True, 'data': 1},
                                             style_cell={'textAlign': 'left', 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',},
                                             style_data={'color': 'black', 'backgroundColor': 'white', 'font-family': 'calibri'},
                                             style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#F8F8FF'}],
                                             style_header={'backgroundColor': '#4169E1', 'color': 'white', 'fontWeight': 'bold', 'font-family': 'calibri'},
                                             style_table={'height': '300px', 'minWidth': '100%', 'overflowY': 'auto','overflowX': 'auto'})
                    ])
                ])
            ])

        ], style={'text-align': 'center'})
    ])
])

#---------------------------------------A PROPOS-----------------------------------------------------------
apropos = html.Div([
    dbc.Row([
        dbc.Col([
            html.H3("La plateforme ENSAE Dakar / ISE3-2023"),
            html.Hr(),
            html.P("Elle conçu pour le suivi des enseignements et faciliter les rappels des tâches à "
                   "réaliser. Elle s'adresse principalement aux étudiants de la promo ISE 2020-2023 "
                   "mais reste accessible à toute personne disposant du lien.")
        ], style={'text-align': 'justify'})
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Concepteur / Administrateur"),
            html.Hr(),
            html.H6("Assana Richard AYIZOU"),
            html.P("Ingénieur Statisticien Economiste en fin de formation à l'ENSAE de Dakar"),
            html.P("2022-2023 : Master Aide à la Décision et Evaluation d'impact des Politiques Publiques"),
            html.P("2021-2022 : Ingénieur Statisticien Economiste / ENSAE de Dakar"),
            html.P("2017-2021 : Ingénieur des Travaux Statistiques / ENSAE de Dakar")
        ], style={'text-align': 'justify'})
    ], style={'margin-top': '20px'})
])

#---------------------------------------PIED DE PAGE-----------------------------------------------------------
piedpage = html.Div([
    dbc.Row([
        dbc.Col([
            html.H3("La plateforme ENSAE Dakar / ISE3-2023"),
            html.Hr(),
            html.P("Elle conçu pour le suivi des enseignements et faciliter les rappels des tâches à "
                   "réaliser. Elle s'adresse principalement aux étudiants de la promo ISE 2020-2023 "
                   "mais reste accessible à toute personne disposant du lien.")
        ], style={'text-align': 'justify'})
    ]),
], style={
    'width': '100%',
    'height': '230px',
    'background': 'Gray',
    'font-family': 'serif',
    'margin-top': '15px'
})
#---------------------------------------CONTAINER-----------------------------------------------------------
container = html.Div(
    id="container",
    children=accueil,
    style={'margin-top': '120px', 'padding': '0px 30px'})
#-------------------------------------LAYOUT--------------------------------------------------------------
app.layout = html.Div(children=[
    dcc.Location(id="url"),
    container,
    entete

])

#---------------------------------------------------- CHARGEMENT DES PAGES ---------------------------------------------------------
@app.callback(
    Output('container', 'children'),
    Input('url', 'pathname')
)
def load_page(lien):
    if lien=='/':
        return accueil
    elif lien=='/accueil':
        return accueil
    elif lien=='/evaluations':
        return evaluations
    elif lien=='/enseignements':
        return enseignements
    elif lien=='/apropos':
        return apropos
    return "Error 404 : Page not found !"

#-----------------------------------------------run app---------------------------------------------------
app.title="ISE3-2023"
app.run_server(debug=True)