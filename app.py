import streamlit as st
from agents import run_agent_query

st.set_page_config(
    page_title="Quetta Safe Hub 3",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 32px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 20px;
    }
    .agent-card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🛡️ Quetta Safe Hub 3 - Advanced Multi-Agent Command Center</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ System Status")
    st.success("Groq API Key Loaded from Secrets!")
    st.markdown("---")
    st.markdown("### 🤖 Active Agents")
    st.markdown("- Traffic & ANPR Agent")
    st.markdown("- Emergency Response Agent")
    st.markdown("- System Health & Admin Agent")

tab1, tab2, tab3 = st.tabs(["🚀 Live Agent Operations", "📊 Infrastructure Specs", "ℹ️ About Application"])

with tab1:
    st.subheader("Interactive Multi-Agent Hub")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="agent-card">', unsafe_allow_html=True)
        st.subheader("🚗 Traffic & ANPR")
        st.write("Vehicle recognition & multi-lane statistics tracking.")
        user_query_1 = st.text_input("Query Traffic Agent:", key="q1")
        if st.button("Run Traffic Agent"):
            if user_query_1:
                with st.spinner("Analyzing traffic data..."):
                    res = run_agent_query("Traffic & ANPR Agent", user_query_1)
                    st.success(res)
            else:
                st.warning("Barah-e-karam query enter karein.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="agent-card">', unsafe_allow_html=True)
        st.subheader("🚨 Emergency Response")
        st.write("PTZ camera alerts & crime response coordination.")
        user_query_2 = st.text_input("Query Emergency Agent:", key="q2")
        if st.button("Run Emergency Agent"):
            if user_query_2:
                with st.spinner("Processing emergency protocols..."):
                    res = run_agent_query("Emergency Response Agent", user_query_2)
                    st.success(res)
            else:
                st.warning("Barah-e-karam query enter karein.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="agent-card">', unsafe_allow_html=True)
        st.subheader("💻 System Health")
        st.write("Server logs, IoT sensors & admin dashboard health.")
        user_query_3 = st.text_input("Query Admin Agent:", key="q3")
        if st.button("Run Admin Agent"):
            if user_query_3:
                with st.spinner("Checking system metrics..."):
                    res = run_agent_query("System Health Agent", user_query_3)
                    st.success(res)
            else:
                st.warning("Barah-e-karam query enter karein.")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Quetta Safe City Infrastructure Specs")
    st.info("System integration: 200+ PTZ Cameras, 1000+ Fixed Cameras, 30+ ANPR Units.")

with tab3:
    st.subheader("About Quetta Safe Hub 3")
    st.write("Powered by Groq model `openai/gpt-oss-120b` and Streamlit.")
