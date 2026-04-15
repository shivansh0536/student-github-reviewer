from langgraph.graph import StateGraph, END
from .state import ReviewState
from .nodes import extract_github_data, code_mentor_review

# 1. Create a new graph
workflow = StateGraph(ReviewState)

# 2. Define the nodes
workflow.add_node("extractor", extract_github_data)
workflow.add_node("mentor", code_mentor_review)

# 3. Define the edges
workflow.set_entry_point("extractor")
workflow.add_edge("extractor", "mentor")
workflow.add_edge("mentor", END)

# 4. Compile the graph into a runnable app
github_reviewer_app = workflow.compile()