import streamlit as st


def show_footer(linked_in_url: str, github_url: str, twitter_url: str = ""):
    footer_html = f"""
        <div style="text-align: center; margin-top: 50px;">
            <a href="{linked_in_url}" target="_blank" style="margin-right: 15px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" width="40">
            </a>
            <a href="{github_url}" target="_blank" style="margin-right: 15px;">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="40">
            </a>
        </div>
        """


    st.markdown(footer_html, unsafe_allow_html=True)
