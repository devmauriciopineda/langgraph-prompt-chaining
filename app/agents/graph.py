from langgraph.graph import StateGraph
from agents.state import State
from langchain_openai import AzureChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
import os
from core.config import settings
import httpx

os.environ["AZURE_OPENAI_API_KEY"] = settings.azure_openai_api_key
os.environ["AZURE_OPENAI_ENDPOINT"] = settings.azure_openai_endpoint
os.environ["OPENAI_API_VERSION"] = settings.openai_api_version


llm = AzureChatOpenAI(deployment_name="gpt-4.1", http_client=httpx.Client(verify=False))
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=settings.google_api_key)


def classify_text(state: State) -> dict:
    text = state.text
    prompt = (
        f"Classify the following text by topic: {text}. "
        "Return only the topic. Valid outputs are 'AI agents', 'other'"
    )
    topic = llm.invoke(prompt).content
    return {"topic": topic}


def route_text(state: State) -> str:
    topic = state.topic
    if topic == "AI agents":
        return "ai"
    else:
        return "other"


def summarize_text(state: State) -> dict:
    text = state.text
    prompt = f"Summarize the following text: {text}"
    summary = llm.invoke(prompt).content
    return {"summary": summary}


def translate_text(state: State) -> dict:
    summary = state.summary
    prompt = f"Traduce el siguiente texto a español: {summary}"
    translation = llm.invoke(prompt).content
    return {"translation": translation, "success": True}


def manage_irrelevant_text(state: State) -> dict:
    return {"success": False}


graph = StateGraph(State)

graph.add_node("classify", classify_text)
graph.add_node("summary", summarize_text)
graph.add_node("translation", translate_text)
graph.add_node("manage_irrelevant", manage_irrelevant_text)


graph.add_edge("__start__", "classify")
graph.add_conditional_edges(
    "classify",
    route_text,
    {"ai": "summary", "other": "manage_irrelevant"}
)
graph.add_edge("summary", "translation")
graph.add_edge("translation", "__end__")
graph.add_edge("manage_irrelevant", "__end__")


compiled_graph = graph.compile()

compiled_graph.get_graph().print_ascii()
