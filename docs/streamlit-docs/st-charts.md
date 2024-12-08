# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Simple chart elements](#simple-chart-elements)
3. [Advanced chart elements](#advanced-chart-elements)

# Chart elements

Streamlit supports several different charting libraries, and our goal is to
continually add support for more. Right now, the most basic library in our
arsenal is [Matplotlib](https://matplotlib.org/). Then there are also
interactive charting libraries like [Vega\\
Lite](https://vega.github.io/vega-lite/) (2D charts) and
[deck.gl](https://github.com/uber/deck.gl) (maps and 3D charts). And
finally we also provide a few chart types that are "native" to Streamlit,
like `st.line_chart` and `st.area_chart`.

## Simple chart elements

[![screenshot](/images/api/area_chart.jpg)**Simple area charts** \\
Display an area chart.\\
\\
`st.area_chart(my_data_frame)\\
`](/develop/api-reference/charts/st.area_chart) [![screenshot](/images/api/bar_chart.jpg)**Simple bar charts** \\
Display a bar chart.\\
\\
`st.bar_chart(my_data_frame)\\
`](/develop/api-reference/charts/st.bar_chart) [![screenshot](/images/api/line_chart.jpg)**Simple line charts** \\
Display a line chart.\\
\\
`st.line_chart(my_data_frame)\\
`](/develop/api-reference/charts/st.line_chart) [![screenshot](/images/api/scatter_chart.svg)**Simple scatter charts** \\
Display a line chart.\\
\\
`st.scatter_chart(my_data_frame)\\
`](/develop/api-reference/charts/st.scatter_chart) [![screenshot](/images/api/map.jpg)**Scatterplots on maps** \\
Display a map with points on it.\\
\\
`st.map(my_data_frame)\\
`](/develop/api-reference/charts/st.map)

## Advanced chart elements

[![screenshot](/images/api/pyplot.jpg)**Matplotlib** \\
Display a matplotlib.pyplot figure.\\
\\
`st.pyplot(my_mpl_figure)\\
`](/develop/api-reference/charts/st.pyplot) [![screenshot](/images/api/vega_lite_chart.jpg)**Altair** \\
Display a chart using the Altair library.\\
\\
`st.altair_chart(my_altair_chart)\\
`](/develop/api-reference/charts/st.altair_chart) [![screenshot](/images/api/vega_lite_chart.jpg)**Vega-Lite** \\
Display a chart using the Vega-Lite library.\\
\\
`st.vega_lite_chart(my_vega_lite_chart)\\
`](/develop/api-reference/charts/st.vega_lite_chart) [![screenshot](/images/api/plotly_chart.jpg)**Plotly** \\
Display an interactive Plotly chart.\\
\\
`st.plotly_chart(my_plotly_chart)\\
`](/develop/api-reference/charts/st.plotly_chart) [![screenshot](/images/api/bokeh_chart.jpg)**Bokeh** \\
Display an interactive Bokeh chart.\\
\\
`st.bokeh_chart(my_bokeh_chart)\\
`](/develop/api-reference/charts/st.bokeh_chart) [![screenshot](/images/api/pydeck_chart.jpg)**PyDeck** \\
Display a chart using the PyDeck library.\\
\\
`st.pydeck_chart(my_pydeck_chart)\\
`](/develop/api-reference/charts/st.pydeck_chart) [![screenshot](/images/api/graphviz_chart.jpg)**GraphViz** \\
Display a graph using the dagre-d3 library.\\
\\
`st.graphviz_chart(my_graphviz_spec)\\
`](/develop/api-reference/charts/st.graphviz_chart)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

- <-
- ->

Previous

[![screenshot](/images/api/components/lottie.jpg)**Streamlit Lottie**](https://github.com/andfanilo/streamlit-lottie)

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

`lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
`

[![screenshot](/images/api/components/plotly-events.jpg)**Plotly Events**](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

`fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
`

[![screenshot](/images/api/components/extras-chart-annotations.jpg)**Streamlit Extras**](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

`chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
`

[![screenshot](/images/api/components/plost.jpg)**Plost**](https://github.com/tvst/plost)

[A deceptively simple plotting library for Streamlit. Created by](https://github.com/tvst/plost) [@tvst](https://github.com/tvst).

`import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
`

[![screenshot](/images/api/components/hiplot.jpg)**HiPlot**](https://github.com/facebookresearch/hiplot)

[High dimensional Interactive Plotting. Created by](https://github.com/facebookresearch/hiplot) [@facebookresearch](https://github.com/facebookresearch).

`data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
`

[![screenshot](/images/api/components/echarts.jpg)**ECharts**](https://github.com/andfanilo/streamlit-echarts)

[High dimensional Interactive Plotting. Created by](https://github.com/andfanilo/streamlit-echarts) [@andfanilo](https://github.com/andfanilo).

`from streamlit_echarts import st_echarts
st_echarts(options=options)
`

[![screenshot](/images/api/components/folium.jpg)**Streamlit Folium**](https://github.com/randyzwitch/streamlit-folium)

[Streamlit Component for rendering Folium maps. Created by](https://github.com/randyzwitch/streamlit-folium) [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
`

[![screenshot](/images/api/components/spacy.jpg)**Spacy-Streamlit**](https://github.com/explosion/spacy-streamlit)

[spaCy building blocks and visualizers for Streamlit apps. Created by](https://github.com/explosion/spacy-streamlit) [@explosion](https://github.com/explosion).

`models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
`

[![screenshot](/images/api/components/agraph.jpg)**Streamlit Agraph**](https://github.com/ChrisDelClea/streamlit-agraph)

[A Streamlit Graph Vis, based on](https://github.com/ChrisDelClea/streamlit-agraph) [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

`from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
`

[![screenshot](/images/api/components/lottie.jpg)**Streamlit Lottie**](https://github.com/andfanilo/streamlit-lottie)

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

`lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
`

[![screenshot](/images/api/components/plotly-events.jpg)**Plotly Events**](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

`fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
`

[![screenshot](/images/api/components/extras-chart-annotations.jpg)**Streamlit Extras**](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

`chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
`

[![screenshot](/images/api/components/plost.jpg)**Plost**](https://github.com/tvst/plost)

[A deceptively simple plotting library for Streamlit. Created by](https://github.com/tvst/plost) [@tvst](https://github.com/tvst).

`import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
`

[![screenshot](/images/api/components/hiplot.jpg)**HiPlot**](https://github.com/facebookresearch/hiplot)

[High dimensional Interactive Plotting. Created by](https://github.com/facebookresearch/hiplot) [@facebookresearch](https://github.com/facebookresearch).

`data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
`

[![screenshot](/images/api/components/echarts.jpg)**ECharts**](https://github.com/andfanilo/streamlit-echarts)

[High dimensional Interactive Plotting. Created by](https://github.com/andfanilo/streamlit-echarts) [@andfanilo](https://github.com/andfanilo).

`from streamlit_echarts import st_echarts
st_echarts(options=options)
`

[![screenshot](/images/api/components/folium.jpg)**Streamlit Folium**](https://github.com/randyzwitch/streamlit-folium)

[Streamlit Component for rendering Folium maps. Created by](https://github.com/randyzwitch/streamlit-folium) [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
`

[![screenshot](/images/api/components/spacy.jpg)**Spacy-Streamlit**](https://github.com/explosion/spacy-streamlit)

[spaCy building blocks and visualizers for Streamlit apps. Created by](https://github.com/explosion/spacy-streamlit) [@explosion](https://github.com/explosion).

`models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
`

[![screenshot](/images/api/components/agraph.jpg)**Streamlit Agraph**](https://github.com/ChrisDelClea/streamlit-agraph)

[A Streamlit Graph Vis, based on](https://github.com/ChrisDelClea/streamlit-agraph) [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

`from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
`

[![screenshot](/images/api/components/lottie.jpg)**Streamlit Lottie**](https://github.com/andfanilo/streamlit-lottie)

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

`lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
`

[![screenshot](/images/api/components/plotly-events.jpg)**Plotly Events**](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

`fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
`

[![screenshot](/images/api/components/extras-chart-annotations.jpg)**Streamlit Extras**](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

`chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
`

Next

[Previous: Data elements](/develop/api-reference/data) [Next: st.area\_chart](/develop/api-reference/charts/st.area_chart)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.