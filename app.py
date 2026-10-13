import streamlit as st
from model.text_summariser import text_to_chunk_convert, create_summary

st.set_page_config(page_title="Text Summariser", layout="wide")

st.title("Text Summariser")

# Create two side-by-side columns
col1, col2 = st.columns(2)

def clear_text():
    st.session_state.text_to_summarise = ""

with col1:
    st.subheader("Original Text")
    input_text = st.text_area("Enter your text:", height=300,placeholder="Paste your text here", key="text_to_summarise")


    summary_length = st.slider("Summary Length (words):", min_value=10, max_value=300, value=50)


    col11, col12 = st.columns(2)

    with col11: 
        summarize_btn = st.button("Summarize", type="primary")

    with col12: 
        clear_btn = st.button("Clear", type='secondary', on_click = clear_text)



with col2:
    st.subheader("Summary Output")
    output_container = st.container()

    if summarize_btn:
        if input_text.strip():
            text = input_text.strip()

            summary_result = create_summary(text_to_chunk_convert(text),  int(summary_length))

            output_container.write(summary_result)
        else:
            output_container.error("Please type something here!")
    else:
        output_container.info(
            "Your summary will be here"
        )