from langchain_google_genai import ChatGoogleGenerativeAI
import config
import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Interview ChatBot")

# Personal Information Section
st.subheader('Personal information', divider='rainbow')

# Input fields for collecting user's personal information
name = st.text_input(label = "Name", max_chars = None, placeholder = "Enter your name")

experience = st.text_area(label = "Expirience", value = "", height = None, max_chars = None, placeholder = "Describe your experience")

skills = st.text_area(label = "Skills", value = "", height = None, max_chars = None, placeholder = "List your skills")

# Test labels for personal information
if name and experience and skills:
    st.write(f"**Your Name**: {name}")
    st.write(f"**Your Experience**: {experience}")
    st.write(f"**Your Skills**: {skills}")

# Company and Position Section
st.subheader('Company and Position', divider = 'rainbow')

#Field for selecting the job level, position and company
col1, col2 = st.columns(2)
with col1:
    level = st.radio(
    "Choose level",
    key="visibility", # Stores the selected value in session_state.visibility for further access
    options=["Junior", "Mid-level", "Senior"],
    )

with col2:
    position = st.selectbox(
    "Choose a position",
    key="job_position",
    options=["Data Scientist", "Data engineer", "ML Engineer", "BI Analyst", "Financial Analyst"],
    )


company = st.selectbox(
    "Choose a Company",
    ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify")
)

# Test labels for company and position information
st.write(f"**Your information**: {level} {position} at {company}")

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
