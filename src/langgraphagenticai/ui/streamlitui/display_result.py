import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
      self.usecase=usecase
      self.graph=graph
      self.user_message=user_message
      if usecase=="BasiChatbot":
          for event in graph.stream({'messages':('user',user_message)}):
              print(event.values())
              for value in event.values():
                  print(value['messsages'])
                  with st.chat_message("user"):
                      st.write(user_message)
                  with st.chat_message("assistant"):
                      st.write(value["message"].content)
                  