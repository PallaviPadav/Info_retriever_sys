import streamlit as st
import time
from info_retriever.helper import get_pdf_text, get_text_chunks
from info_retriever.helper import get_vector_store, get_conversational_chain


def user_input(user_question):
    response = st.session_state.conversation({'question':user_question})
    st.session_state.chatHistory = response['chat_history']
    # Reverse chat history → latest first
    reversed_history = st.session_state.chatHistory[::-1]
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 ==0:
            st.markdown(
                f"""
                <div style="
                    background-color:#f8d7da;
                    padding:15px;
                    border-radius:10px;
                    margin-bottom:20px;
                    border-left:6px solid #dc3545;
                ">
                    <b>🤖 Reply:</b><br>
                    {message.content}
                </div>
                """,
                unsafe_allow_html=True
            )

            #st.write("user: ", message.content)

        else:
             st.markdown(
                f"""
                <div style="
                    background-color:#d1e7dd;
                    padding:12px;
                    border-radius:10px;
                    margin-bottom:10px;
                ">
                    <b>🧑 User:</b><br>
                    {message.content}
                </div>
                """,
                unsafe_allow_html=True
            )
            #st.write("Reply: ", message.content)

def main():
    st.set_page_config(page_title="Information Retriever System", page_icon="spinner ")

    st.title("Information Retriever System 📝")
    st.header("------Information Retriever System 📝------")

    question = st.text_input("Ask any Question regarding pfd")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if question:
        user_input(question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your pdf and click on the submit & Process Button", accept_multiple_files = True)
        if st.button("Submit and Process"):
            with st.spinner("Processing ....."):
                time.sleep(2)
                text = get_pdf_text(pdf_docs)
                chunk = get_text_chunks(text)
                vector_store = get_vector_store(chunk) 
                st.session_state.conversation = get_conversational_chain(vector_store)

                st.success("Done")


if __name__ == '__main__':
    main()