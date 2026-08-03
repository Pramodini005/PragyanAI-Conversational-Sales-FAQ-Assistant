import pandas as pd

faq_data = {
    "Category": [
        "Program Overview", "Program Structure", "Program Structure",
        "Pricing & Fees", "Pricing & Fees", "Curriculum & Skills",
        "Curriculum & Skills", "Evaluation & Projects", "Career & Placement",
        "Leadership & Contact"
    ],
    "Question": [
        "What is the total duration and structure of the PragyanAI program?",
        "What happens in Phase 1 (First 6 Months)?",
        "What happens in Phase 2 (12 Months)?",
        "What is the fee structure for the Founding Batch?",
        "What is the salary potential after completing the program?",
        "What modules are covered in Months 1-3 (Foundational Core)?",
        "What modules are covered in Months 4-6 (Advanced Frontier)?",
        "How are students evaluated during the 6-month offline training?",
        "What career tracks or roles are unlocked?",
        "Who leads PragyanAI and how can I contact them?"
    ],
    "Answer": [
        "The PragyanAI AI GenAI program is an 18-month journey comprising 6 Months of Fully Offline Training followed by a 12-Month Internship & Placement Drive.",
        "Phase 1 (6 Months) consists of intensive offline training with half-day classroom sessions, half-day hands-on labs, real-time projects, monthly hackathons, and technical seminars.",
        "Phase 2 (12 Months) includes an extended internship, live client assignments, technical mock interviews, resume building, and startup/product development exposure.",
        "Founding Batch (First 100 students): Initial Training Fee is ₹50,000 + Success Fee of ₹50,000 after placement (Total ₹1,00,000, discounted from standard ₹1,50,000).",
        "Target packages: AI Engineer (₹6–₹15 LPA), GenAI Engineer (₹8–₹18 LPA), and Agentic AI Engineer (₹10–₹25 LPA).",
        "Month 1: Python Full Stack & Analytics. Month 2: Data Science & BI Analytics. Month 3: Machine Learning Frameworks (AutoML, Streamlit deployment).",
        "Month 4: Deep Learning & Computer Vision (CNNs, PyTorch, YOLO). Month 5: NLP & Generative AI (LLMs, RAG, LangChain, Fine-tuning). Month 6: Agentic AI (CrewAI, AutoGen, Multi-Agent Systems, MCP).",
        "Students participate in 1 Technical Seminar per skill (evaluated out of 100 marks) and 1 Skill-wise 48-Hour Hackathon with cash prizes (₹5,000 winner, ₹3,000 runner-up).",
        "7 Multi-Track Pathways: Data Analyst, Data Scientist & ML, AI Engineer, GenAI Engineer, Agentic AI Engineer, Product/MVP Engineer, and Software Engineer.",
        "Led by Sateesh Ambesange (Co-Founder, NITK alumnus, 25+ years IT exp). Phone: +91-9741007422 | Email: sateesh.ambesange@pragyanai.com / pragyan.ai.school@gmail.com"
    ]
}

df = pd.DataFrame(faq_data)
df.to_excel("pragyan_faq_prices.xlsx", index=False)
print("✅ Created 'pragyan_faq_prices.xlsx' with PragyanAI presentation data!")
import os
import pandas as pd
import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq
