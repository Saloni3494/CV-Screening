import os
import re
import csv
import fitz  # PyMuPDF
import spacy
import unicodedata
from tqdm import tqdm

# Load spaCy model, can use other models like "en_core_web_md" for better accuracy
nlp = spacy.load("en_core_web_sm")

# Step 1: Extract text from PDF
def extract_text_from_pdf(file_path):
    try:
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

# Step 2: Clean and normalize the text
def clean_text(text):
    text = unicodedata.normalize("NFKD", text)  # Remove artifacts like ï¼​
    text = re.sub(r'\s+', ' ', text)           # Collapse all whitespace
    text = re.sub(r'\.([A-Za-z])', r'. \1', text)  # Ensure space after periods
    return text.strip()

# Step 3: Extract sections using keyword-based slicing
def extract_sections(text, keywords):
    text_lower = text.lower()
    section_indices = {}
    
    for kw in keywords:
        index = text_lower.find(kw.lower())
        if index != -1:
            section_indices[kw.lower()] = index
    
    if not section_indices:
        return {}
    
    sorted_sections = sorted(section_indices.items(), key=lambda x: x[1])
    result = {}
    
    for i, (section, start_idx) in enumerate(sorted_sections):
        end_idx = sorted_sections[i + 1][1] if i + 1 < len(sorted_sections) else len(text)
        result[section] = text[start_idx:end_idx].strip()
    
    return result

# Step 4: Named Entity Recognition with spaCy
def extract_named_entities(text):
    doc = nlp(text)
    return "; ".join([f"{ent.text} ({ent.label_})" for ent in doc.ents])

# Step 5: Process all PDFs and write to CSV
def process_and_save_csv(pdf_folder, output_csv):
    keywords = ["Summary", "Education", "Experience", "Skills", "Interests"]
    all_data = []

    for file in tqdm(os.listdir(pdf_folder)):
        if not file.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(pdf_folder, file)
        print(f"\nProcessing: {file}")
        raw_text = extract_text_from_pdf(file_path)

        if len(raw_text.strip()) < 50:
            print(f"[{file}] - Very short content, possibly empty or corrupt.")
            continue

        cleaned_text = clean_text(raw_text)
        print(f"[{file}] Extracted Text Preview:\n{cleaned_text[:300]}...\n")

        # Extract the first non-empty line as title
        first_line_title = ""
        for line in raw_text.splitlines():
            line = line.strip()
            if line:
                first_line_title = line
                break

        sections = extract_sections(cleaned_text, keywords)
        entities = extract_named_entities(cleaned_text)

        # Print extracted sections for debug
        for key in ["education", "experience", "skills"]:
            print(f"{key.title()} Section:\n{sections.get(key, '')[:300]}...\n")

        all_data.append([
            file,
            first_line_title,
            cleaned_text[:1000],  # Preview first 1000 chars
            sections.get("education", ""),
            sections.get("experience", ""),
            sections.get("skills", ""),
            entities
        ])

    # Write to CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Filename", "Title", "Full Text (Preview)", "Education", "Experience", "Skills", "Named Entities"])
        writer.writerows(all_data)

# === USAGE ===
pdf_folder = "cvs"  # Make sure this folder contains your PDFs
output_csv = "processed_cvs.csv"

process_and_save_csv(pdf_folder, output_csv)
