from langchain_google_genai import ChatGoogleGenerativeAI
import config
import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Pirate ChatBot 🏴‍☠️")

# Initialize LLM
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
        {"role": "system", "content": "You are a helpful assistant that always speaks like a pirate, using 'Ahoy', 'matey', 'Arrr', and pirate slang."}
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

    # Save user message to session_state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using full chat history
    with st.chat_message("assistant"):
        # Combine all messages (system + previous conversation)
        conversation = [msg for msg in st.session_state.messages]
        response_stream = llm.stream(conversation)
        response = st.write_stream(response_stream)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": str(response)})
