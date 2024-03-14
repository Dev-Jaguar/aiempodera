import streamlit as st
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("Hello, Admin")

st.title("🦜🔗Script Generator")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
    # Prompt
    template = "You are an experimentaded script writer, I want you to write me a family-friendly and neutral of 1 minute to 2 minutes maximum script about {topic}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter the topic:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)

st.divider()

uploaded_avatar = st.file_uploader("Upload your avatar", type=['.jpg', '.png'], accept_multiple_files=False)


if uploaded_avatar is not None:
    st.write("Name of the avatar: ", uploaded_avatar.name)
    st.image(uploaded_avatar)
st.info("Enter the avatar with extention .jpg, .png")
