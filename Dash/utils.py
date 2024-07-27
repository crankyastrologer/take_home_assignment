import plotly.express as px

def create_heatmap(df,columns):
    df = df[columns]
    dff = df.corr()
    fig = px.imshow(dff)
    fig.update_layout(height=900,
        width=900)
    return fig

