from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi import Request
from pydantic import BaseModel
import os
from openai import OpenAI
from termcolor import colored
import json

# Constants
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o"

# Initialize FastAPI
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize OpenAI client
try:
    client = OpenAI()
    print(colored("OpenAI client initialized successfully", "green"))
except Exception as e:
    print(colored(f"Error initializing OpenAI client: {str(e)}", "red"))
    raise

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_mindmap")
async def generate_mindmap(topic_request: TopicRequest):
    try:
        print(colored(f"Generating mindmap for topic: {topic_request.topic}", "cyan"))
        
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """You are a mindmap generator. Create a detailed mindmap structure in JSON format.
                    The structure should have a central node with the main topic, and branches with subtopics and their details.
                    JSON response format should be: 
                    {
                        "nodes": [
                            {"id": "1", "label": "Main Topic", "level": 0},
                            {"id": "2", "label": "Subtopic 1", "level": 1},
                            ...
                        ],
                        "edges": [
                            {"from": "1", "to": "2"},
                            ...
                        ]
                    }"""
                },
                {
                    "role": "user",
                    "content": f"Create a detailed mindmap about: {topic_request.topic}"
                }
            ],
            response_format={"type": "json_object"}
        )
        
        print(colored("Successfully generated mindmap data", "green"))
        return JSONResponse(content=json.loads(completion.choices[0].message.content))

    except Exception as e:
        print(colored(f"Error generating mindmap: {str(e)}", "red"))
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True) 