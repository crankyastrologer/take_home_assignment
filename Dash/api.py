from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from components.Introduction import introduction, data_visualization
import plotly.graph_objs as go
from sklearn.preprocessing import MinMaxScaler
from views import dic
from utils import create_heatmap

df = pd.read_csv('../processed.csv')
other_columns = ['gdp_growth', 'house_inventory', 'Diff_house_inventory',
                 'inflation', 'material_cost', 'mortgage_rate', 'population_growth',
                 'shares', 'Unemployment', 'vacancy_rate', 'Total', 'rent_price']
base_columns = ['house_price', 'house_price_diff']
app = Dash()

app.layout = [


    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    introduction,
    html.Br(),
    data_visualization,
    dcc.Dropdown(other_columns, 'gdp_growth', id='dropdown-selection'),
    dcc.Graph(id='data-visualization'),
    html.P(id='info', children="hello world"),
    dcc.Graph(id='correlation', figure=create_heatmap(df,other_columns+base_columns))
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


if __name__ == '__main__':
    app.run(debug=True)
