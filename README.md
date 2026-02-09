# 🎯 Adportal AI Optimization Engine

An intelligent, multi-platform ad campaign analysis tool that transforms raw performance data into executive-level strategic recommendations. Built with a "Real AI Mindset," this engine identifies budget waste, scaling opportunities, and creative fatigue across Meta, Google Ads, and TikTok.



## 🚀 Project Overview

The Adportal AI Optimization Engine is a modular backend service designed to integrate seamlessly into existing ad management platforms. It leverages OpenAI's GPT-4o to provide:

* **Three-Tier Prioritization**: Suggestions are categorized into **High**, **Medium**, and **Low** impact cards for immediate action.
* **Data-Driven Insights**: Observations are backed by real metrics (ROAS, CPA, CTR) rather than generic advice.
* **Unified JSON Output**: A standardized API response format that includes metadata, campaign identifiers, and optimization objects.

## 📂 Project Structure

```text
adportal-ai-optimization/
├── backend/                # Core AI Logic (Deliverable for Developers)
│   ├── __init__.py         # Package initialization
│   ├── ai_engine.py        # The Unified Brain & JSON formatter
│   └── prompts.py          # Expert Media Strategist System Prompt
├── sample_data/            # Test campaign JSON files
├── app.py                  # Streamlit Dashboard (Visual Demo/Test Bench)
├── .env                    # API Key configuration (Environment Variables)
└── requirements.txt        # Python dependencies
```
