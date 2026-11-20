from pathlib import Path
def clean_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)
    return "\n".join(clean_lines)
corpus_dir = Path("corpus")
cleaned_dir = Path("cleaned")
cleaned_dir.mkdir(exist_ok=True)
files = list(corpus_dir.glob("*.txt"))
documents = []
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    text = clean_text(text)
    
    if text == "":
        print("Пропущен пустой файл:", file_path.name)
        continue
        
    documents.append({
        "source": file_path.name,
        "text": text
    })
    
    output_path = cleaned_dir / file_path.name
    output_path.write_text(text, encoding="utf-8")
print(f"\nДокументов: {len(documents)}")
total_chars = 0
for document in documents:
    chars = len(document["text"])
    total_chars += chars
    print(f"{document['source']} — {chars} символов")
    if chars < 50:
        print(f"  ! Предупреждение: короткий документ ({document['source']})")
print(f"\nВсего символов: {total_chars}")