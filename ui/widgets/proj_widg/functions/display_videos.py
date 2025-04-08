import streamlit as st


def display_videos(project):
    if project.video_urls:
        st.divider()
        st.caption(f"### Videos")

        for video in project.video_urls:
            st.video(video)
