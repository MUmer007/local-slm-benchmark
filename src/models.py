"""
models.py
---------
Thin wrapper around the Ollama Python client.

Every inference call goes through this class so timing, token counts,
and response capture are measured identically across every test run.
This consistency is what makes the benchmark numbers comparable.
"""

import time
import ollama


class LocalModel:
    """Wraps a single Ollama model and standardizes how we call + measure it."""

    def __init__(self, name: str):
        self.name = name

    def generate(self, prompt: str, temperature: float = 0.7) -> dict:
        """
        Run one inference call and return timing + token metrics.

        Measures wall-clock latency around the full call (includes model
        load time if the model isn't already warm in memory — this is
        intentional, since cold-start latency is a real deployment cost
        on constrained hardware).
        """
        start = time.perf_counter()

        response = ollama.chat(
            model=self.name,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": temperature},
        )

        elapsed = time.perf_counter() - start

        content = response["message"]["content"]

        # eval_count = number of tokens generated, reported directly by Ollama.
        # Fall back to a word-count estimate if the field is ever missing.
        tokens = response.get("eval_count") or len(content.split())

        # eval_duration is nanoseconds spent purely on generation (excludes
        # model load time). We convert it so we can separately report
        # "pure generation speed" vs "total wall-clock latency."
        eval_duration_ns = response.get("eval_duration", 0)
        eval_duration_s = eval_duration_ns / 1e9 if eval_duration_ns else elapsed

        tok_per_sec = round(tokens / eval_duration_s, 2) if eval_duration_s > 0 else 0.0

        return {
            "model": self.name,
            "prompt": prompt,
            "response": content,
            "response_length_chars": len(content),
            "total_latency_s": round(elapsed, 3),
            "generation_time_s": round(eval_duration_s, 3),
            "tokens_generated": tokens,
            "tokens_per_sec": tok_per_sec,
            "temperature": temperature,
        }