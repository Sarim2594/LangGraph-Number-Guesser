from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import random

NUM=15

class AgentState(TypedDict):
    name: str
    guesses: list[int]
    attempts: int
    lower_bound: int
    upper_bound: int
    
def setup(state: AgentState) -> AgentState:
    state['guesses'] = []
    state['attempts'] = 0
    return state

def guess(state: AgentState) -> AgentState:
    state['attempts'] += 1
    state['guesses'].append(random.randint(state['lower_bound'], state['upper_bound']))
    if state['guesses'][-1] < NUM:
        state['lower_bound'] = state['guesses'][-1] + 1
    elif state['guesses'][-1] > NUM:
        state['upper_bound'] = state['guesses'][-1] - 1
    return state

def check(state: AgentState) -> AgentState:
    if state['guesses'][-1] == NUM or state['attempts'] == 7:
        return "stop_guessing"
    return "keep_guessing"

graph = StateGraph(AgentState)
graph.add_node("setup", setup)
graph.add_node("guess", guess)
graph.add_node("check", lambda state: state)  # Placeholder, logic handled in conditional edges
graph.add_edge(START, "setup")
graph.add_edge("setup", "guess")
graph.add_edge("guess", "check")
graph.add_conditional_edges("check", check, {"keep_guessing": "guess", "stop_guessing": END})

app=graph.compile()
final_state = app.invoke(
    {
        "name": "Student",
        "lower_bound": 1,
        "upper_bound": 20
    }
)
print(final_state)

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))