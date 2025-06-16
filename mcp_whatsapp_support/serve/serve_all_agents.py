from fastapi import FastAPI
from langserve import add_routes

# Import your MCP agents
from agents.acme_support import agent as acme_agent
from agents.nova_support import agent as nova_agent

app = FastAPI(title="Multi-Agent MCP Server")

# Add each agent to a unique endpoint
add_routes(app, acme_agent, path="/acme")
add_routes(app, nova_agent, path="/nova")

# Optional health check


@app.get("/")
def read_root():
    return {"status": "MCP multi-agent server is running"}
