import streamlit as st


def hero():
    st.markdown(
        """
<div style="padding-top:20px;padding-bottom:15px">

<h1 style="
font-size:56px;
font-weight:800;
margin-bottom:0px;">
🤖 Single-Agent AI Research Assistant
</h1>

<p style="
font-size:22px;
color:#6b7280;
margin-top:10px;
margin-bottom:25px;">
Research • Analyze • Translate • Export
</p>

<p style="
font-size:18px;
max-width:850px;
line-height:1.8;">
Generate comprehensive AI-powered research reports using
<strong>LangGraph</strong>,
<strong>Groq</strong>,
<strong>DuckDuckGo Search</strong>,
<strong>Wikipedia</strong>,
automatic report evaluation,
and multilingual translation.
</p>

</div>
""",
        unsafe_allow_html=True,
    )
