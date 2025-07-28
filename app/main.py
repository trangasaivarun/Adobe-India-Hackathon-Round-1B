import os
import json
import time
from utils.pdf_parser import parse_pdf
from utils.embedder import Embedder
from utils.ranker import rank_sections
from utils.formatter import build_output

INPUT_DIR = "app/input"
INPUT_JSON = "test_input/challenge1b_input.json"
OUTPUT_PATH = "app/output/challenge1b_output.json"

def main():
    with open(INPUT_JSON, "r") as f:
        data = json.load(f)

    persona = data["persona"]["role"]
    job = data["job_to_be_done"]["task"]
    query = f"{persona}. {job}"

    embedder = Embedder()
    query_embed = embedder.encode([query])[0]

    all_sections = []
    document_titles = []

    for doc in data["documents"]:
        filename = doc["filename"]
        title = doc["title"]
        document_titles.append(filename)

        file_path = os.path.join(INPUT_DIR, filename)
        sections = parse_pdf(file_path)

        for section in sections:
            section["document"] = filename
            section["title"] = section.get("title", f"Page {section['page_number']}")
            all_sections.append(section)

    # Rank all sections together
    ranked = rank_sections(all_sections, query_embed, embedder)
    output = build_output(
        document_titles,
        persona,
        job,
        ranked
    )

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
