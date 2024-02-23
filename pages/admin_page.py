import streamlit as st

st.title("Hello, Admin")

st.info("We will only admit the script in .txt")
uploaded_files = st.file_uploader("Upload the script", type=['.txt'], accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("Filename: ", uploaded_file.name)
    st.write("Content: ", bytes_data)

