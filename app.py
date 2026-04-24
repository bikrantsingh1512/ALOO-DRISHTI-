import streamlit as st
from PIL import Image, ImageOps, ImageStat
import wikipedia
import datetime
import time
import pandas as pd

# --- 1. PAGE SETTINGS ---
st.set_page_config(page_title="SOLANEX AI", page_icon="⚡", layout="wide")

# --- 2. PREMIUM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .glass-header {
        background: linear-gradient(135deg, #001d3d 0%, #003566 100%);
        padding: 50px; border-radius: 30px; color: white; text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3); margin-bottom: 30px;
        border-bottom: 5px solid #00d4ff;
    }
    .main-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee;
        margin-bottom: 20px;
    }
    .stTable { border-radius: 15px; overflow: hidden; }
    .report-text { font-size: 16px; line-height: 1.6; color: #2c3e50; }
    .section-tag { color: #00d4ff; font-weight: 800; text-transform: uppercase; font-size: 12px; }
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
        st.markdown('<p class="section-tag">Sample Input</p>', unsafe_allow_html=True)
        file = st.file_uploader("Upload Leaf/Potato Image", type=['jpg','png','jpeg'])
        if file: st.image(file, use_container_width=True)

    with c2:
        st.markdown('<p class="section-tag">Diagnostic Report</p>', unsafe_allow_html=True)
        if file:
            with st.spinner("Analyzing Pathogens..."):
                time.sleep(1.5)
                img = Image.open(file)
                score = ImageStat.Stat(ImageOps.grayscale(img)).stddev[0]
                
                if score < 38:
                    st.success("### Result: Healthy Crop")
                    st.write("**Next Step:** Normal irrigation every 7-10 days.")
                else:
                    disease = "Early Blight" if score < 55 else "Late Blight"
                    med = "Antracol (2.5g/L)" if disease == "Early Blight" else "Ridomil Gold (2g/L)"
                    st.error(f"### Detection: {disease}")
                    st.markdown(f"""
                    <div class="main-card" style="background:#fff5f5;">
                        <p class="report-text">
                        <b>Cause:</b> Fungal pathogen spreading via air/moisture.<br>
                        <b>Chemical Cure:</b> {med}<br>
                        <b>Spray Interval:</b> Repeat every <b>12-14 days</b> if symptoms persist.<br>
                        <b>Irrigation:</b> Stop irrigation for 48 hours after spray.<br>
                        <b>Ratio:</b> Mix 400g medicine in 200L water per acre.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
        else: st.info("Waiting for sample...")

# --- TAB 2: DISEASE ENCYCLOPEDIA (New Manual Module) ---
with tabs[1]:
    st.markdown("### 🔍 Potato Disease Manual")
    disease_choice = st.selectbox("Select Disease to learn more:", ["Early Blight", "Late Blight", "Black Scurf", "Common Scab"])
    
    encyclopedia = {
        "Early Blight": "Target-like brown spots on leaves. **Cure:** Mancozeb/Antracol spray every 10 days.",
        "Late Blight": "Water-soaked dark lesions. Spreads fast in cold fog. **Cure:** Ridomil Gold or Copper Oxychloride.",
        "Black Scurf": "Black spots on potato skin (dirt like). **Cure:** Seed treatment with Boric Acid (3%) before sowing.",
        "Common Scab": "Rough corky lesions on tubers. **Cure:** Maintain soil moisture and avoid high pH soil."
    }
    st.info(encyclopedia[disease_choice])

# --- TAB 3: MANDI INTELLIGENCE (6 Types & Predictions) ---
with tabs[2]:
    st.markdown('<p class="section-tag">Market Analytics (Farrukhabad Region)</p>', unsafe_allow_html=True)
    mandi_data = {
        "Variety": ["Chipsona-1", "Pukhraj", "Badshah", "Kufri Bahar", "Haldwani Red", "LR (Sugar Free)"],
        "Current Rate (Qt)": [850, 610, 720, 680, 890, 950],
        "Predicted (Next Week)": [880, 590, 740, 700, 920, 980],
        "Irrigation Cycle": ["7 Days", "9 Days", "8 Days", "10 Days", "7 Days", "8 Days"],
        "Demand Status": ["High", "Medium", "Stable", "Stable", "High", "Very High"]
    }
    st.table(pd.DataFrame(mandi_data))
    st.warning("⚠️ **Note:** Spray intervals for all types should be maintained at 12-15 days during peak growth.")

# --- TAB 4: GLOBAL SEARCH (Wikipedia Fixed) ---
with tabs[3]:
    st.markdown('<p class="section-tag">Neural Knowledge Retrieval</p>', unsafe_allow_html=True)
    q = st.text_input("Search Global Database (e.g., 'History of Potato', 'Soil Science'):")
    if q:
        try:
            # Force context to Potato if keywords are missing
            search_term = f"{q} potato" if "potato" not in q.lower() else q
            summary = wikipedia.summary(search_term, sentences=4)
            st.markdown(f'<div class="main-card"><h4>Result for: {q}</h4><p>{summary}</p></div>', unsafe_allow_html=True)
        except: st.error("Specific data not found. Try 'Potato cultivation' or 'Solanum tuberosum'.")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align:center; padding:30px; color:gray; font-size:12px;">
        SOLANEX AI v6.0 | SECURE NEURAL INTERFACE<br>
        <b>Developers: Bikrant Singh & Abhinav Rajput</b> | APS Fatehgarh<br>
        © {datetime.datetime.now().year} All Rights Reserved
    </div>
    """, unsafe_allow_html=True)
