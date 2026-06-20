"""
generate_charts.py
-------------------
Reads results/benchmark.json and produces interactive HTML charts
in the charts/ folder. Run this AFTER run_benchmark.py has completed.

    python generate_charts.py
"""

import json
import pathlib
import pandas as pd
import plotly.express as px

ROOT = pathlib.Path(__file__).resolve().parent
RESULTS_PATH = ROOT / "results" / "benchmark.json"
CHARTS_DIR = ROOT / "charts"

CHARTS_DIR.mkdir(exist_ok=True)

# Load the raw benchmark data into a pandas DataFrame (a table) for easy analysis.
data = json.loads(RESULTS_PATH.read_text())
df = pd.DataFrame(data)

print(f"Loaded {len(df)} benchmark results.\n")

# ---------------------------------------------------------------------
# Chart 1: Tokens/sec by task category
# Shows which kinds of tasks Phi-3 handles fastest vs slowest.
# ---------------------------------------------------------------------
fig1 = px.box(
    df, x="category", y="tokens_per_sec", color="category",
    title="Phi-3 Generation Speed by Task Category",
    labels={"tokens_per_sec": "Tokens / sec", "category": "Task Category"},
    points="all",
)
fig1.write_html(CHARTS_DIR / "speed_by_category.html")
print("Saved: charts/speed_by_category.html")

# ---------------------------------------------------------------------
# Chart 2: Latency by prompt length (short vs long)
# Shows how response time scales with input/output size.
# ---------------------------------------------------------------------
fig2 = px.box(
    df, x="prompt_length", y="total_latency_s", color="prompt_length",
    title="Total Latency: Short vs Long Prompts",
    labels={"total_latency_s": "Total Latency (seconds)", "prompt_length": "Prompt Length"},
    points="all",
)
fig2.write_html(CHARTS_DIR / "latency_by_length.html")
print("Saved: charts/latency_by_length.html")

# ---------------------------------------------------------------------
# Chart 3: Temperature comparison (deterministic vs creative)
# Shows whether temperature setting affects speed.
# ---------------------------------------------------------------------
fig3 = px.box(
    df, x="temperature_label", y="tokens_per_sec", color="temperature_label",
    title="Speed: Deterministic vs Creative Temperature",
    labels={"tokens_per_sec": "Tokens / sec", "temperature_label": "Temperature Setting"},
    points="all",
)
fig3.write_html(CHARTS_DIR / "speed_by_temperature.html")
print("Saved: charts/speed_by_temperature.html")

# ---------------------------------------------------------------------
# Chart 4: Cold start vs warm runs
# Shows the real cost of the FIRST call after idle vs repeated calls.
# ---------------------------------------------------------------------
fig4 = px.box(
    df, x="cold_start", y="total_latency_s", color="cold_start",
    title="Cold Start vs Warm Run Latency",
    labels={"total_latency_s": "Total Latency (seconds)", "cold_start": "Is Cold Start?"},
    points="all",
)
fig4.write_html(CHARTS_DIR / "cold_vs_warm.html")
print("Saved: charts/cold_vs_warm.html")

# ---------------------------------------------------------------------
# Summary table printed to console + saved as CSV
# ---------------------------------------------------------------------
summary = df.groupby("category").agg(
    avg_latency_s=("total_latency_s", "mean"),
    avg_tokens_per_sec=("tokens_per_sec", "mean"),
    min_latency_s=("total_latency_s", "min"),
    max_latency_s=("total_latency_s", "max"),
    total_runs=("run", "count"),
).round(2)

print("\n--- Summary by Category ---")
print(summary.to_string())

summary.to_csv(CHARTS_DIR / "summary_by_category.csv")
print(f"\nSaved: charts/summary_by_category.csv")

print("\nAll charts generated. Open the .html files in charts/ with your browser.")