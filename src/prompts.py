"""
prompts.py
----------
Test prompt bank for the Phi-3 edge-inference benchmark.

Each task category has a SHORT and LONG variant so we can measure
how latency and quality scale with prompt/context length on
constrained hardware (no GPU, 2-core CPU, 8 GB RAM).
"""

PROMPTS = {
    "reasoning": {
        "short": "A bat and ball cost $1.10. The bat costs $1 more than the ball. How much does the ball cost?",
        "long": (
            "A small bakery sells cupcakes and cookies. On Monday, they sold 3 times as many "
            "cookies as cupcakes, and the total number of items sold was 48. On Tuesday, they "
            "sold half as many cupcakes as Monday, but the same number of cookies as Monday. "
            "How many cupcakes and how many cookies were sold in total across both days? "
            "Show your reasoning step by step."
        ),
    },
    "summarize": {
        "short": "Summarize the causes of World War 1 in exactly 3 bullet points.",
        "long": (
            "Summarize the following passage in exactly 3 bullet points: "
            "The Industrial Revolution, which began in Britain in the late 18th century, "
            "transformed economies that had been based on agriculture and handicrafts into "
            "economies based on large-scale industry, mechanized manufacturing, and the "
            "factory system. New machines, new power sources, and new ways of organizing "
            "work made existing industries more productive and efficient. It also led to "
            "rapid urbanization as people moved from rural areas to cities for factory jobs, "
            "and it created significant social changes including the rise of a working class "
            "and changes in family structure, while also causing pollution and harsh labor "
            "conditions that eventually led to labor rights movements."
        ),
    },
    "code": {
        "short": "Write a Python function to check if a string is a palindrome.",
        "long": (
            "Write a Python function called `validate_password` that checks if a password "
            "meets the following requirements: at least 8 characters long, contains at least "
            "one uppercase letter, one lowercase letter, one digit, and one special character "
            "from the set !@#$%^&*. The function should return a tuple of (bool, str) where "
            "the string explains which requirement failed, or 'valid' if it passed. Include "
            "docstring and at least 2 example usages in comments."
        ),
    },
    "creative": {
        "short": "Write a 4-line poem about a robot learning to feel emotions.",
        "long": (
            "Write a short story, no more than 150 words, about an old laptop that gets "
            "donated to a school in a remote village and experiences being used by a child "
            "for the first time. Give it a clear beginning, middle, and end."
        ),
    },
    "factual": {
        "short": "What are the main differences between RAM and ROM? Be concise.",
        "long": (
            "Explain how a CPU cache works, including the difference between L1, L2, and L3 "
            "cache, why caches exist, and how cache misses affect performance. Keep the "
            "explanation suitable for someone studying computer architecture for the first time."
        ),
    },
}

# Temperature settings to test decoding-level speed/quality tradeoff.
# Low temperature = more deterministic/focused. High = more varied/creative.
TEMPERATURES = {
    "deterministic": 0.2,
    "creative": 0.8,
}