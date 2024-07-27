from dash import html

result = html.Div([
    html.H3('Regression analysis'),
    html.P(children="Here different models are used to predict the difference in house prices "
                    "from one month to another (it was chosen as house prices have an increasing trend "
                    "which will make it more difficult to predict because most of the other variables don't share "
                    "the same trend. "
                    "So it is better to find the impact of these variables on the variation of house prices each "
                    "month."),
    html.Iframe(
        srcDoc=open('../graphs/crossval.html', 'r', encoding='utf-8').read(),
        style={"width": "100%", "height": "600px", "border": "none"}
    ),
    html.P(children="We can see that the gradient boosting regressor has worked better than all other models. "
                    "Now let's see the feature importance of the model."),
    html.Iframe(
        srcDoc=open('../graphs/best_feature.html', 'r', encoding='utf-8').read(),
        style={"width": "100%", "height": "600px", "border": "none"}
    ),
    html.P(children="We can see that the top features are:\n"
                    "1. Mortgage Rates\n"
                    "2. Stock prices\n"  # Example placeholder
                    "3. Material costs and rent prices\n"  # Example placeholder
                    )
])
