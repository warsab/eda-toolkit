
import pandas as pd
from IPython.display import HTML

def make_pretty(df, nr_rows=10, set_caption='Dataframe', caption_color='white', header_color='green',
                 hover_color='darkblue', max_width='600px'):
    dataframe = df.head(nr_rows)
    styler = dataframe.style
    styler.set_caption(set_caption)
    styler.set_table_styles([
        dict(selector="th", props=[("text-align", "center"), ("color", caption_color)]),
        dict(selector="caption", props=[("caption-side", "top")]),
        dict(selector="thead", props=[("background-color", header_color)]),
        dict(selector="tbody tr:hover", props=[("background-color", hover_color)]),
    ])
    styler.set_properties(**{'word-wrap': 'break-word', 'max-width': max_width})
    return styler

def view_df(df, column, focus="max", nr_rws=10, colour="green", cmap='viridis'):
    sorted_df = df.sort_values(by=column, ascending=False)
    if focus.lower() == "max":
        return sorted_df.head(nr_rws).style.set_caption(f"Maximum columns on {column}").highlight_max(subset=[column], color=colour)
    elif focus.lower() == "min":
        sorted_df = df.sort_values(by=column, ascending=True)
        return sorted_df.head(nr_rws).style.set_caption(f"Minimum columns on {column}").highlight_min(subset=[column], color=colour)
    elif focus.lower() == "null":
        return sorted_df.head(nr_rws).style.highlight_null(color=colour)
    elif focus.lower() == "heatmap":
        return sorted_df.head(nr_rws).style.background_gradient(cmap=cmap)
    elif focus.lower() == 'bar':
        return sorted_df.head(nr_rws).style.bar(color=colour)
    else:
        return sorted_df.head(nr_rws).style.highlight_max(subset=[column], color=colour)

def style_df(df, caption="dataframe", nr_rows=5, cell_colour="white"):
    styled_df = df.head(nr_rows).style.set_caption(caption).set_properties(**{'border': '2px solid green', 'color': cell_colour})
    styled_df = styled_df.format({col: "{:.2f}" for col in df.select_dtypes(include='float').columns})
    return styled_df
