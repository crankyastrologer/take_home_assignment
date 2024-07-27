from dash import html

introduction = html.P(
    children="The Housing prices affect the everyday life of nearly all individuals in US here we try to find different "
             "variables that might affect house prices")

data_visualization = html.P(
    children="Here we are comparing different variables included in this study with house prices and house prices difference"
             "which is basically the change in the house price (all the data is normalized to better fit on the same scale in "
             "the graph")
factors_with_links = [
    ("GDP growth", "https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=US&most_recent_year_desc=false"),
    ("House inventory the no of houses listed for sale in market", "https://fred.stlouisfed.org/series/ACTLISCOUUS"),
    ("House prices", "http://fred.stlouisfed.org/series/CSUSHPISA"),
    ("Houses built no of houses completed", "https://www.census.gov/construction/nrc/historical_data/index.html"),
    ("Inflation", "https://www.usinflationcalculator.com/inflation/current-inflation-rates/"),
    ("Material prices", "https://fred.stlouisfed.org/series/WPUSI012011"),
    ("Mortgage rates", "https://fred.stlouisfed.org/series/MORTGAGE30US/"),
    ("Population growth", "https://data.worldbank.org/indicator/SP.POP.GROW?locations=US"),
    ("S&P index",
     "https://finance.yahoo.com/quote/%5EGSPC/history/?frequency=1mo&period1=1027296000&period2=1721668158"),
    ("Unemployment rate", "https://www.bls.gov/charts/employment-situation/civilian-unemployment-rate.htm#"),
    ("Vacancy rate % of vacant houses up for rent", "https://fred.stlouisfed.org/series/RRVRUSQ156N"),
    ("rent price", "https://fred.stlouisfed.org/series/CUUR0000SEHA")
]
links = html.Ul([html.Li(html.A(factor[0], href=factor[1], target="_blank")) for factor in factors_with_links])
