import streamlit as st


def feature_chips():

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🧠 LangGraph")
        st.success("⚡ Groq")

    with c2:
        st.info("🌐 DuckDuckGo")
        st.info("📚 Wikipedia")

    with c3:
        st.warning("📄 PDF Export")
        st.warning("🌍 Translation")
