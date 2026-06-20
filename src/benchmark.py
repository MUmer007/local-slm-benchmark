"""
benchmark.py
------------
Core benchmark engine.

Runs Phi-3 across multiple dimensions instead of comparing multiple
models (the test machine is a dual-core CPU laptop with no GPU and
8 GB RAM, so this project benchmarks ONE model under varying real-world
conditions rather than racing several large models against each other):

  1. Task category   -> reasoning, summarize, code, creative, factual
  2. Prompt length    -> short vs long (tests latency scaling with context)
  3. Temperature      -> deterministic (0.2) vs creative (0.8)
  4. Cold vs warm run -> first call after idle vs repeated calls

Results are written to results/benchmark.json for downstream charting.
"""

import json
import pathlib
import sys

# Allow running this file directly (python src/benchmark.py) or as a module
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from src.models import LocalModel
from src.prompts import PROMPTS, TEMPERATURES

MODEL_NAME = "phi3"
RUNS_PER_CONDITION = 3  # repeat each condition N times to smooth out noise
RESULTS_PATH = pathlib.Path(__file__).resolve().parent.parent / "results" / "benchmark.json"


def run_all() -> list[dict]:
    model = LocalModel(MODEL_NAME)
    results = []
    total_calls = len(PROMPTS) * 2 * len(TEMPERATURES) * RUNS_PER_CONDITION
    call_num = 0

    print(f"Starting benchmark: {total_calls} total inference calls on '{MODEL_NAME}'")
    print("This may take a while on CPU-only hardware. Sit tight.\n")

    for category, variants in PROMPTS.items():
        for length_label, prompt_text in variants.items():
            for temp_label, temp_value in TEMPERATURES.items():
                for run_idx in range(1, RUNS_PER_CONDITION + 1):
                    call_num += 1
                    is_cold_start = (run_idx == 1)

                    result = model.generate(prompt_text, temperature=temp_value)
                    result.update({
                        "category": category,
                        "prompt_length": length_label,
                        "temperature_label": temp_label,
                        "run": run_idx,
                        "cold_start": is_cold_start,
                    })
                    results.append(result)

                    print(
                        f"[{call_num}/{total_calls}] {category:<10} | {length_label:<5} | "
                        f"{temp_label:<13} | run {run_idx} | "
                        f"{result['total_latency_s']}s | {result['tokens_per_sec']} tok/s"
                    )

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nDone. Saved {len(results)} results to {RESULTS_PATH}")

    return results


if __name__ == "__main__":
    run_all()