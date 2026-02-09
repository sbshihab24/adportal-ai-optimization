import streamlit as st
import json
import os
import datetime
from backend.ai_engine import run_optimization_analysis

st.set_page_config(page_title="Adportal AI | Strategic Dashboard", layout="wide")

# 1. AUTOMATIC DATA LOADING
def load_local_data():
    file_path = os.path.join("sample_data", "campaign_test.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None

campaign_data = load_local_data()

# 2. PREMIUM CSS
st.markdown("""
    <style>
    .opt-card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-left: 10px solid #4F46E5;
    }
    .impact-high { border-left-color: #EF4444; }
    .impact-medium { border-left-color: #F59E0B; }
    .impact-low { border-left-color: #10B981; }
    .badge {
        padding: 6px 14px; border-radius: 20px; color: white;
        font-size: 11px; font-weight: 800; text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💡 Strategic Recommendations")
st.caption(f"Adportal AI Mindset Engine | {datetime.datetime.now().strftime('%Y-%m-%d')}")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("📊 Current Data")
    if campaign_data:
        st.json(campaign_data) 
        if st.button("🚀 Analyze Performance"):
            with st.spinner("AI is evaluating performance gaps..."):
                st.session_state.results = run_optimization_analysis(campaign_data)
    else:
        st.error("Error: sample_data/campaign_test.json not found!")

with col2:
    st.header("🤖 AI Recommendations")
    if 'results' in st.session_state:
        full_res = st.session_state.results
        optimizations = full_res.get("optimizations", [])
        
        if not optimizations:
            st.warning("No optimizations identified.")
        
        for opt in optimizations:
            impact_raw = opt.get('impact', 'Low').upper()
            if impact_raw == "HIGH":
                impact_class, badge_color = "impact-high", "#EF4444"
            elif impact_raw == "MEDIUM":
                impact_class, badge_color = "impact-medium", "#F59E0B"
            else:
                impact_class, badge_color = "impact-low", "#10B981"
            
            # --- FIXED SECTION BELOW ---
            st.markdown(f"""
            <div class="opt-card {impact_class}">
                <span class="badge" style="background-color: {badge_color};">{impact_raw} IMPACT</span>
                <h2 style="margin: 12px 0; font-size: 1.5rem;">{opt.get('subject', 'Strategic Insight')}</h2>
                <p style="color: #374151;"><b>Observation:</b> {opt.get('observation', 'N/A')}</p>
                <p style="color: #374151;"><b>Recommendation:</b> {opt.get('recommendation', 'N/A')}</p>
            </div>
            """, unsafe_allow_html=True)
            # --- END OF FIXED SECTION ---
            
        with st.expander("🛠️ Developer Tool: Raw JSON Response"):
            st.code(json.dumps(full_res, indent=2), language='json')

# End of file - Make sure the """ above is included!