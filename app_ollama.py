import streamlit as st
import ollama
import os

# Define the Ollama model you want to use (make sure it's downloaded)
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3") # Default to llama3 if not set

QUESTIONS = [
    {
        "question": "How do you use VLOOKUP to find a value in a table?",
        "expected": "You write =VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])."
    },
    {
        "question": "What is the difference between absolute and relative cell references in Excel?",
        "expected": "Relative references change when copied, absolute references ($A$1) do not."
    },
    {
        "question": "Explain how to create a Pivot Table in Excel.",
        "expected": "Select data → Insert → PivotTable → Choose fields for rows, columns, and values."
    }
]

st.title("🧑‍💻 AI Excel Mock Interviewer (Ollama Version)")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.evaluations = []

# Basic check if Ollama is running (optional, but good practice)
try:
    ollama.list()
    ollama_available = True
except Exception as e:
    st.warning(f"Could not connect to Ollama. Please ensure Ollama is running and the model '{OLLAMA_MODEL}' is downloaded. Error: {e}")
    ollama_available = False

if ollama_available:
    if st.session_state.step < len(QUESTIONS):
        q = QUESTIONS[st.session_state.step]
        st.subheader(f"Question {st.session_state.step+1}: {q['question']}")
        user_answer = st.text_area("Your Answer:", key=f"answer_{st.session_state.step}")

        if st.button("Submit Answer"):
            prompt = f'''
            You are an Excel interviewer. Evaluate the candidate's answer.

            Question: {q['question']}
            Expected Answer: {q['expected']}
            Candidate's Answer: {user_answer}

            Give:
            - Score (0-5)
            - Feedback in 2 sentences
            '''
            try:
                # Use Ollama to generate the evaluation
                response = ollama.chat(
                    model=OLLAMA_MODEL,
                    messages=[{'role': 'user', 'content': prompt}]
                )
                evaluation = response['message']['content']
                st.session_state.evaluations.append(evaluation)
                st.session_state.step += 1
                st.rerun()
            except Exception as e:
                st.error(f"Error during Ollama API call: {e}")


    else:
        st.subheader("✅ Interview Complete!")
        for i, eval in enumerate(st.session_state.evaluations):
            st.write(f"**Q{i+1}:** {QUESTIONS[i]['question']}")
            st.write(eval)
        st.success("This concludes your interview. Thank you!")
else:
     st.warning("Ollama is not available. Please set it up to run this version of the app.")