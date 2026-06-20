"""
run_benchmark.py
-----------------
Entry point. Run this from the project root:

    python run_benchmark.py

Make sure Ollama is running and phi3 is pulled first:

    ollama pull phi3
"""

from src.benchmark import run_all

if __name__ == "__main__":
    run_all()