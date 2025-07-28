import fitz  # PyMuPDF

def parse_pdf(file_path):
    doc = fitz.open(file_path)
    sections = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            sections.append({
                "page_number": i + 1,
                "text": text,
                "title": f"Page {i+1}"
            })
    return sections
