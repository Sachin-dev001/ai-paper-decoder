import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Paper Decoder",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background-color: #0E1117;
    color: white;
}

.main-title {
    font-size: 55px;
    font-weight: bold;
    color: white;
}

.sub-title {
    font-size: 20px;
    color: #A0A0A0;
    margin-bottom: 30px;
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
    color: #FFFFFF;
}

.result-box {
    background-color: #1E1E1E;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #2E2E2E;
    font-size: 17px;
    line-height: 1.8;
}

.creator-box {
    background-color: #161B22;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #30363D;
}

.tech-badge {
    display: inline-block;
    background-color: #21262D;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-size: 14px;
}

.stButton>button {
    width: 100%;
    height: 3.2em;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #6C63FF, #5A54E8);
    color: white;
    font-size: 18px;
    font-weight: bold;
}

.stDownloadButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    background-color: #262730;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ⚙️ Configuration")

    paper_input = st.selectbox(
        "📄 Select Research Paper",
        
         ["Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "GPT-3: Language Models are Few-Shot Learners",
            "GPT-4 Technical Report",
            "LLaMA: Open and Efficient Foundation Language Models",
            "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
            "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
            "LoRA: Low-Rank Adaptation of Large Language Models",
            "Diffusion Models Beat GANs on Image Synthesis",
            "Denoising Diffusion Probabilistic Models"
]           
            
        
    )

    style_input = st.selectbox(
        "🧠 Explanation Style",
        [
            "Beginner-Friendly",
            "Technical",
            "Code-Oriented",
            "Mathematical"
        ]
    )

    length_input = st.selectbox(
        "📚 Explanation Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

    temperature = st.slider(
        "🎨 Creativity Level",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1
    )

    st.markdown("---")

    st.success("✅ Project Status: Active")
    st.info("📌 Version: v1.0")

    st.markdown("---")

    # =========================================================
    # DEVELOPER CARD
    # =========================================================

    st.markdown("""
    <div class="creator-box">

    <h2>👨‍💻 Developer</h2>

    <h3>Sachin Sharma</h3>

    <p>
    GenAI Developer
    </p>

    <p>
    Building AI-powered applications using LangChain, Gemini API, and Python.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🚀 Tech Stack")

    st.markdown("""
    <div class="tech-badge">Python</div>
    <div class="tech-badge">LangChain</div>
    <div class="tech-badge">Gemini API</div>
    <div class="tech-badge">Streamlit</div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🌐 Connect With Me")

    st.markdown("""
    🔗 [LinkedIn](https://www.linkedin.com/in/sachin-sharma-659ab53b6)
    """)

# =========================================================
# MAIN TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🧠 AI Paper Decoder</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Decode complex AI research papers into easy-to-understand insights using Gemini + LangChain.</div>',
    unsafe_allow_html=True
)

# =========================================================
# MODEL
# =========================================================

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=temperature
)

# =========================================================
# LOAD PROMPT
# =========================================================

template = load_prompt("template.json")

# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button("🚀 Decode Research Paper"):

    with st.spinner("🧠 AI is analyzing the research paper..."):

        try:

            chain = template | model

            result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            })

            time.sleep(2)

            st.success("✅ Explanation Generated Successfully!")

            # =========================================================
            # DIFFICULTY INDICATOR
            # =========================================================

            difficulty_map = {
                
                "Attention Is All You Need": "🔴 Advanced",
                "BERT: Pre-training of Deep Bidirectional Transformers": "🟠 Intermediate",
                "GPT-3: Language Models are Few-Shot Learners": "🔴 Advanced",
                "GPT-4 Technical Report": "🔴 Advanced",
                "LLaMA: Open and Efficient Foundation Language Models": "🟠 Intermediate",
                "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks": "🟠 Intermediate",
                "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models": "🟡 Beginner-Friendly",
                "LoRA: Low-Rank Adaptation of Large Language Models": "🟠 Intermediate",
                "Diffusion Models Beat GANs on Image Synthesis": "🔴 Advanced",
                "Denoising Diffusion Probabilistic Models": "🔴 Advanced"

            }

            st.markdown(
                f"### 📊 Paper Difficulty: {difficulty_map.get(paper_input)}"
            )

            # =========================================================
            # RESULT SECTION
            # =========================================================

            st.markdown(
                '<div class="section-title">📖 AI Explanation</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="result-box">
                {result.content}
                </div>
                """,
                unsafe_allow_html=True
            )

            # =========================================================
            # DOWNLOAD BUTTON
            # =========================================================

            st.download_button(
                label="📥 Download Explanation",
                data=result.content,
                file_name="ai_paper_explanation.txt",
                mime="text/plain"
            )

            # =========================================================
            # EXPANDABLE PAPER INFO
            # =========================================================

            with st.expander("📌 Research Paper Details"):

                st.write(f"### 📄 Selected Paper")
                st.write(paper_input)

                st.write(f"### 🧠 Explanation Style")
                st.write(style_input)

                st.write(f"### 📚 Explanation Length")
                st.write(length_input)

                st.write(f"### 🎨 Creativity Level")
                st.write(temperature)

            # =========================================================
            # WHY THIS PAPER MATTERS
            # =========================================================

            with st.expander("🚀 Why This Paper Matters"):

                st.info("""
                These research papers transformed modern AI systems.

                Understanding them helps you learn:
                - Transformers
                - Large Language Models
                - NLP
                - Diffusion Models
                - Modern GenAI Systems
                """)

        except Exception as e:

            st.error(f"❌ Error: {e}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div style='text-align: center; padding: 20px;'>

<h3>👨‍💻 Developed By Sachin Sharma</h3>

<p>
GenAI Developer • AI Enthusiast • Building Modern AI Applications
</p>

<p>
Built using LangChain + Gemini API + Streamlit
</p>

</div>
""", unsafe_allow_html=True)