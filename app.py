import streamlit as st

from humanizer import humanize
from quality_checker import similarity_score

st.title(
    "AI Humanizer"
)

text = st.text_area(
    "Paste text here"
)

mode = st.selectbox(
    "Mode",
    [
        "casual",
        "professional",
        "academic",
        "creative"
    ]
)

if st.button(
    "Humanize"
):

    output = humanize(
        text,
        mode
    )

    score = similarity_score(
        text,
        output
    )

    st.subheader(
        "Humanized Text"
    )

    st.write(
        output
    )

    st.metric(
        "Meaning Preservation %",
        score
    )
