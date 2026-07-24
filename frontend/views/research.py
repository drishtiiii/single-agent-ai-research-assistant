import streamlit as st
from api import start_research
from components.feature_chips import feature_chips
from components.hero import hero


def render_research_page():
    """
    Render the Research page.
    """

    hero()

    st.markdown(
        """
    <div style="
    padding:25px;
    border-radius:18px;
    border:1px solid rgba(120,120,120,0.25);
    background-color:rgba(255,255,255,0.03);
    margin-top:15px;
    margin-bottom:20px;
    ">
    
    <h3 style="margin-top:0;">
    🔍 What would you like to research today?
    </h3>
    
    <p style="color:gray;">
    Enter any topic and the AI Research Assistant will
    generate a comprehensive research report using
    LangGraph, Groq, DuckDuckGo Search and Wikipedia.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    query = st.text_area(
        "",
        placeholder="Example: Impact of Generative AI on Healthcare",
        height=180,
        label_visibility="collapsed",
    )
    st.write("")

    if st.button(
        "🚀 Generate AI Research Report",
        use_container_width=True,
    ):
        st.write("")

        if not query.strip():
            st.warning("Please enter a research topic.")

        else:
            with st.spinner("Generating research report..."):
                try:
                    response = start_research(query)

                    st.success("Research job started successfully!")

                    st.info(f"Job ID: {response['job_id']}")

                    st.markdown("### Status")

                    st.write(response["report"])

                except Exception as e:
                    st.error(str(e))


st.divider()

feature_chips()
