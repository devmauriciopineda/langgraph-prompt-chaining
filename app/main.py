from agents.graph import compiled_graph

TEXT = """
What makes an AI system an Agent?
In simple terms, an AI agent is a system designed to perceive its environment and take actions to achieve a specific goal. It's an evolution from a standard Large Language Model (LLM), enhanced with the abilities to plan, use tools, and interact with its surroundings. Think of an Agentic AI as a smart assistant that learns on the job. It follows a simple, five-step loop to get things done (see Fig.1):
Get the Mission: You give it a goal, like "organize my schedule."
Scan the Scene: It gathers all the necessary information—reading emails, checking calendars, and accessing contacts—to understand what's happening.
Think It Through: It devises a plan of action by considering the optimal approach to achieve the goal.
Take Action: It executes the plan by sending invitations, scheduling meetings, and updating your calendar.
Learn and Get Better: It observes successful outcomes and adapts accordingly. For example, if a meeting is rescheduled, the system learns from this event to enhance its future performance.
"""

result = compiled_graph.invoke({"text": TEXT})
print("----")
print("Summary:\n")
print(result["summary"])
print("----")
print("Translation:\n")
print(result["translation"])

