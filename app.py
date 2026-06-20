"""
app.py
------
FastAPI backend for the Phi-3 local inference dashboard.

Run with:
    uvicorn app:app --reload

Then open your browser to:
    http://127.0.0.1:8000
"""

import time
import ollama
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Phi-3 Local Inference Dashboard")
templates = Jinja2Templates(directory="templates")


class InferRequest(BaseModel):
    prompt: str
    temperature: float = 0.7


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serves the dashboard page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/infer")
async def infer(req: InferRequest):
    """
    Receives a prompt from the webpage, sends it to Phi-3 via Ollama,
    times the response, and returns the result + metrics as JSON.
    """
    start = time.perf_counter()

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": req.prompt}],
        options={"temperature": req.temperature},
    )

    elapsed = time.perf_counter() - start
    content = response["message"]["content"]
    tokens = response.get("eval_count") or len(content.split())
    tokens_per_sec = round(tokens / elapsed, 2) if elapsed > 0 else 0.0

    return {
        "response": content,
        "latency_s": round(elapsed, 2),
        "tokens": tokens,
        "tokens_per_sec": tokens_per_sec,
    }