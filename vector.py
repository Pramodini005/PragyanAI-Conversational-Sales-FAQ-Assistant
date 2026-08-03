# ---------------------------------------------------------------------------
# 2. Vector Store Indexer (Loads Excel FAQ + PDF Documents)
# ---------------------------------------------------------------------------
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = None

def load_documents_into_vectorstore(file_paths=None):
    global vectorstore
    docs = []

    # 1. Process UI file uploads (PDFs or Excel files)
    if file_paths:
        for file in file_paths:
            path = file.name if hasattr(file, 'name') else file
            if path.endswith('.pdf'):
                loader = PyPDFLoader(path)
                docs.extend(loader.load())
            elif path.endswith('.xlsx') or path.endswith('.xls'):
                excel_df = pd.read_excel(path)
                for _, row in excel_df.iterrows():
                    content = " | ".join([f"{col}: {val}" for col, val in row.items()])
                    docs.append(Document(page_content=content, metadata={"source": path}))

    # 2. Automatically load default Excel FAQ if present locally
    if os.path.exists("pragyan_faq_prices.xlsx"):
        excel_df = pd.read_excel("pragyan_faq_prices.xlsx")
        for _, row in excel_df.iterrows():
            content = " | ".join([f"{col}: {val}" for col, val in row.items()])
            docs.append(Document(page_content=content, metadata={"source": "pragyan_faq_prices.xlsx"}))

    # Fallback knowledge base if no files are loaded
    if not docs:
        docs = [
            Document(page_content="PragyanAI Program: 6 Months Offline Training + 12 Months Placement Drive. Led by Sateesh Ambesange."),
            Document(page_content="Founding Batch Fee: ₹50,000 initial training + ₹50,000 success fee post placement.")
        ]

    vectorstore = FAISS.from_documents(docs, embeddings)
    return f"✅ PragyanAI Knowledge Base updated successfully with {len(docs)} document chunks!"

# Build initial index
load_documents_into_vectorstore()
