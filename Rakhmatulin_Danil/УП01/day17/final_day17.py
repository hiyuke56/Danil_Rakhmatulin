from pathlib import Path
def clean_line(line):
    line = line.replace("\u00a0", " ")
    line = line.replace("\t", " ")
    line = " ".join(line.split())
    return line
def normalize_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        line = clean_line(line)
        if line == "":
            continue
        if line not in clean_lines:
            clean_lines.append(line)
    return "\n".join(clean_lines)
source_dir = Path("cleaned")
normalized_dir = Path("normalized")
normalized_dir.mkdir(exist_ok=True)
files = list(source_dir.glob("*.txt"))
total_before = 0
total_after = 0
print("Начинаем нормализацию корпуса...\n")
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)
    before = len(text)
    after = len(normalized)
    total_before += before
    total_after += after
    if after == 0:
        print(f"ВНИМАНИЕ: Документ {file_path.name} стал пустым после очистки!")
    output_path = normalized_dir / file_path.name
    output_path.write_text(normalized, encoding="utf-8")
    print(f"Файл: {file_path.name}")
    print(f"  До: {before} символов")
    print(f"  После: {after} символов")
print("\n--- Общая сводка ---")
print(f"Общий объём до: {total_before} символов")
print(f"Общий объём после: {total_after} символов")
if total_before > 0:
    percent = (total_before - total_after) / total_before * 100
    print(f"Сокращение корпуса: {round(percent, 1)}%")