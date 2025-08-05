from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    represent the the structure of the state used in graph

    """
    messages: Annotated[list, add_messages]
    
    