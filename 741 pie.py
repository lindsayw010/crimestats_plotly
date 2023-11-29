import plotly.express as px
import plotly.graph_objects as go

labels = ['Unknown', '30 to 39', '20 to 29', '40 to 49', '10 to 19', '50 to 59', '60 to 69', '70 to 79', '90 to Older', '0 to 9', '80 to 89']
values = [854727, 556240, 503456, 304140, 262165, 219368, 51474, 9299, 5765, 4477, 1864]
colors = ['red', 'orange', 'yellow', 'lime', 'aqua', 'mediumorchid', 'deeppink', 'gainsboro', 'silver', 'gray', 'dimgray']

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(hoverinfo='label+value', textfont_size=20, textfont_color="white",
                  marker=dict(colors=colors))
fig.update_layout(paper_bgcolor="black", hoverlabel=dict(bgcolor="white", font_size=20, font_family="Rockwell"), font_color="white",
                  title={'text': "2022 All Property Crime Offender Ages", 'y':0.93, 'x':0.47})
fig.write_html('first_figure.html', auto_open=True)

#line=dict(color="white", width=2)