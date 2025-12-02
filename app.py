import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI()

## Will start with the API creation
@app.post("/blogs")
async def create_blogs(request: Request):
    data = await request.json()
    topic = data.get("topic", "").strip()
    language = data.get("language", "").strip().lower()

    ## Input validation
    if not topic:
        return JSONResponse(status_code=400, content={"error": "Missing 'topic' in request body."})

    ## Get the LLM object
    groqllm = GroqLLM()
    llm = groqllm.get_llm()

    ## Get the appropriate graph
    graph_builder = GraphBuilder(llm)
    if language in ["hindi", "french"]:
        graph = graph_builder.setup_graph(usecase="language")
        state = graph.invoke({"topic": topic, "current_language": language})
    else:
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic": topic})

    return {"data": state}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)