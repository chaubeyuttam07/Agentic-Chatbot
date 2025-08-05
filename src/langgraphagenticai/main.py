import streamlit as st 
import os
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    The load_langgraph_agenticai_app function initializes and launches the LangGraph Agentic AI application.
    It creates an instance of the Streamlit UI loader and calls its method to load the Streamlit-based user interface.
    This function serves as the entry point for starting the application's UI.
    """
    # load UI
    ui = LoadStreamlitUI()  
    user_inputs = ui.load_streamlit_ui()
    if not user_inputs:
        st.error("Error: Failed to load user input from the UI")
        return
    user_message= st.chat_input("Enter your message:")
    if user_message:
        try:
            # configure llm
            obj_llm_config= GroqLLM(user_controls_input=user_inputs)
            model= obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: LLM MODEL COULD NOT BE INITIALIZED")
                return
            # initialize and setup graph based on usecase
            usecase = user_inputs["selected_usecase"]
            if not usecase:
                st.error("Error: no usecase is selected")
                return
            # graph builder
            graph_builder= GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"error:graph setup failed-{e}")
                return
        except Exception as e:
            st.error(f"error:graph setup failed-{e}")
            return