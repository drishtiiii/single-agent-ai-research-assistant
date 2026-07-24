import streamlit as st
from api import (
    get_history,
    get_report,
    translate_report,
)


def render_translator_page():

    st.title("🌍 AI Research Translator")

    st.caption("Translate your AI-generated research reports into multiple languages.")

    st.divider()

    history = get_history()["history"]

    completed = [item for item in history if item["status"] == "COMPLETED"]

    if not completed:
        st.info("No completed reports available.")
        return

    left, right = st.columns(2)

    with left:
        selected = st.selectbox(
            "Research Report",
            completed,
            format_func=lambda x: x["query"],
        )

    with right:
        language = st.selectbox(
            "Target Language",
            [
                "English",
                "German",
                "French",
                "Spanish",
                "Russian",
            ],
        )

    st.write("")

    if not st.button(
        "🌐 Translate Report",
        use_container_width=True,
    ):
        return

    report = get_report(selected["id"])["history"]

    with st.spinner("🌐 Translating report..."):
        translated = translate_report(
            report["report"],
            language,
        )

    st.divider()

    left, right = st.columns(2)

    # --------------------------------------------------
    # ORIGINAL REPORT
    # --------------------------------------------------

    with left:
        st.subheader("📄 Original Report")

        st.markdown(
            f"""
<div style="
height:600px;
overflow-y:auto;
padding:20px;
border:1px solid #444;
border-radius:12px;
background-color:rgba(255,255,255,0.02);
">
{report["report"]}
</div>
""",
            unsafe_allow_html=True,
        )

        action1, action2, action3 = st.columns(3)

        with action1:
            st.button(
                "📋 Copy",
                disabled=True,
                use_container_width=True,
            )

        with action2:
            st.download_button(
                "📝 Markdown",
                data=report["report"],
                file_name=f"{selected['query']}.md",
                mime="text/markdown",
                use_container_width=True,
            )

        with action3:
            st.button(
                "📄 PDF",
                disabled=True,
                use_container_width=True,
            )

    # --------------------------------------------------
    # TRANSLATED REPORT
    # --------------------------------------------------

    with right:
        st.subheader(f"🌍 {language} Translation")

        st.markdown(
            f"""
<div style="
height:600px;
overflow-y:auto;
padding:20px;
border:1px solid #444;
border-radius:12px;
background-color:rgba(255,255,255,0.02);
">
{translated["translated_report"]}
</div>
""",
            unsafe_allow_html=True,
        )

        action1, action2, action3 = st.columns(3)

        with action1:
            st.button(
                "📋 Copy",
                disabled=True,
                use_container_width=True,
            )

        with action2:
            st.download_button(
                "📝 Markdown",
                data=translated["translated_report"],
                file_name=f"{selected['query']}_{language}.md",
                mime="text/markdown",
                use_container_width=True,
            )

        with action3:
            st.button(
                "📄 PDF",
                disabled=True,
                use_container_width=True,
            )
