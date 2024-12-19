from flask import Flask, request, render_template
from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
import pdfplumber
import os

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    extracted_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text.append(text)
    if not extracted_text:
        print("Error: No text found in the PDF.")
    return "\n".join(extracted_text)

# Function to split text into chunks
def split_text_into_chunks(text, chunk_size=1000, overlap=200):
    splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)

# Create LangChain Document objects
def create_documents(chunks):
    return [Document(page_content=chunk) for chunk in chunks]

# Initialize embeddings
def initialize_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1")

# Create FAISS vector store
def create_vector_store(documents, embeddings):
    return FAISS.from_documents(documents, embeddings)

# Initialize variables
vectorstore = None

@app.route("/", methods=["GET", "POST"])
def index():
    global vectorstore
    results = []

    if request.method == "POST":
        # Step 1: Handle File Upload
        if "file" in request.files:
            file = request.files["file"]
            if file.filename.endswith(".pdf"):
                pdf_path = os.path.join("uploads", file.filename)
                os.makedirs("uploads", exist_ok=True)
                file.save(pdf_path)

                # Step 2: Extract, Chunk, and Store
                pdf_text = extract_text_from_pdf(pdf_path)
                if pdf_text.strip():
                    chunks = split_text_into_chunks(pdf_text)
                    documents = create_documents(chunks)
                    embeddings = initialize_embeddings()
                    vectorstore = create_vector_store(documents, embeddings)
                else:
                    return render_template("index.html", results=["Error: No text found in the PDF."])

        # Step 3: Handle Query
        query = request.form.get("query")
        if query and vectorstore:
            retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})
            results = retriever.get_relevant_documents(query)

            # Debugging: Print retrieved results
            print(f"Query: {query}")
            if results:
                for idx, result in enumerate(results, start=1):
                    print(f"Result {idx}: {result.page_content[:200]}")  # Print first 200 characters
            else:
                print("No relevant documents found.")

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
