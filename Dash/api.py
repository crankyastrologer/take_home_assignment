from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from components.Introduction import introduction, data_visualization, links
from components.correlation import correlation
from components.Training_Result import result
from components.Time_variation import time, dic3,dic2
from components.conclusion import concl
import plotly.graph_objs as go
from sklearn.preprocessing import MinMaxScaler
from views import dic
import dash_bootstrap_components as dbc
from utils import create_heatmap

df = pd.read_csv('processed.csv')

other_columns = ['gdp_growth', 'house_inventory', 'Diff_house_inventory',
                 'inflation', 'material_cost', 'mortgage_rate', 'population_growth',
                 'shares', 'Unemployment', 'vacancy_rate', 'Total', 'rent_price']
base_columns = ['house_price', 'house_price_diff']
app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.layout = [


    html.H1(children='Housing Price Prediction', style={'textAlign': 'center'}),
    html.H3('Introduction'),
    introduction,
    html.P('factors we are considering are:-'),
    links,

    html.Br(),
    data_visualization,
    dcc.Dropdown(other_columns, 'gdp_growth', id='dropdown-selection'),
    dcc.Graph(id='data-visualization'),
    html.P(id='info', children="hello world"),
html.Br(),
    html.H3('Correlation analysis'),
    correlation,
    dcc.Graph(id='correlation', figure=create_heatmap(df,other_columns+base_columns)),
html.Br(),
    result,
html.Br(),
    time,
    html.Div(id='iframe-container'),
html.Br(),
    html.H3('Conclusion'),
    concl

]


@callback(
    Output('data-visualization', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    columns_to_plot = base_columns + [value]
    scaler = MinMaxScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df[columns_to_plot]), columns=columns_to_plot)
    df_normalized['DATE'] = df['DATE']
    fig = go.Figure()
    for column in columns_to_plot:
        fig.add_trace(go.Scatter(x=df_normalized['DATE'], y=df_normalized[column], mode='lines', name=column))
    fig.update_layout(
        title="Normalized Time Series Plot",
        xaxis_title="Date",
        yaxis_title="Normalized Values",
        legend_title="Variables",
        height=600,
        width=900
    )

    return fig


@callback(
    Output('info', 'children'),
    Input('dropdown-selection', 'value')
)
def update_info(value):
    return dic[value]


@app.callback(
    Output('iframe-container', 'children'),
    [Input('dropdown-time', 'value')]
)
def update_iframes(selected_time_period):
    # Get the filenames based on the selected time period
    crossval_file = f'graphs/{dic2[selected_time_period]}_crossval.html'
    best_feature_file = f'graphs/{dic3[selected_time_period]}.html'

    # Read the content of the HTML files
    with open(crossval_file, 'r', encoding='utf-8') as file:
        crossval_content = file.read()
    with open(best_feature_file, 'r', encoding='utf-8') as file:
        best_feature_content = file.read()

    # Return the updated iframes
    return [
        html.Iframe(srcDoc=crossval_content, style={"width": "100%", "height": "600px", "border": "none"}),
        html.Iframe(srcDoc=best_feature_content, style={"width": "100%", "height": "600px", "border": "none"})
    ]

if __name__ == '__main__':
    app.run(debug=True)
