# LangGraph Number Guesser

A simple demonstration of building a stateful, iterative agent using the **LangGraph** library. This project implements a classic **number guessing game** as a directed acyclic graph (DAG), where the agent iteratively narrows down a range to find a secret number.

## 🌟 Features

* **State Management:** Uses `TypedDict` to define the agent's state (`AgentState`), tracking guesses, attempts, and the current search bounds.
* **Iterative Process:** The graph is designed to cycle through guessing and checking until the correct number is found or the maximum number of attempts is reached.
* **Conditional Edges:** Demonstrates how to use conditional logic (`check` function) to control the flow of the graph, either looping back to make a new guess or ending the execution.
