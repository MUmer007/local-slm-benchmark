# 🚀 Local SLM Benchmark Platform

### Offline AI Inference with Phi-3 Mini on Resource-Constrained Hardware

> Measuring the real-world performance, latency, and deployment tradeoffs of running modern Small Language Models entirely offline.

---

## Overview

Large Language Models are often evaluated on powerful cloud infrastructure equipped with GPUs and virtually unlimited resources. However, many practical deployments operate under significantly tighter constraints:

* Edge devices
* Air-gapped environments
* Privacy-sensitive organizations
* Budget-limited infrastructure
* Offline-first applications

This project investigates a fundamental engineering question:

> **Can modern Small Language Models deliver useful AI capabilities on commodity hardware without relying on cloud APIs?**

To answer that question, I built a fully offline benchmarking platform powered by Microsoft's Phi-3 Mini running through Ollama and evaluated its performance across multiple real-world task categories.

The result is an end-to-end system capable of:

* Running local inference
* Capturing detailed performance metrics
* Benchmarking model behavior
* Visualizing results through an interactive dashboard
* Operating without internet connectivity after setup

---

# Key Highlights

✅ 100% Offline Inference

✅ No Cloud APIs

✅ No Per-Request Cost

✅ Real-Time Dashboard

✅ Automated Benchmarking Pipeline

✅ Interactive Analytics & Visualizations

✅ Tested on Low-End Hardware

---

# System Architecture

```text
┌──────────────────────────────────────┐
│           Benchmark Suite            │
│                                      │
│  • Prompt Generation                 │
│  • Scenario Execution                │
│  • Metrics Collection                │
└─────────────────┬────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────┐
│              Ollama                  │
│                                      │
│      Phi-3 Mini (2.3 GB Model)       │
└─────────────────┬────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────┐
│        Performance Collector         │
│                                      │
│ • Latency                            │
│ • Tokens Generated                   │
│ • Throughput                         │
│ • Cold/Warm Start Analysis           │
└─────────────────┬────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────┐
│        Analytics Dashboard           │
│                                      │
│ • Plotly Charts                      │
│ • Interactive Metrics                │
│ • Benchmark Reports                  │
└──────────────────────────────────────┘
```

---

# Technology Stack

| Layer               | Technology        |
| ------------------- | ----------------- |
| Local Model Runtime | Ollama            |
| Language Model      | Phi-3 Mini        |
| Backend API         | FastAPI           |
| Benchmark Engine    | Python            |
| Data Analysis       | Pandas            |
| Visualization       | Plotly            |
| Dashboard           | HTML + JavaScript |

---

# Hardware Configuration

The benchmark intentionally avoids high-performance hardware.

| Component | Specification            |
| --------- | ------------------------ |
| CPU       | Intel Core i5-6300U      |
| Cores     | 2 Physical / 4 Logical   |
| GPU       | None                     |
| Memory    | 8 GB RAM                 |
| Storage   | SATA SSD                 |
| OS        | Windows/Linux Compatible |

This configuration represents hardware commonly found in:

* Legacy business laptops
* Educational environments
* Edge computing devices
* Small office deployments

---

# Benchmark Methodology

A total of **60 controlled inference runs** were executed.

### Task Categories

* Logical Reasoning
* Summarization
* Code Generation
* Creative Writing
* Factual Question Answering

### Prompt Variants

| Variable      | Options      |
| ------------- | ------------ |
| Prompt Length | Short / Long |
| Temperature   | 0.2 / 0.8    |
| Repetitions   | 3            |

### Metrics Collected

Each inference request recorded:

* Total latency
* Generation latency
* Output token count
* Tokens per second
* Cold-start status
* Prompt category
* Temperature setting
* Prompt length

---

# Results

## Average Performance by Task Category

| Category         | Avg Latency | Avg Tokens/sec | Fastest Run | Slowest Run |
| ---------------- | ----------- | -------------- | ----------- | ----------- |
| Code Generation  | 234.27s     | 2.88           | 22.11s      | 1191.86s    |
| Reasoning        | 119.25s     | 3.17           | 36.77s      | 222.06s     |
| Factual QA       | 119.33s     | 3.71           | 17.01s      | 295.47s     |
| Creative Writing | 57.71s      | 2.90           | 13.81s      | 82.53s      |
| Summarization    | 53.49s      | 3.17           | 39.66s      | 73.00s      |

---

# Engineering Insights

## 1. Task Complexity Dominates Runtime

Prompt length and temperature influenced runtime less than expected.

The strongest predictor of latency was the task itself.

Code generation workloads consistently produced the slowest responses while summarization remained the most stable category.

### Deployment Implication

Infrastructure planning should prioritize expected workload type rather than relying solely on model specifications.

---

## 2. Small Models Can Still Demonstrate Reasoning

Despite its compact size, Phi-3 successfully solved classic reasoning problems including the Bat-and-Ball cognitive bias test.

This suggests that carefully designed SLMs can provide meaningful reasoning capabilities without requiring massive parameter counts.

---

## 3. Memory Constraints Become Visible During Long Sessions

The largest latency spikes appeared during later benchmark stages.

Observed behavior suggests increasing memory pressure and system contention on an 8 GB machine.

### Why This Matters

Many benchmark reports exclude these effects.

In production deployments, however, sustained performance degradation is often more important than best-case performance.

---

# Dashboard Features

The included web dashboard provides:

* Live model interaction
* Benchmark result exploration
* Throughput analysis
* Latency visualization
* Category comparison
* Temperature comparison
* Cold vs Warm start analysis

Generated outputs include:

```text
speed_by_category.html
latency_by_length.html
speed_by_temperature.html
cold_vs_warm.html
summary_by_category.csv
```

---

# Project Structure

```text
local-slm-benchmark/
│
├── src/
│   ├── benchmark.py
│   ├── models.py
│   └── prompts.py
│
├── results/
│   └── benchmark.json
│
├── charts/
│   ├── speed_by_category.html
│   ├── latency_by_length.html
│   ├── speed_by_temperature.html
│   ├── cold_vs_warm.html
│   └── summary_by_category.csv
│
├── templates/
│   └── index.html
│
├── app.py
├── run_benchmark.py
├── generate_charts.py
└── requirements.txt
```

---

# Running the Project

## 1. Install Ollama

```bash
ollama serve
```

## 2. Download Phi-3

```bash
ollama pull phi3
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Benchmark Suite

```bash
python run_benchmark.py
```

## 5. Generate Analytics

```bash
python generate_charts.py
```

## 6. Launch Dashboard

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

# Skills Demonstrated

This project showcases practical experience in:

* Local LLM Deployment
* AI Performance Benchmarking
* Prompt Engineering
* FastAPI Development
* Data Analysis
* Systems Performance Evaluation
* Interactive Data Visualization
* Edge AI Deployment
* Offline AI Systems
* Python Software Engineering

---

# Future Work

Potential extensions include:

* Multi-model benchmarking
* Quantized model comparison
* RAG integration
* Memory utilization profiling
* CPU utilization analysis
* Energy consumption benchmarking
* ARM-based edge device testing
* Automated benchmark scheduling

---

# Conclusion

This project demonstrates that modern Small Language Models can provide meaningful AI functionality entirely offline while operating on hardware that would typically be considered unsuitable for AI workloads.

While latency remains a significant constraint, the tradeoff enables complete privacy, zero inference cost, and deployment independence—characteristics that remain critical for many real-world applications.

The benchmark provides a realistic view of what local AI deployment looks like beyond marketing claims and laboratory conditions.
