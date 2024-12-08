# Hello there 👋

Thanks for stopping by! We use cookies to help us understand how you interact with our website.

By clicking “Accept all”, you consent to our use of cookies. For more information, please see our [privacy policy](www.streamlit.io/privacy-policy).

Cookie settingsReject allAccept all

# Navigation and pages

[![screenshot](/images/api/navigation.jpg)**Navigation** \\
Configure the available pages in a multipage app.\\
\\
`st.navigation({\\
    "Your account" : [log_out, settings],\\
    "Reports" : [overview, usage],\\
    "Tools" : [search]\\
})\\
`](/develop/api-reference/navigation/st.navigation) [![screenshot](/images/api/page.jpg)**Page** \\
Define a page in a multipage app.\\
\\
`home = st.Page(\\
    "home.py",\\
    title="Home",\\
    icon=":material/home:"\\
)\\
`](/develop/api-reference/navigation/st.page) [![screenshot](/images/api/page_link.jpg)**Page link** \\
Display a link to another page in a multipage app.\\
\\
`st.page_link("app.py", label="Home", icon="🏠")\\
st.page_link("pages/profile.py", label="Profile")\\
`](/develop/api-reference/widgets/st.page_link) [**Switch page** \\
Programmatically navigates to a specified page.\\
\\
`st.switch_page("pages/my_page.py")\\
`](/develop/api-reference/navigation/st.switch_page)[Previous: Third-party components](https://streamlit.io/components) [Next: st.navigation](/develop/api-reference/navigation/st.navigation)_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.