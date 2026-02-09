import openai
import os
import json
import datetime
from dotenv import load_dotenv

# Change this line: Remove the dot (.) before prompts
try:
    from backend.prompts import SYSTEM_PROMPT
except ImportError:
    from prompts import SYSTEM_PROMPT

# Load API keys from .env file
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_optimization_analysis(campaign_data: dict):
    """
    The main engine for Adportal AI. 
    It processes any multi-platform JSON and returns a structured JSON response.
    """
    try:
        # 1. Send the data to GPT-4o with the Expert Mindset prompt
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Analyze this campaign data: {json.dumps(campaign_data)}"}
            ],
            response_format={"type": "json_object"} # Ensures AI returns valid JSON
        )
        
        # 2. Extract the AI's analysis
        ai_payload = json.loads(response.choices[0].message.content)
        
        # 3. Extract campaign details for metadata
        overview = campaign_data.get("campaign_overview", {})
        campaign_id = overview.get("campaign_id", "unknown")
        campaign_name = overview.get("name", "Unnamed Campaign")

        # 4. Build the Unified JSON Response for the Backend
        final_json = {
            "status": "success",
            "metadata": {
                "campaign_id": campaign_id,
                "campaign_name": campaign_name,
                "processed_at": datetime.datetime.now().isoformat()
            },
            "optimizations": ai_payload.get("optimizations", [])
        }
        
        return final_json

    except Exception as e:
        # Return a structured error JSON so the backend doesn't crash
        return {
            "status": "error",
            "message": str(e),
            "processed_at": datetime.datetime.now().isoformat()
        }
    
















    # --- Check in terminal output

# --- CLEAN MAIN BLOCK FOR TERMINAL TEST ---

if __name__ == "__main__":
    import json
    
    # 1. Define sample data
    test_data = {
        "campaign_overview": {"campaign_id": "TEST-101", "name": "Terminal Test"},
        "performance_metrics": {
            "Meta": {"roas": 1.5, "spend": 1000},
            "Google Ads": {"roas": 4.8, "spend": 200}
        }
    }
    
    # 2. Run analysis
    result = run_optimization_analysis(test_data)
    
    # 3. Filter only necessary fields for display
    # This prevents the "too much list" problem
    clean_display = {
        "status": result.get("status"),
        "metadata": result.get("metadata"),
        "optimizations": result.get("optimizations")
    }
    
    # 4. Print clean JSON
    print("\n--- STANDALONE AI REPORT ---")
    print(json.dumps(clean_display, indent=4))