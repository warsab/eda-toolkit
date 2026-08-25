
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def corr_plot(df, title="Correlation Matrix"):
    numerical_df = df.select_dtypes(include=['number'])
    if numerical_df.empty:
        raise ValueError("The DataFrame does not contain any numerical columns.")
    corr_matrix = numerical_df.corr()
    fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu', title=title)
    fig.update_layout(width=1000, height=800)
    fig.show()

def scatter_plot(df, target, columns, template="plotly_dark", logo_path="logo.png"):
    if isinstance(columns, str):
        columns = [columns]
    for col in columns:
        fig = px.scatter(df, x=col, y=target, title=f'Scatter Plot of {col} vs {target}', trendline="ols", trendline_color_override="red")
        fig.update_traces(marker=dict(color="green", size=8, opacity=0.7), selector=dict(mode='markers'))
        fig.update_layout(xaxis_title=col, yaxis_title=target, template=template)
        fig.show()

def outliers_plot(df, logo_path="logo.png"):
    numeric_columns = df.select_dtypes(include='number').columns
    fig = go.Figure()
    for i, col in enumerate(numeric_columns):
        fig.add_trace(go.Box(y=df[col], name=col, visible=(i == 0), marker=dict(color='green')))
    steps = [dict(method="update", args=[{"visible": [j == i for j in range(len(numeric_columns))]}], label=col) for i, col in enumerate(numeric_columns)]
    sliders = [dict(active=0, currentvalue={"prefix": "Feature: "}, pad={"t": 50}, steps=steps)]
    fig.update_layout(title='Outlier Box Plots', sliders=sliders, template="plotly_dark")
    fig.show()
