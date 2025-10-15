from langchain_google_genai import ChatGoogleGenerativeAI
import config
import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("ChatBot")

# Initialize LLM properly (no `stream=True` here — streaming is handled in `invoke` or `stream` methods)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=config.GEMINI_API_KEY,
    temperature=0,
    max_output_tokens=250, 
    model_kwargs={"seed": 42}
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful tool that speaks like a pirate."}
    ]

# Display previous messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Your message..."):
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate response (streaming output)
    with st.chat_message("assistant"):
        response_stream = llm.stream(prompt)
        response = st.write_stream(response_stream)

    st.session_state.messages.append({"role": "assistant", "content": str(response)})
