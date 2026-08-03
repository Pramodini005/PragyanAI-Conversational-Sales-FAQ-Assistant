import streamlit as st

st.set_page_config(
    page_title="PragyanAI Intelligent Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PragyanAI Conversational Sales & FAQ Assistant")
st.write("Answers program questions based on the **PragyanAI Presentation & FAQ Sheet**.")

# ---------------- Sidebar ---------------- #
st.sidebar.header("Settings")

persona_name = st.sidebar.selectbox(
    "Select PragyanAI Persona",
    list(SALES_PROMPTS.keys()),
    index=0
)

uploaded_files = st.sidebar.file_uploader(
    "Upload Additional PDFs or Excel Sheets",
    type=["pdf", "xlsx", "xls"],
    accept_multiple_files=True
)

if uploaded_files:
    status = load_documents_into_vectorstore(uploaded_files)
    st.sidebar.success(status)
else:
    st.sidebar.info("PragyanAI presentation FAQ pre-loaded.")

if st.sidebar.button("Clear Chat Memory"):
    clear_chat_history(persona_name)
    st.sidebar.success("Conversation cleared.")

# ---------------- Chat History ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- User Input ---------------- #
question = st.chat_input("Ask anything about PragyanAI...")

if question:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = respond(
                question,
                st.session_state.messages,
                persona_name
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
