import streamlit as st

from api import (
    delete_report,
    get_history,
    get_markdown_download_url,
    get_pdf_download_url,
    get_report,
    start_research,
)

st.set_page_config(
    page_title="Single-Agent AI Research Assistant",
    page_icon="🤖",
    layout="wide",
)

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("🤖 Navigation")

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
Generate AI-powered research reports using **LangGraph**, **Groq**, **DuckDuckGo Search**, and **Wikipedia**.
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

                    st.info(
                        f"Job ID: {response['job_id']} started."
                    )

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

                with st.expander(
                    f"{item['query']} ({item['status']})"
                ):

                    st.write(
                        f"📅 Created: {item['created_at']}"
                    )

                    col1, col2 = st.columns(2)

                    # -------------------------
                    # VIEW REPORT
                    # -------------------------

                    with col1:

                        if st.button(
                            "📄 View Report",
                            key=f"view_{item['id']}",
                        ):

                            report = get_report(
                                item["id"]
                            )["history"]

                            st.markdown(
                                "### 📄 Research Report"
                            )

                            st.markdown(report["report"])

                            st.divider()

                            st.subheader("📥 Downloads")

                            download_col1, download_col2 = st.columns(
                                2
                            )

                            with download_col1:

                                st.link_button(
                                    "📝 Download Markdown",
                                    get_markdown_download_url(
                                        item["id"]
                                    ),
                                    use_container_width=True,
                                )

                            with download_col2:

                                st.link_button(
                                    "📄 Download PDF",
                                    get_pdf_download_url(
                                        item["id"]
                                    ),
                                    use_container_width=True,
                                )

                    # -------------------------
                    # DELETE REPORT
                    # -------------------------

                    with col2:

                        if st.button(
                            "🗑 Delete",
                            key=f"delete_{item['id']}",
                        ):

                            delete_report(item["id"])

                            st.success(
                                "Research report deleted successfully."
                            )

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
### Single-Agent AI Research Assistant

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