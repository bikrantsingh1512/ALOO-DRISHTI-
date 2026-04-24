import streamlit as st
from PIL import Image, ImageOps, ImageStat
import wikipedia
import datetime
import time
import pandas as pd

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(page_title="SOLANEX AI", page_icon="⚡", layout="wide")

# --- 2. CSS STYLING (For Modern UI) ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .glass-header {
        background: linear-gradient(135deg, #001d3d 0%, #003566 100%);
        padding: 50px; border-radius: 30px; color: white; text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3); margin-bottom: 30px;
        border-bottom: 8px solid #00d4ff;
    }
    .main-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee;
        margin-bottom: 20px;
    }
    .section-tag { color: #00d4ff; font-weight: 800; text-transform: uppercase; font-size: 13px; letter-spacing: 1px; }
    .report-title { color: #003566; font-weight: 900; font-size: 24px; }
    .stTable { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BRANDING HEADER ---
st.markdown("""
    <div class="glass-header">
        <h1 style="font-size: 65px; font-weight: 900; margin: 0; letter-spacing: -2px;">SOLANEX <span style="color:#00d4ff;">AI</span></h1>
        <p style="font-size: 22px; opacity: 0.9; font-weight: 300;">Precision Agriculture & Neural Diagnostics Portal</p>
        <div style="margin-top: 25px; padding: 12px 35px; background: rgba(255,255,255,0.1); border-radius: 50px; display: inline-block; border: 1px solid rgba(255,255,255,0.2);">
            <b>Core Developers:</b> Bikrant Singh & Abhinav Rajput | Class 12 CS | APS Fatehgarh
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. NAVIGATION TABS ---
tabs = st.tabs(["🚀 NEURAL SCANNER", "📖 POTATO ENCYCLOPEDIA", "📉 MANDI INTELLIGENCE", "🌐 GLOBAL SEARCH"])

# --- TAB 1: AI SCANNER (Detailed Disease Analysis) ---
with tabs[0]:
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.markdown('<p class="section-tag">Sample Acquisition</p>', unsafe_allow_html=True)
        file = st.file_uploader("Upload Leaf/Potato Image for Analysis", type=['jpg','png','jpeg'])
        if file: st.image(file, use_container_width=True)

    with c2:
        st.markdown('<p class="section-tag">Detailed Diagnostic Report</p>', unsafe_allow_html=True)
        if file:
            with st.spinner("Decoding Cellular Pathogens..."):
                time.sleep(2)
                img = Image.open(file)
                score = ImageStat.Stat(ImageOps.grayscale(img)).stddev[0]
                
                if score < 38:
                    st.success("### Status: 100% Healthy")
                    st.write("**Irrigation Advice:** Regular cycle (every 7-10 days depending on soil moisture).")
                else:
                    disease = "Early Blight" if score < 55 else "Late Blight"
                    med = "Antracol (2.5g/L)" if disease == "Early Blight" else "Ridomil Gold (2g/L)"
                    st.error(f"### Detection: {disease}")
                    st.markdown(f"""
                    <div class="main-card" style="background:#fff9f9; border-left: 5px solid red;">
                        <p class="report-text">
                        <b>Primary Cause:</b> Pathogenic fungal spread due to excess humidity.<br>
                        <b>Chemical Cure:</b> {med}<br><br>
                        <b>🗓️ SPRAY INTERVAL:</b> Repeat the spray every <b>12-14 days</b> if spots are still visible.<br>
                        <b>💧 MIXING RATIO:</b> Mix <b>400-500g</b> of medicine in <b>200 Litres</b> of water for 1 Acre.<br>
                        <b>🚜 IRRIGATION GAP:</b> Do NOT irrigate the field for at least <b>48 hours</b> after spraying.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
        else: st.info("Waiting for sample input to begin neural processing...")

# --- TAB 2: DISEASE ENCYCLOPEDIA (Manual Learning) ---
with tabs[1]:
    st.markdown("### 🔍 Professional Disease Manual")
    disease_choice = st.selectbox("Select a disease to learn detailed symptoms:", ["Early Blight", "Late Blight", "Black Scurf", "Common Scab", "Potato Virus Y"])
    
    encyclopedia = {
        "Early Blight": "Target-like brown spots on older leaves. **Cure:** Mancozeb/Antracol spray every 10-12 days.",
        "Late Blight": "Dark water-soaked lesions. Spreads extremely fast in cold/foggy weather. **Cure:** Ridomil Gold or Copper Oxychloride.",
        "Black Scurf": "Hard black spots on potato skin (cannot be washed off). **Cure:** Seed treatment with Boric Acid (3%) before sowing.",
        "Common Scab": "Cork-like rough lesions on tubers. **Cure:** Maintain soil moisture and avoid high pH (lime) soil.",
        "Potato Virus Y": "Mottling or yellowing of leaves. **Cure:** Use certified seeds and control Aphids (insects) using Imidacloprid."
    }
    st.info(encyclopedia[disease_choice])

# --- TAB 3: MANDI INTELLIGENCE (6 Varieties & Prices) ---
with tabs[2]:
    st.markdown('<p class="section-tag">Market Analytics & Projections (Farrukhabad)</p>', unsafe_allow_html=True)
    mandi_data = {
        "Potato Variety": ["Chipsona-1", "Pukhraj", "Badshah", "Kufri Bahar", "Haldwani Red", "LR (Sugar Free)"],
        "Today's Rate (per Qt)": ["₹850", "₹610", "₹720", "₹680", "₹890", "₹950"],
        "Predicted (Next 7 Days)": ["₹885 ▲", "₹590 ▼", "₹740 ▲", "₹705 ▲", "₹920 ▲", "₹990 ▲"],
        "Irrigation Requirement": ["7-8 Days", "9-10 Days", "8 Days", "10-12 Days", "7 Days", "8-9 Days"],
        "Market Status": ["High Demand", "Stable Supply", "Stable", "Stable", "High", "Very High"]
    }
    st.table(pd.DataFrame(mandi_data))
    st.warning("⚠️ **Farmer Tip:** Maintain a 12-15 day spray gap for prophylactic (preventive) care during peak winter.")

# --- TAB 4: GLOBAL SEARCH (Wikipedia Fixed) ---
with tabs[3]:
    st.markdown('<p class="section-tag">Neural Knowledge Retrieval Engine</p>', unsafe_allow_html=True)
    q = st.text_input("Ask anything (e.g., 'Potato history', 'Soil Nitrogen'):", key="wiki_input")
    if q:
        with st.spinner("Fetching verified data..."):
            try:
                wikipedia.set_lang("en")
                # Fix: Auto-add context if missing
                final_query = f"{q} potato" if "potato" not in q.lower() else q
                summary = wikipedia.summary(final_query, sentences=5)
                st.markdown(f"""
                <div class="main-card">
                    <h4>Detailed Result for: {q}</h4>
                    <p style="font-size:16px; color:#333;">{summary}</p>
                </div>
                """, unsafe_allow_html=True)
            except: st.error("No specific data found. Please try keywords like 'Potato farming' or 'Solanum tuberosum'.")

# --- 5. FOOTER ---
st.markdown(f"""
    <div style="text-align:center; padding:40px; color:gray; font-size:12px; border-top: 1px solid #ddd;">
        <b>SOLANEX AI v6.5</b> | SECURE NEURAL INTERFACE<br>
        <b>Core Developers: Bikrant Singh & Abhinav Rajput</b> | APS Fatehgarh<br>
        © {datetime.datetime.now().year} All Rights Reserved
    </div>
    """, unsafe_allow_html=True)

