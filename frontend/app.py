import streamlit as st
from api import (
    delete_report,
    get_history,
    get_markdown_file,
    get_pdf_file,
    get_report,
    start_research,
)
from theme import (
    apply_theme,
    initialize_theme,
    toggle_theme,
)

st.set_page_config(
    page_title="Single-Agent AI Research Assistant",
    page_icon="🤖",
    layout="wide",
)
initialize_theme()
apply_theme()


# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("🤖 Navigation")

st.sidebar.divider()

if st.sidebar.toggle(
    "🌙 Dark Mode",
    value=st.session_state.theme == "dark",
):
    if st.session_state.theme != "dark":
        toggle_theme()
        st.rerun()
else:
    if st.session_state.theme != "light":
        toggle_theme()
        st.rerun()

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Research",
        "📜 History",
        "ℹ️ About",
    ],
    label_visibility="collapsed",
)

# -------------------------
# HOME
# -------------------------

if page == "🏠 Research":
    st.title("🤖 Single-Agent AI Research Assistant")

    st.markdown(
        """
Generate AI-powered research reports using: 
**LangGraph**
**Groq**
**DuckDuckGo Search**
**Wikipedia**.
"""
    )

    query = st.text_area(
        "Research Topic",
        placeholder="Latest developments in Artificial Intelligence",
        height=150,
    )

    if st.button(
        "🚀 Generate Report",
        use_container_width=True,
    ):
        if not query.strip():
            st.warning("Please enter a research topic.")

        else:
            with st.spinner("Starting research..."):
                try:
                    response = start_research(query)

                    st.success(response["report"])

                    st.info(f"Job ID: {response['job_id']} started.")

                except Exception as e:
                    st.error(str(e))

# -------------------------
# HISTORY
# -------------------------

elif page == "📜 History":
    st.title("📜 Research History")

    try:
        history = get_history()["history"]

        if not history:
            st.info("No research reports available.")

        else:
            for item in history:
                with st.expander(f"{item['query']} ({item['status']})"):
                    st.write(f"📅 Created: {item['created_at']}")

                    st.write(f"**Status:** {item['status']}")

                    col1, col2 = st.columns(2)

                    # -------------------------
                    # VIEW REPORT
                    # -------------------------

                    with col1:
                        if st.button(
                            "📄 View Report",
                            key=f"view_{item['id']}",
                        ):
                            report = get_report(item["id"])["history"]

                            st.markdown("### 📄 Research Report")

                            st.markdown(report["report"])

                            st.divider()

                            st.subheader("📥 Downloads")

                            download_col1, download_col2 = st.columns(2)

                            # -------------------------
                            # Markdown Download
                            # -------------------------

                            with download_col1:
                                markdown_bytes = get_markdown_file(item["id"])

                                st.download_button(
                                    label="📝 Download Markdown",
                                    data=markdown_bytes,
                                    file_name=f"{item['query']}.md",
                                    mime="text/markdown",
                                    key=f"md_{item['id']}",
                                    use_container_width=True,
                                )

                            # -------------------------
                            # PDF Download
                            # -------------------------

                            with download_col2:
                                pdf_bytes = get_pdf_file(item["id"])

                                st.download_button(
                                    label="📄 Download PDF",
                                    data=pdf_bytes,
                                    file_name=f"{item['query']}.pdf",
                                    mime="application/pdf",
                                    key=f"pdf_{item['id']}",
                                    use_container_width=True,
                                )

                    # -------------------------
                    # DELETE REPORT
                    # -------------------------

                    with col2:
                        if st.button(
                            "🗑 Delete",
                            key=f"delete_{item['id']}",
                            use_container_width=True,
                        ):
                            delete_report(item["id"])

                            st.success("Research report deleted successfully.")

                            st.rerun()

    except Exception as e:
        st.error(f"Error loading history: {e}")

# -------------------------
# ABOUT
# -------------------------

else:
    st.title("ℹ️ About")

    st.markdown(
        """
## Single-Agent AI Research Assistant

A production-ready AI research assistant built with:

- 🚀 FastAPI
- 🧠 LangGraph
- 🤖 Groq LLM
- 🔎 DuckDuckGo Search
- 📚 Wikipedia
- 🗄️ SQLAlchemy ORM
- 💾 SQLite
- 🐳 Docker
- ⚙️ GitHub Actions

---

### Features

- AI-powered research generation
- Background research jobs
- DuckDuckGo + Wikipedia search
- Markdown export
- PDF export
- Research history
- One-click downloads
- Docker support
- CI/CD with GitHub Actions

---

Developed by **Drishti Saha**
"""
    )
