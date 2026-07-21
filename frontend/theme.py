import streamlit as st


def initialize_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "light"


def toggle_theme():
    st.session_state.theme = (
        "dark"
        if st.session_state.theme == "light"
        else "light"
    )


def apply_theme():

    if st.session_state.theme == "dark":

        st.markdown(
            """
            <style>

            .stApp {
                background-color: #0E1117;
            }


            section[data-testid="stSidebar"] {
                background-color: #161B22;
            }


            section[data-testid="stSidebar"] * {
                color: white !important;
            }


            h1,h2,h3,h4,h5,h6 {
                color:white !important;
            }


            .stMarkdown p,
            .stMarkdown li {
                color:#E5E7EB !important;
            }


            label {
                color:white !important;
            }


            textarea {
                background-color:#161B22 !important;
                color:white !important;
            }


            textarea::placeholder {
                color:#9CA3AF !important;
            }


            div[data-testid="stExpander"] {
                background-color:#161B22 !important;
            }


            div[data-testid="stExpander"] * {
                color:white !important;
            }


            .main-title {
                color:white !important;
            }


            .sub-title {
                color:#CBD5E1 !important;
            }


            </style>
            """,
            unsafe_allow_html=True,
        )


    else:

        st.markdown(
            """
            <style>

            .stApp {
                background-color:#F7F9FC;
            }


            section[data-testid="stSidebar"] {
                background-color:white;
            }


            section[data-testid="stSidebar"] * {
                color:#111827 !important;
            }


            h1,h2,h3,h4,h5,h6 {
                color:#111827 !important;
            }


            .stMarkdown p,
            .stMarkdown li {
                color:#111827 !important;
            }


            label {
                color:#111827 !important;
            }


            textarea {
                background-color:white !important;
                color:#111827 !important;
            }


            textarea::placeholder {
                color:#6B7280 !important;
            }


            div[data-testid="stExpander"] {
                background-color:white !important;
            }


            div[data-testid="stExpander"] * {
                color:#111827 !important;
            }


            .main-title {
                color:#111827 !important;
            }


            .sub-title {
                color:#374151 !important;
            }


            </style>
            """,
            unsafe_allow_html=True,
        )