from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from streamlit_js_eval import streamlit_js_eval


# Gemini AI Setup
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=st.secrets["GEMINI_API_KEY"],
    temperature=0,
    max_output_tokens=250,
    model_kwargs={"seed": 42}
)


# Setting up the Streamlit page configuration
st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Interview ChatBot")


# Initialize session state variables
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
    
if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0
    
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False
    
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = False


# Helper functions to update session state
def show_feedback():
    st.session_state.feedback_shown = True
    
def complete_setup():
    st.session_state.setup_complete = True


# Setup stage for collecting user details
if not st.session_state.setup_complete:
    st.subheader('Personal Information')

    # Initialize session state for personal information
    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    # Get personal information input
    st.session_state["name"] = st.text_input(label="Name", value=st.session_state["name"], placeholder="Enter your name", max_chars=40)
    st.session_state["experience"] = st.text_area(label="Experience", value=st.session_state["experience"], placeholder="Describe your experience", max_chars=200)
    st.session_state["skills"] = st.text_area(label="Skills", value=st.session_state["skills"], placeholder="List your skills", max_chars=200)

    # Company and Position Section
    st.subheader('Company and Position')

    # Initialize session state for company and position information and setting default values 
    if "level" not in st.session_state:
        st.session_state["level"] = "Junior"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "company" not in st.session_state:
        st.session_state["company"] = "Deloitte"

    col1, col2 = st.columns(2)
    with col1:
        st.session_state["level"] = st.radio(
            "Choose level",
            key="visibility",
            options=["Junior", "Mid-level", "Senior"],
            index=["Junior", "Mid-level", "Senior"].index(st.session_state["level"])
        )

    with col2:
        st.session_state["position"] = st.selectbox(
            "Choose a position",
            ("Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst", "Financial Analyst"),
            index=("Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst", "Financial Analyst").index(st.session_state["position"])
        )

    st.session_state["company"] = st.selectbox(
        "Select a Company",
        ("Deloitte", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"),
        index=("Deloitte", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify").index(st.session_state["company"])
    )

    # Button to complete setup
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
            "content": (f"You are an HR executive interviewing a candidate named {st.session_state['name']} "
                        f"who has experience {st.session_state['experience']} and skills {st.session_state['skills']}. "
                        f"You are interviewing them for the position {st.session_state['level']} {st.session_state['position']} "
                        f"at the company {st.session_state['company']}. "
                        f"Ask only **one question at a time**, wait for the candidate’s answer, then respond naturally and move to the next question. "
                        f"Keep your tone professional, conversational, and realistic, as in an actual HR interview."
            )
        }]
   
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
    if st.session_state.user_message_count < 5:     
        if prompt := st.chat_input("Your message..."):
            with st.chat_message("user"):
                st.markdown(prompt)

            st.session_state.messages.append({"role": "user", "content": prompt})
            
            if st.session_state.user_message_count < 4:
                with st.chat_message("assistant"):
                    conversation = [msg for msg in st.session_state.messages]
                    response_stream = llm.stream(conversation)
                    response = st.write_stream(response_stream)

                st.session_state.messages.append({"role": "assistant", "content": str(response)})           
             
            st.session_state.user_message_count += 1
        
    # Check if the user message count reaches 5
    if st.session_state.user_message_count >= 5:
        st.session_state.chat_complete = True           
                    
# Show "Get Feedback" 
if st.session_state.chat_complete and not st.session_state.feedback_shown:
    if st.button("Get Feedback", on_click=show_feedback):
        st.write("Fetching feedback...")    

# Show feedback screen
if st.session_state.feedback_shown:
    st.subheader("Feedback")

    conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    messages = [
            {
                "role": "system",
                "content": """You are a helpful tool that provides feedback on an interviewee performance.
                Before the feedback give a score of 1 to 10.
                Follow this format:
                Overall Score: //Your score
                Feedback: //Here you put your feedback
                Give only the feedback. Do not ask any additional questions."""
            },
            {
                "role": "user",
                "content": f"This is the interview you need to evaluate. Keep in mind that you are only a tool and should not engage in conversation:\n{conversation_history}"
            }
    ]
    response_stream = llm.stream(messages)
    response = st.write_stream(response_stream)

    # Button to restart the interview
    if st.button("Restart Interview", type="primary"):
            streamlit_js_eval(js_expressions="parent.window.location.reload()")