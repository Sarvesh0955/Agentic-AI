"""
Cloud LLM Model Configuration
This file defines available free working models for Gemini and Groq.
Since .env is ignored by Git, model selections in this file can be committed to Git.
"""

import os

# ==============================================================================
# Active Selected Models (Uncomment ONE line to select active model)
# ==============================================================================

# Gemini Active Model Selection
GEMINI_MODEL = "gemini-3.6-flash"                     # Gemini 3.6 Flash - Fast general-purpose tasks (Recommended)
# GEMINI_MODEL = "gemini-3.7-flash"                   # Gemini 3.7 Flash - Latest Flash model
# GEMINI_MODEL = "gemini-3.5-flash"                   # Gemini 3.5 Flash - Stable general purpose
# GEMINI_MODEL = "gemini-3.5-flash-lite"              # Gemini 3.5 Flash-Lite - Fast/lightweight tasks
# GEMINI_MODEL = "gemini-3.1-flash-lite"              # Gemini 3.1 Flash-Lite - Lightweight 3.1 model
# GEMINI_MODEL = "gemini-2.5-flash"                   # Gemini 2.5 Flash - Stable 2.5 model

# Groq Active Model Selection
GROQ_MODEL = "openai/gpt-oss-120b"                    # GPT-OSS 120B - Reasoning, coding, agents (Recommended)
# GROQ_MODEL = "openai/gpt-oss-20b"                   # GPT-OSS 20B - Faster/lighter reasoning
# GROQ_MODEL = "qwen/qwen3.8-27b"                     # Qwen 3.8 27B - Reasoning, coding, general tasks
# GROQ_MODEL = "groq/compound"                        # Groq Compound - Multi-tool composite model
# GROQ_MODEL = "groq/compound-mini"                   # Groq Compound Mini - Fast composite model
# GROQ_MODEL = "allam-2-7b"                           # ALLaM 2 7B - Lightweight language model
# GROQ_MODEL = "openai/gpt-oss-safeguard-20b"         # GPT-OSS Safeguard 20B - Moderation/safeguard model


# ==============================================================================
# Verified Working Models Catalog
# ==============================================================================
AVAILABLE_GEMINI_MODELS = {
    "gemini-3.6-flash": "Fast general-purpose tasks (Recommended)",
    "gemini-3.7-flash": "Latest Flash model",
    "gemini-3.5-flash": "Stable general purpose",
    "gemini-3.5-flash-lite": "Fast/lightweight tasks",
    "gemini-3.1-flash-lite": "Lightweight 3.1 model",
    "gemini-2.5-flash": "Stable 2.5 model",
}

AVAILABLE_GROQ_MODELS = {
    "openai/gpt-oss-120b": "Reasoning, coding, agents (Recommended)",
    "openai/gpt-oss-20b": "Faster/lighter reasoning",
    "qwen/qwen3.8-27b": "Reasoning, coding, general tasks",
    "groq/compound": "Multi-tool composite model",
    "groq/compound-mini": "Fast composite model",
    "allam-2-7b": "Lightweight language model",
    "openai/gpt-oss-safeguard-20b": "Moderation/safeguard model",
}


def get_gemini_model():
    return os.getenv("GEMINI_MODEL", GEMINI_MODEL)


def get_groq_model():
    return os.getenv("GROQ_MODEL", GROQ_MODEL)
