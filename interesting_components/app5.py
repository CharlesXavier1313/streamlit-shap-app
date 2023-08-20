import streamlit as st

# This code is different for each deployed app.
CURRENT_THEME = "blue"
IS_DARK_THEME = True
EXPANDER_TEXT = """
    This is a custom theme. You can enable it by copying the following code
    to `.streamlit/config.toml`:

    ```python
    [theme]
    primaryColor = "#E694FF"
    backgroundColor = "#00172B"
    secondaryBackgroundColor = "#0083B8"
    textColor = "#C6CDD4"
    font = "sans-serif"
    ```
    """


# This code is the same for each deployed app.
st.image(
    (
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/"
        "apple/271/artist-palette_1f3a8.png"
    ),
    width=100,
)

st.text(
    """
# Try out Theming!

Click on the images below to view this app with different themes.
"""
)

st.text("")

THEMES = [
    "light",
    "dark",
    "green",
    "blue",
]
GITHUB_OWNER = "streamlit"

# Show thumbnails for available themes.
# As html img tags here, so we can add links on them.
cols = st.columns(len(THEMES))
for col, theme in zip(cols, THEMES):
    # Get repo name for this theme (to link to correct deployed app)-
    repo = "theming-showcase" if theme == "light" else f"theming-showcase-{theme}"
    # Set border of current theme to red, otherwise black or white
    if theme == CURRENT_THEME:
        border_color = "red"
    else:
        border_color = "lightgrey" if IS_DARK_THEME else "black"

    col.markdown(
        # f'<p align=center><a href="https://share.streamlit.io/{GITHUB_OWNER}/{repo}/main"><img
        # style="border: 1px solid {border_color}" alt="{theme}"
        # src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/
        # {theme}.png" width=150></a></p>',
        f'<p align=center><a href="https://apps.streamlitusercontent.com/'
        f'{GITHUB_OWNER}/{repo}/main/streamlit_app.py/+/"><img style="border: '
        f'1px solid {border_color}" alt="{theme}" src='
        f'"https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/'
        f'main/thumbnails/{theme}.png" width=150></a></p>',
        unsafe_allow_html=True,
    )
    if theme in ["light", "dark"]:
        theme_descriptor = f"{theme.capitalize()} theme"
    else:
        theme_descriptor = "Custom theme"
    col.write(f"<p align=center>{theme_descriptor}</p>", unsafe_allow_html=True)


st.text("")
with st.expander("Not loading?"):
    st.write(
        "You probably played around with themes before and overrode this app's "
        "theme. Go to ☰ -> Settings -> Theme and select *Custom Theme*."
    )
with st.expander("How can I use this theme in my app?"):
    st.write(EXPANDER_TEXT)

st.text("")
st.text("")


# Draw some dummy content in main page and sidebar.
def draw_all(
    key: str,
    plot: bool = False,
) -> None:
    st.write(
        """
        # Example Widgets

        These widgets don't do anything. But look at all the new colors they got 👀

        ```python
        # First some code.
        streamlit = "cool"
        theming = "fantastic"
        both = "💥"
        ```
        """
    )

    st.checkbox("Is this cool or what?", key=f"{key}_checkbox")
    st.radio(
        "How many balloons?",
        ["1 balloon 🎈", "2 balloons 🎈🎈", "3 balloons 🎈🎈🎈"],
        key=f"{key}_radio",
    )
    st.button("🤡 Click me", key=f"{key}_button")

    # if plot:
    #     st.write("Oh look, a plot:")
    #     x1 = np.random.randn(200) - 2
    #     x2 = np.random.randn(200)
    #     x3 = np.random.randn(200) + 2

    #     hist_data = [x1, x2, x3]
    #     group_labels = ["Group 1", "Group 2", "Group 3"]

    #     fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

    #     st.plotly_chart(fig, use_container_width=True)

    st.file_uploader("You can now upload with style", key=f"{key}_file_uploader")
    st.slider(
        "From 10 to 11, how cool are themes?",
        min_value=10,
        max_value=11,
        key=f"{key}_slider",
    )
    # st.select_slider("Pick a number", [1, 2, 3], key=key)
    st.number_input("So many numbers", key=f"{key}_number_input")
    st.text_area("A little writing space for you :)", key=f"{key}_text_area")
    st.selectbox(
        "My favorite thing in the world is...",
        ["Streamlit", "Theming", "Baloooons 🎈 "],
        key=f"{key}_select_box",
    )
    # st.multiselect("Pick a number", [1, 2, 3], key=key)
    # st.color_picker("Colors, colors, colors", key=key)
    with st.expander("Expand me!"):
        st.write("Hey there! Nothing to see here 👀 ")
    st.write("")
    # st.write("That's our progress on theming:")
    # st.progress(0.99)
    if plot:
        st.write("And here's some data and plots")
        st.json({"data": [1, 2, 3, 4]})
        st.dataframe({"data": [1, 2, 3, 4]})
        st.table({"data": [1, 2, 3, 4]})
        st.line_chart({"data": [1, 2, 3, 4]})
        # st.help(st.write)
    st.write("This is the end. Have fun building themes!")


draw_all("main", plot=True)

with st.sidebar:
    draw_all("sidebar")
