# Round 1B – Persona-Driven Document Intelligence
## Team Solution: UPI Fraud Detection Use Case

### 👤 Persona:
**Fraud Analyst at a FinTech Company**

### 🎯 Job-to-be-Done:
Identify the most effective machine learning algorithms, preprocessing methods, and evaluation techniques to build a real-time UPI fraud detection system.

---

## 🧠 Approach Overview

Our solution processes a collection of domain-specific PDFs and intelligently extracts the most relevant sections based on a given persona and task. It combines PDF parsing, lightweight embedding models, and semantic ranking to deliver focused insights, all within the required offline, CPU-only constraints.

---

## 🧱 System Architecture

1. **PDF Parsing**  
   We use `PyMuPDF` to extract text at the page level from each PDF. Each page is treated as a section with metadata (document name, page number, etc.).

2. **Persona-Task Embedding**  
   We form a semantic query from the persona and job-to-be-done. This query is embedded using `MiniLM` (via `sentence-transformers`) to ensure fast and memory-efficient offline inference.

3. **Section Embedding + Ranking**  
   All parsed page texts are embedded using the same MiniLM model. We calculate cosine similarity between the query and each page, then rank them globally across all documents.

4. **Top Section Extraction**  
   We select the top 5 highest scoring pages as `extracted_sections`, capturing document name, section title, and importance rank.

5. **Subsection Refinement**  
   From the same top pages, we extract 1–2 paragraphs of raw text to provide deeper insight into each section as part of the `subsection_analysis`.

6. **Output JSON**  
   All results are compiled into a single `challenge1b_output.json`, conforming exactly to the official schema.

---

## ⚙️ Technologies Used

- Python 3.9
- `PyMuPDF` for PDF parsing
- `sentence-transformers` (`all-MiniLM-L6-v2`)
- `torch` for embedding operations
- Docker (CPU-only, offline mode)
- Fully modular and generalizable codebase

---

## ✅ Constraints Handled

| Constraint                        | Compliance  |
|----------------------------------|-------------|
| Runs Offline (No Internet)       | ✅ Yes      |
| Model Size ≤ 1GB                 | ✅ ~80MB    |
| Runtime ≤ 60s for 3–5 PDFs       | ✅ ~10s      |
| CPU Only (amd64)                 | ✅ Yes      |
| Generic (no hardcoding)          | ✅ Yes      |

---

## 🧪 Evaluation

The output shows that our pipeline selects highly relevant sections including:
- Model comparisons (XGBoost, CatBoost, SVM)
- Preprocessing techniques (SMOTE, PCA)
- Real-time detection frameworks

Each section contributes toward the persona's task: building a robust fraud detection system.

---

## 🔚 Summary

This approach showcases how lightweight NLP can be used to make PDF collections semantically responsive to diverse users. It is scalable, accurate, and optimized for offline intelligence. Our solution generalizes well and can support future persona-task combinations across domains.
