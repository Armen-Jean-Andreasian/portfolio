import streamlit as st

def display_screenshots(project):
    st.divider()

    st.subheader("Screenshots")
    cols = st.columns(2)

    for i, screenshot_url in enumerate(project.screenshots_urls):
        with cols[i % 2]:  # Alternate between col[0] and col[1]
            st.image(screenshot_url, use_container_width=True)  # or set width=300
