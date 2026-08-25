
import pandas as pd
import plotly.graph_objects as go

def missing_values(df, logo_path="logo.png"):
    missing_data = df.isna().sum()
    percentage_missing = (missing_data / len(df)) * 100
    dtypes = df.dtypes.astype(str)
    summary_df = pd.DataFrame({
        'Column': missing_data.index,
        'Missing Value': missing_data.values,
        'Percentage': percentage_missing.values,
        'Dtypes': dtypes.values,
        'Total df Volume': len(df)
    })
    summary_df['Percentage'] = summary_df['Percentage'].apply(lambda x: f"{x:.2f}%")
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Column', 'Missing Value', 'Percentage', 'Dtypes', 'Total df Volume'],
                    fill_color='paleturquoise', align='left'),
        cells=dict(values=[summary_df[c] for c in summary_df.columns], fill_color='lavender', align='left'))
    ])
    fig.update_layout(title="Missing Values Summary", title_x=0.5, template="plotly_white", width=800, height=400)
    fig.show()
