# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

# Data elements

When you're working with data, it is extremely valuable to visualize that
data quickly, interactively, and from multiple different angles. That's what
Streamlit is actually built and optimized for.

You can display data via [charts](#display-charts), and you can display it in
raw form. These are the Streamlit commands you can use to display and interact with raw data.

[![screenshot](/images/api/dataframe.jpg)**Dataframes** \\
Display a dataframe as an interactive table.\\
\\
`st.dataframe(my_data_frame)\\
`](/develop/api-reference/data/st.dataframe) [![screenshot](/images/api/data_editor.jpg)**Data editor** \\
Display a data editor widget.\\
\\
`edited = st.data_editor(df, num_rows="dynamic")\\
`](/develop/api-reference/data/st.data_editor) [![screenshot](/images/api/column_config.jpg)**Column configuration** \\
Configure the display and editing behavior of dataframes and data editors.\\
\\
`st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")\\
`](/develop/api-reference/data/st.column_config) [![screenshot](/images/api/table.jpg)**Static tables** \\
Display a static table.\\
\\
`st.table(my_data_frame)\\
`](/develop/api-reference/data/st.table) [![screenshot](/images/api/metric.jpg)**Metrics** \\
Display a metric in big bold font, with an optional indicator of how the metric changed.\\
\\
`st.metric("My metric", 42, 2)\\
`](/develop/api-reference/data/st.metric) [![screenshot](/images/api/json.jpg)**Dicts and JSON** \\
Display object or string as a pretty-printed JSON string.\\
\\
`st.json(my_dict)\\
`](/develop/api-reference/data/st.json)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

- <-
- ->

Previous

[![screenshot](/images/api/components/image-coordinates.jpg)**Image Coordinates**](https://github.com/blackary/streamlit-image-coordinates)

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

`from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
`

[![screenshot](/images/api/components/plotly-events.jpg)**Plotly Events**](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

`from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
`

[![screenshot](/images/api/components/extras-metric-cards.jpg)**Streamlit Extras**](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
`

[![screenshot](/images/api/components/aggrid.jpg)**Streamlit Aggrid**](https://github.com/PablocFonseca/streamlit-aggrid)

[Implementation of Ag-Grid component for Streamlit. Created by](https://github.com/PablocFonseca/streamlit-aggrid) [@PablocFonseca](https://github.com/PablocFonseca).

`df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']
`

[![screenshot](/images/api/components/folium.jpg)**Streamlit Folium**](https://github.com/randyzwitch/streamlit-folium)

[Streamlit Component for rendering Folium maps. Created by](https://github.com/randyzwitch/streamlit-folium) [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
st_data = st_folium(m, width=725)
`

[![screenshot](/images/api/components/pandas-profiling.jpg)**Pandas Profiling**](https://github.com/okld/streamlit-pandas-profiling)

[Pandas profiling component for Streamlit. Created by](https://github.com/okld/streamlit-pandas-profiling) [@okld](https://github.com/okld/).

`df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)
`

[![screenshot](/images/api/components/image-coordinates.jpg)**Image Coordinates**](https://github.com/blackary/streamlit-image-coordinates)

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

`from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
`

[![screenshot](/images/api/components/plotly-events.jpg)**Plotly Events**](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

`from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
`

[![screenshot](/images/api/components/extras-metric-cards.jpg)**Streamlit Extras**](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
`

[![screenshot](/images/api/components/aggrid.jpg)**Streamlit Aggrid**](https://github.com/PablocFonseca/streamlit-aggrid)

[Implementation of Ag-Grid component for Streamlit. Created by](https://github.com/PablocFonseca/streamlit-aggrid) [@PablocFonseca](https://github.com/PablocFonseca).

`df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']
`

[![screenshot](/images/api/components/folium.jpg)**Streamlit Folium**](https://github.com/randyzwitch/streamlit-folium)

[Streamlit Component for rendering Folium maps. Created by](https://github.com/randyzwitch/streamlit-folium) [@randyzwitch](https://github.com/randyzwitch).

`m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
st_data = st_folium(m, width=725)
`

[![screenshot](/images/api/components/pandas-profiling.jpg)**Pandas Profiling**](https://github.com/okld/streamlit-pandas-profiling)

[Pandas profiling component for Streamlit. Created by](https://github.com/okld/streamlit-pandas-profiling) [@okld](https://github.com/okld/).

`df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()
st_profile_report(pr)
`

[![screenshot](/images/api/components/image-coordinates.jpg)**Image Coordinates**](https://github.com/blackary/streamlit-image-coordinates)

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

`from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")
st.write(value)
`

[![screenshot](/images/api/components/plotly-events.jpg)**Plotly Events**](https://github.com/null-jones/streamlit-plotly-events)

[Make Plotly charts interactive!. Created by](https://github.com/null-jones/streamlit-plotly-events) [@null-jones](https://github.com/null-jones/).

`from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
`

[![screenshot](/images/api/components/extras-metric-cards.jpg)**Streamlit Extras**](https://extras.streamlit.app/)

[A library with useful Streamlit extras. Created by](https://extras.streamlit.app/) [@arnaudmiribel](https://github.com/arnaudmiribel/).

`from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
`

Next

[Previous: Text elements](/develop/api-reference/text) [Next: st.dataframe](/develop/api-reference/data/st.dataframe)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.