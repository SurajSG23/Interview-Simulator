from langchain_google_genai import ChatGoogleGenerativeAI
import config
import streamlit as st

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=config.GEMINI_API_KEY,
    temperature=0,
    max_output_tokens=250,
    model_kwargs={"seed": 42}
)

st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Interview ChatBot")

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

def complete_setup():
    st.session_state.setup_complete = True

if not st.session_state.setup_complete:

    st.subheader('Personal information', divider='rainbow')

    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    st.session_state["name"] = st.text_input(label = "Name", max_chars = None, value = st.session_state["name"], placeholder = "Enter your name")

    st.session_state["experience"] = st.text_area(label = "Expirience", value = st.session_state["experience"], height = None, max_chars = None, placeholder = "Describe your experience")

    st.session_state["skills"] = st.text_area(label = "Skills", value = st.session_state["skills"], height = None, max_chars = None, placeholder = "List your skills")

    st.write(f"**Your Name**: {st.session_state['name']}")
    st.write(f"**Your Experience**: {st.session_state['experience']}")
    st.write(f"**Your Skills**: {st.session_state['skills']}")

    st.subheader('Company and Position', divider = 'rainbow')

    if "level" not in st.session_state:
        st.session_state["level"] = "Junior"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "company" not in st.session_state:
        st.session_state["company"] = "Amazon"

    col1, col2 = st.columns(2)
    with col1:
         st.session_state["level"] = st.radio(
        "Choose level",
        key="visibility",
        options=["Junior", "Mid-level", "Senior"],
        )

    with col2:
        st.session_state["position"] = st.selectbox(
        "Choose a position",
        ("Data Scientist", "Data engineer", "ML Engineer", "BI Analyst", "Financial Analyst"))

    st.session_state["company"] = st.selectbox(
        "Choose a Company",
        ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify")
    )

    st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")

    if st.button("Start Interview", on_click=complete_setup):
        st.write("Setup complete. Starting interview...")


if st.session_state.setup_complete:
    st.info(
        """
        Start by introducing yourself.
        """,
        icon = "👋"
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "system",
            "content": (f"You are an HR executive that interviews an interviewee called {st.session_state['name']} "
                        f"with experience {st.session_state['experience']} and skills {st.session_state['skills']}. "
                        f"You should interview them for the position {st.session_state['level']} {st.session_state['position']} "
                        f"at the company {st.session_state['company']}")
        }]
   
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
    if prompt := st.chat_input("Your message..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            conversation = [msg for msg in st.session_state.messages]
            response_stream = llm.stream(conversation)
            response = st.write_stream(response_stream)

        st.session_state.messages.append({"role": "assistant", "content": str(response)})           
                    
                
                