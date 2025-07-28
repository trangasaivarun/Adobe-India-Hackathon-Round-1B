import time

def build_output(documents, persona, job, ranked_sections):
    metadata = {
        "input_documents": documents,
        "persona": persona,
        "job_to_be_done": job,
        "processing_timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }

    extracted_sections = []
    subsection_analysis = []

    for rank, (sec, _) in enumerate(ranked_sections, 1):
        extracted_sections.append({
            "document": sec["document"],
            "section_title": sec["title"],
            "importance_rank": rank,
            "page_number": sec["page_number"]
        })
        subsection_analysis.append({
            "document": sec["document"],
            "refined_text": sec["text"][:2000],  # limit to 2000 chars
            "page_number": sec["page_number"]
        })

    return {
        "metadata": metadata,
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
