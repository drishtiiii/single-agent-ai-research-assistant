import streamlit as st


def initialize_theme():
    """Initialize the theme."""
    if "theme" not in st.session_state:
        st.session_state.theme = "light"


def toggle_theme():
    """Toggle theme."""
    if st.session_state.theme == "light":
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"


def apply_theme():
    """Apply CSS according to selected theme."""

    if st.session_state.theme == "dark":

        st.markdown("""
<style>

.stApp{
    background:#0E1117;
    color:#FAFAFA;
}

section[data-testid="stSidebar"]{
    background:#161B22;
}

section[data-testid="stSidebar"] *{
    color:#FAFAFA !important;
}

div.stButton > button{
    background:#2563EB;
    color:white;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

    else:

        st.markdown("""
<style>

.stApp{
    background:#F7F9FC;
    color:#111827;
}

section[data-testid="stSidebar"]{
    background:#FFFFFF;
}

section[data-testid="stSidebar"] *{
    color:#111827 !important;
}

div.stButton > button{
    background:#2563EB;
    color:white;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)