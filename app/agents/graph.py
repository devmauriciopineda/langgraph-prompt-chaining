from langgraph.graph import StateGraph
from agents.state import State
# from langchain_openai import AzureChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from core.config import settings

os.environ["AZURE_OPENAI_API_KEY"] = settings.azure_openai_api_key
os.environ["AZURE_OPENAI_ENDPOINT"] = settings.azure_openai_endpoint
os.environ["OPENAI_API_VERSION"] = settings.openai_api_version


# llm = AzureChatOpenAI(deployment_name="gpt-4.1", verify=False)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=settings.google_api_key)


def summarize_text(state: State) -> dict:
    text = state.text
    prompt = f"Summarize the following text: {text}"
    summary = llm.invoke(prompt).content
    return {"summary": summary}


def translate_text(state: State) -> dict:
    summary = state.summary
    prompt = f"Traduce el siguiente texto a español: {summary}"
    translation = llm.invoke(prompt).content
    return {"translation": translation}


graph = StateGraph(State)

graph.add_node("summary", summarize_text)
graph.add_node("translation", translate_text)

graph.add_edge("__start__", "summary")
graph.add_edge("summary", "translation")
graph.add_edge("translation", "__end__")

compiled_graph = graph.compile()
