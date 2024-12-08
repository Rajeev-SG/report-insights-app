# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

# Layouts and Containers

## Complex layouts

Streamlit provides several options for controlling how different elements are laid out on the screen.

[![screenshot](/images/api/columns.jpg)**Columns** \\
Insert containers laid out as side-by-side columns.\\
\\
`col1, col2 = st.columns(2)\\
col1.write("this is column 1")\\
col2.write("this is column 2")\\
`](/develop/api-reference/layout/st.columns) [![screenshot](/images/api/container.jpg)**Container** \\
Insert a multi-element container.\\
\\
`c = st.container()\\
st.write("This will show last")\\
c.write("This will show first")\\
c.write("This will show second")\\
`](/develop/api-reference/layout/st.container) [![screenshot](/images/api/dialog.jpg)**Modal dialog** \\
Insert a modal dialog that can rerun independently from the rest of the script.\\
\\
`@st.dialog("Sign up")\\
def email_form():\\
    name = st.text_input("Name")\\
    email = st.text_input("Email")\\
`](/develop/api-reference/execution-flow/st.dialog) [![screenshot](/images/api/empty.jpg)**Empty** \\
Insert a single-element container.\\
\\
`c = st.empty()\\
st.write("This will show last")\\
c.write("This will be replaced")\\
c.write("This will show first")\\
`](/develop/api-reference/layout/st.empty) [![screenshot](/images/api/expander.jpg)**Expander** \\
Insert a multi-element container that can be expanded/collapsed.\\
\\
`with st.expander("Open to see more"):\\
st.write("This is more content")\\
`](/develop/api-reference/layout/st.expander) [![screenshot](/images/api/popover.svg)**Popover** \\
Insert a multi-element popover container that can be opened/closed.\\
\\
`with st.popover("Settings"):\\
st.checkbox("Show completed")\\
`](/develop/api-reference/layout/st.popover) [![screenshot](/images/api/sidebar.jpg)**Sidebar** \\
Display items in a sidebar.\\
\\
`st.sidebar.write("This lives in the sidebar")\\
st.sidebar.button("Click me!")\\
`](/develop/api-reference/layout/st.sidebar) [![screenshot](/images/api/tabs.jpg)**Tabs** \\
Insert containers separated into tabs.\\
\\
`tab1, tab2 = st.tabs(["Tab 1", "Tab2"])\\
tab1.write("this is tab 1")\\
tab2.write("this is tab 2")\\
`](/develop/api-reference/layout/st.tabs)

Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

[![screenshot](/images/api/components/elements.jpg)**Streamlit Elements**](https://github.com/okld/streamlit-elements)

[Create a draggable and resizable dashboard in Streamlit. Created by](https://github.com/okld/streamlit-elements) [@okls](https://github.com/okls).

`from streamlit_elements import elements, mui, html
with elements("new_element"):
mui.Typography("Hello world")
`

[![screenshot](/images/api/components/pydantic.jpg)**Pydantic**](https://github.com/lukasmasuch/streamlit-pydantic)

[Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by](https://github.com/lukasmasuch/streamlit-pydantic) [@lukasmasuch](https://github.com/lukasmasuch).

`import streamlit_pydantic as sp
sp.pydantic_form(key="my_form",
model=ExampleModel)
`

[![screenshot](/images/api/components/pages.jpg)**Streamlit Pages**](https://github.com/blackary/st_pages)

[An experimental version of Streamlit Multi-Page Apps. Created by](https://github.com/blackary/st_pages) [@blackary](https://github.com/blackary).

`from st_pages import Page, show_pages, add_page_title
show_pages([ Page("streamlit_app.py", "Home", "🏠"),\
Page("other_pages/page2.py", "Page 2", ":books:"), ])
`

[Previous: Media elements](/develop/api-reference/media) [Next: st.columns](/develop/api-reference/layout/st.columns)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.