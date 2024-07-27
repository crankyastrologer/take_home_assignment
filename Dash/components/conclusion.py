from dash import html
factors = ["Average size of house", "Ratio of institutional investors", "Average age of house"]
concl = html.Div([
    html.P('The fluctuations in house prices are caused by complicated factors that vary over time but some of '
           'major ones include Mortgage rates, material costs, rent prices etc.'),
    html.Br(),
    html.P("Some of the variable that can affect the prices but couldn't added due to lack of available data or time "
           "constraints are:-"),
    html.Ul([html.Li(factor) for factor in factors])

])