# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

1. Contents
2. [Caching](#caching)
3. [Manage state](#manage-state)
4. [Deprecated commands](#deprecated-commands)

# Caching and state

Optimize performance and add statefulness to your app!

## Caching

Streamlit provides powerful [cache primitives](/develop/concepts/architecture/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

[**Cache data** \\
Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).\\
\\
`@st.cache_data\\
def long_function(param1, param2):\\
# Perform expensive computation here or\\
# fetch data from the web here\\
return data\\
`](/develop/api-reference/caching-and-state/st.cache_data) [**Cache resource** \\
Function decorator to cache functions that return global resources (e.g. database connections, ML models).\\
\\
`@st.cache_resource\\
def init_model():\\
# Return a global resource here\\
return pipeline(\\
    "sentiment-analysis",\\
    model="distilbert-base-uncased-finetuned-sst-2-english"\\
)\\
`](/develop/api-reference/caching-and-state/st.cache_resource)

## Manage state

Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

[**Session State** \\
Save data between reruns and across pages.\\
\\
`st.session_state["foo"] = "bar"\\
`](/develop/api-reference/caching-and-state/st.session_state) [**Query parameters** \\
Get, set, or clear the query parameters that are shown in the browser's URL bar.\\
\\
`st.query_params[key] = value\\
st.query_params.clear()\\
`](/develop/api-reference/caching-and-state/st.query_params)

## Deprecated commands

[_delete_\\
\\
> This command was deprecated in version 1.18.0. Use `st.cache_data` instead.\\
\\
**Memo** \\
Experimental function decorator to memoize function executions.\\
\\
`@st.experimental_memo\\
def fetch_and_clean_data(url):\\
# Fetch data from URL here, and then clean it up.\\
return data\\
`](/develop/api-reference/caching-and-state/st.experimental_memo) [_delete_\\
\\
> This command was deprecated in version 1.18.0. Use `st.cache_resource` instead.\\
\\
**Singleton** \\
Experimental function decorator to store singleton objects.\\
\\
`@st.experimental_singleton\\
def get_database_session(url):\\
# Create a database session object that points to the URL.\\
return session\\
`](/develop/api-reference/caching-and-state/st.experimental_singleton) [_delete_\\
**Get query parameters** \\
Get query parameters that are shown in the browser's URL bar.\\
\\
`param_dict = st.experimental_get_query_params()\\
`](/develop/api-reference/caching-and-state/st.experimental_get_query_params) [_delete_\\
**Set query parameters** \\
Set query parameters that are shown in the browser's URL bar.\\
\\
`st.experimental_set_query_params(\\
{"show_all"=True, "selected"=["asia", "america"]}\\
)\\
`](/develop/api-reference/caching-and-state/st.experimental_set_query_params)[Previous: Execution flow](/develop/api-reference/execution-flow) [Next: st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.