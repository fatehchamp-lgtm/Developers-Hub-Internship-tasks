import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set up page configurations
st.set_page_config(page_title="Mental Health Support Chatbot", page_icon="🧠", layout="centered")

st.title("🧠 Mental Health Support Assistant")
st.write("A lightweight, empathetic conversational interface designed for emotional wellness guidance.")
st.markdown("---")


# Load local model and tokenizer
@st.cache_resource
def load_local_agent():
    model_directory = "./fine_tuned_mental_health_model"
    tokenizer = AutoTokenizer.from_pretrained(model_directory)
    model = AutoModelForCausalLM.from_pretrained(model_directory)
    return tokenizer, model


try:
    tokenizer, model = load_local_agent()

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input handler
    if user_prompt := st.chat_input("How are you feeling today?"):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Generate agent execution logs & responses
        with st.chat_message("assistant"):
            with st.spinner("Generating compassionate alignment..."):
                # Structuring sequence context injection
                formatted_input = f"Context: {user_prompt} | Response:"
                inputs = tokenizer(formatted_input, return_tensors="pt", truncation=True, max_length=128)

                # Inference execution setup
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=50,
                    pad_token_id=tokenizer.eos_token_id,
                    no_repeat_ngram_size=2,
                    do_sample=True,
                    top_k=50,
                    top_p=0.9
                )

                raw_response = tokenizer.decode(outputs[0], skip_special_tokens=True)

                # Parsing targeted token response block safely
                if "Response:" in raw_response:
                    final_response = raw_response.split("Response:")[-1].strip()
                else:
                    final_response = "I hear you, and I'm here to listen. Please take things one small step at a time. Your well-being matters."

                st.markdown(final_response)
                st.session_state.messages.append({"role": "assistant", "content": final_response})

except Exception as e:
    st.error(f"Execution Error during runtime tracking: {str(e)}")
    st.info("Ensure the './fine_tuned_mental_health_model' directory contains valid checkpoint configurations.")