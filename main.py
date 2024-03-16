# !/usr/bin/env python

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file (assuming it's in the same directory)
load_dotenv()

def app():
  st.title("Empower-Medica")

  # Conversation History (list to store user and model responses)
  conversation = []

  # Chat Input Area with Placeholder Text
  user_input = st.text_input("Ask Empower-Medica anything...", key="user_input")

  # Submit Button for a Cleaner Look
  if st.button("Ask"):
      if user_input:
          # Update Conversation History
          conversation.append({"role": "user", "parts": [user_input]})

          # Integrate Generative AI with Conversation History
          google_generative_ai_key = st.secrets["google_generative_ai_key"]
          
          # Integrate Generative AI with Conversation History
          genai.configure(api_key=google_generative_ai_key)
          model = genai.GenerativeModel(model_name="tunedModels/empower-medica-chatbot--kuwtcvdjyalv")
          convo = model.start_chat(history=conversation)
          convo.send_message(user_input)
          model_response = convo.last.text

          # Update Conversation History with Model Response
          conversation.append({"role": "model", "parts": [model_response]})

          # Display Conversation History
          for message in conversation:
              st.write(f"{message['role']}: {message['parts'][0]}")
          animate_chat_bubbles()  # Call animation after processing
      else:
          st.warning("Please enter your question before asking.")

def animate_chat_bubbles():
  """
  Animates three chat bubbles with CSS transitions.
  """
  bubble_styles = """
  .bubble {
    display: inline-block;
    width: 100px;
    height: 50px;
    border-radius: 10px;
    background-color: #ddd;
    margin: 0 5px;
    animation-name: bob;
    animation-duration: 2s;
    animation-iteration-count: infinite;
  }
  
  @keyframes bob {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
  }
  """
  st.write('<style>' + bubble_styles + '</style>', unsafe_allow_html=True)
  for i in range(3):
      st.write('<div class="bubble"></div>', unsafe_allow_html=True)

if __name__ == "__main__":
  app()
