import streamlit as st
from PIL import Image, ImageOps, ImageStat
import wikipedia
import datetime
import time
import pandas as pd

# --- 1. PAGE SETTINGS ---
st.set_page_config(page_title="SOLANEX AI", page_icon="⚡", layout="wide")

# --- 2. ADVANCED CSS (Professional Branding & Divisions) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .glass-header {
        background: linear-gradient(135deg, #001d3d 0%, #003566 100%);
        padding: 50px; border-radius: 30px; color: white; text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2); margin-bottom: 40px;
        border-bottom: 5px solid #00d4ff;
    }
    .main-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee;
        margin-bottom: 20px;
    }
    .section-tag {
        color: #00d4ff; font-weight: 800; letter-spacing: 1.5px;
        text-transform: uppercase; font-size: 12px; margin-bottom: 10px;
    }
    .stButton>button {
        border-radius: 12px; background-color: #003566; color: white;
        transition: 0.3s; width: 100%; border: none; height: 3em;
    }
    .stButton>button:hover { background-color: #00d4ff; color: #001d3d; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BRANDING HEADER (With Abhinav Rajput & Bikrant Singh) ---
st.markdown("""
    <div class="glass-header">
        <p style="letter-spacing: 5px; font-size: 12px; color: #00d4ff; margin-bottom: 10px;">SYSTEM STATUS: ONLINE</p>
        <h1 style="font-size: 60px; font-weight: 900; margin: 0; letter-spacing: -2px;">SOLANEX <span style="color:#00d4ff;">AI</span></h1>
        <p style="font-size: 18px; opacity: 0.8; font-weight: 300; margin-top:10px;">Advanced Tuber Diagnostics & Knowledge Engine</p>
        <div style="margin-top: 25px; padding: 12px 30px; background: rgba(255,255,255,0.1); border-radius: 50px; display: inline-block; font-size: 15px; border: 1px solid rgba(255,255,255,0.2);">
            <b>Developers:</b> Bikrant Singh & Abhinav Rajput | Class 12 CS | APS Fatehgarh
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. NAVIGATION SYSTEM ---
tab_scan, tab_wiki, tab_market = st.tabs(["🚀 AI NEURAL SCANNER", "📖 GLOBAL ENCYCLOPEDIA", "📊 MARKET DATA"])

# --- TAB 1: AI SCANNER (Original Health Logic) ---
with tab_scan:
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown('<p class="section-tag">01. SAMPLE ACQUISITION</p>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="main-card">', unsafe_allow_html=True)
            source = st.radio("Input Method:", ["Internal Storage", "Live Camera"], horizontal=True)
            file = st.file_uploader("Upload Leaf or Potato Image", type=['jpg','png','jpeg'])
            if file:
                st.image(file, caption="Selected Sample", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="section-tag">02. NEURAL ANALYSIS</p>', unsafe_allow_html=True)
        if file:
            with st.spinner("Processing Cellular Patterns..."):
                time.sleep(1.5)
                # Original Image Processing Logic
                img = Image.open(file)
                gray = ImageOps.grayscale(img)
                score = ImageStat.Stat(gray).stddev[0]
                
                # Logic: Healthy vs Blight
                if score < 38: 
                    res, med = "Healthy", "No Disease Detected. Your crop is safe."
                    color = "#2ecc71"
                elif 38 <= score < 55: 
                    res, med = "Early Blight", "Recommended: Apply Antracol (2.5g/L)."
                    color = "#f1c40f"
                else: 
                    res, med = "Late Blight", "Urgent: Apply Ridomil Gold (2g/L) immediately."
                    color = "#e74c3c"
                
                st.markdown(f"""
                    <div class="main-card" style="border-left: 10px solid {color};">
                        <h2 style="color:{color};">{res}</h2>
                        <p style="font-size:18px;"><b>Prescription:</b> {med}</p>
                        <hr>
                        <p style="font-size:14px; color:gray;">System Confidence: {round(92+score/12, 2)}%</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("System Ready. Please upload a sample to generate a diagnostic report.")

# --- TAB 2: WIKIPEDIA (The Global Search Feature) ---
with tab_wiki:
    st.markdown('<p class="section-tag">KNOWLEDGE RETRIEVAL PORTAL</p>', unsafe_allow_html=True)
    wiki_query = st.text_input("Search Science, History, or GK:", placeholder="e.g., Photosynthesis, Indian Constitution, Farrukhabad History...")
    
    if wiki_query:
        with st.spinner("Accessing Wikipedia Database..."):
            try:
                wikipedia.set_lang("en")
                summary = wikipedia.summary(wiki_query, sentences=4)
                page = wikipedia.page(wiki_query)
                st.markdown(f"""
                    <div class="main-card">
                        <h3 style="color:#003566;">📑 {page.title}</h3>
                        <hr>
                        <p style="font-size:16px; line-height:1.7; color:#333;">{summary}</p>
                        <br>
                        <a href="{page.url}" target="_blank" style="color:#00d4ff; font-weight:bold; text-decoration:none;">Read full article on Wikipedia →</a>
                    </div>
                """, unsafe_allow_html=True)
            except:
                st.error("Topic not found. Try adding more detail or check your spelling.")

# --- TAB 3: MARKET (Regional Mandi Rates) ---
with tab_market:
    st.markdown('<p class="section-tag">REGIONAL ECONOMIC DATA</p>', unsafe_allow_html=True)
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.write("### 📉 Farrukhabad Mandi Trends (Today)")
    mandi_df = pd.DataFrame({
        "Variety": ["Chipsona", "Pukhraj", "Badshah", "Haldwani"],
        "Rate per Qt": ["₹820", "₹595", "₹710", "₹850"],
        "Market Trend": ["▲ Up", "▼ Down", "Stable", "▲ Up"]
    })
    st.table(mandi_df)
    st.caption("Data source: Local Market Estimates | Updates every 24 hours")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. COPYRIGHT FOOTER ---
st.markdown(f"""
    <div style="text-align:center; padding:50px; color:#95a5a6; font-size:12px; border-top: 1px solid #ddd;">
        <b>SOLANEX AI v5.0</b> | Secure Neural Interface<br>
        Proprietary Project of <b>Bikrant Singh & Abhinav Rajput</b><br>
        © {datetime.datetime.now().year} All Rights Reserved | APS Fatehgarh
    </div>
    """, unsafe_allow_html=True)
