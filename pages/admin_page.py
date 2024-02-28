import streamlit as st

st.title("Hello, Admin")

st.info("We will only admit the script in .txt")
uploaded_scripts = st.file_uploader("Upload your script", type=['.txt'], accept_multiple_files=True)

for uploaded_script in uploaded_scripts:
    bytes_data = uploaded_script.read()
    st.write("Filename: ", uploaded_script.name)
    st.write("Content: ", bytes_data)

st.divider()

uploaded_avatar = st.file_uploader("Upload your avatar", type=['.jpg', '.png'], accept_multiple_files=False)
st.write("Name of the avatar: ", uploaded_avatar)
st.image(uploaded_avatar)
