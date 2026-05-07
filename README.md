# Chat-with-pdf

This is a simple RAG system which uses google gemini api to answer questions from your uploaded pdf.
this script takes your pdf file path and your question as inputs.

---
## what this does and how it works

your question will be split into words and will be compared to chunks of the pdf and the most matched chunk will be chosen and given gemini along with your question. we will get a response which is relevent to the pdf and answer to your question.

---
## Tools used
- Python
- Google gemini api
- requests
- python-dotenv
- pymupdf

---
## how to run it

**1.clone the repository**
```
git clone https://github.com/cs24btech11025/chat-with-pdf
cd chat-with-pdf
```
**2.install dependencies**
```
pip install pymupdf requests python-dotenv
```
**3.get api-key**

Go to [aistudio.google.com](https://aistudio.google.com)
->get api key
->copy it

**create a new .env file**

write
```
GEMINI_API_KEY="your-api-key"
```
**run it!**
```
python chat.py
```
---
## what i learned

- extracting text from pdf using fitz
- chunking text
- choosing chunk to send based on common words
- calling ai api
- debugging edge cases where there are no common words

---
