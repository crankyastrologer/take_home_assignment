from dash import html, dcc

dic3 = {
    "2003-2008": "best_0",
    "2009-2013": "best_1",
    "2014-2018": "best_2",
    "2019-2024": "best_3"
}
dic2 = {
    "2003-2008": "0",
    "2009-2013": "1",
    "2014-2018": "2",
    "2019-2024": "3"
}
i = '2003-2008'
other_columns = ['2003-2008', '2009-2013', '2014-2018', '2019-2024']
time = html.Div([
    html.H3('Changing variable importance with time'),
    html.P('Here we have trained the models on whole of the dataset but the variables affecting the '
           'house prices may change over time for eg in certain time house prices may be directed by mortgage but at other'
           'times it could be the house_inventory'),
    html.Br(),
    html.P('So here the dataset is divided into 4 time periods of roughly 5 years each and models are trained to see '
           'variables affect the house prices'),
    dcc.Dropdown(other_columns, '2003-2008', id='dropdown-time'),

])
