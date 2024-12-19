
# 📄 Chat with PDF Interface 📄

Welcome to the **Chat with PDF** project! This application allows users to upload a PDF file, extract text, and query the content using Natural Language Processing (NLP) techniques. 

---

## 🚀 Features 🚀
- 📂 **Upload PDFs**: Easily upload your PDF files.
- 🔍 **Text Extraction**: Extract text content from PDFs with precision.
- 💬 **Query Interface**: Interact with your PDF data via a user-friendly query interface.
- ⚡ **FAISS Vector Store**: Fast and efficient text searching.
- 🤖 **Pre-trained NLP Models**: Uses `sentence-transformers` for semantic similarity queries.

---

## 📂 Project Structure 📂
```plaintext
Chat_With_PDF/
├── templates/
│   ├── index.html      # Frontend for the web app
├── uploads/            # Uploaded PDF files (generated dynamically)
├── main.py             # Core Python backend
```

---

## 💻 Setup Instructions 💻
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Chat-With-PDF.git
   cd Chat-With-PDF
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Access the application in your browser at: `http://127.0.0.1:5000/`.

---

## 🌟 Screenshots 🌟
![Screenshot (1527)](https://github.com/user-attachments/assets/1102ca63-5ffe-4c04-b283-3b158f39cecc)

---
 
## 🛠️ Technologies Used 🛠️
- **Backend**: Flask
- **NLP**: LangChain, HuggingFace Transformers
- **Frontend**: HTML, CSS
- **PDF Processing**: pdfplumber
- **Vector Store**: FAISS

---

## 📷 Demonstration 📷
Here's how the application works:

1. **Step 1**: Upload a PDF file.
2. **Step 2**: Extract and chunk text for efficient querying.
3. **Step 3**: Enter a query and get relevant text snippets.

---

## 🧱 Future Enhancements 🧱
- 🔄 Real-time updates to the query results.
- 🌐 Deployment to platforms like AWS/GCP.
- 🧩 Adding support for multi-format documents (e.g., DOCX).

---

## 👥 Contributors
- **Your Name** - Yalagandula Baby Ramya
---
