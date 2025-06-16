import yaml
from langchain.chat_models import ChatOpenAI
from langchain.agents.mcp_agent import create_openai_functions_agent

from tools.rag_retriever import query_docs
from tools.callback_logger import log_callback

# Load config


def load_config():
    with open("config/nova.yaml", "r", encoding="utf-8") as configFile:
        return yaml.safe_load(configFile)


config = load_config()

# Language-specific persona prompt
persona = config.get("persona_prompt_he")

# Initialize OpenAI model
llm = ChatOpenAI(model="gpt-4", temperature=0.3)

# Define the agent with tools
agent = create_openai_functions_agent(
    llm=llm,
    tools=[query_docs, log_callback],
    system_message=persona
)
