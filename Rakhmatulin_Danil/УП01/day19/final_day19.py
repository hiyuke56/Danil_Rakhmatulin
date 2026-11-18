from pathlib import Path
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
chunks_dir = Path("chunks")
chunks = []
if chunks_dir.exists():
    files = list(chunks_dir.glob("*.txt"))
    for file_path in files[:10]:
        text = file_path.read_text(encoding="utf-8")
        chunks.append({
            "source": file_path.name,
            "chunk_id": 0,
            "text": text
        })
else:
    print("Папка chunks не найдена. Используем тестовые данные.")
    chunks = [
        {"source": "python.txt", "chunk_id": 0, "text": "Списки Python создаются через квадратные скобки."},
        {"source": "git.txt", "chunk_id": 0, "text": "git commit сохраняет изменения в истории."},
        {"source": "pandas.txt", "chunk_id": 0, "text": "DataFrame используется для табличных данных."}
    ]
texts = [chunk["text"] for chunk in chunks]
chunk_embeddings = model.encode(texts)
print("Система готова. Задайте 3 вопроса.")
for i in range(1, 4):
    query = input(f"Введите вопрос {i}: ").strip()
    if not query:
        continue
    query_embedding = model.encode(query)
    scores = model.similarity(query_embedding, chunk_embeddings)[0].tolist()
    best_score = max(scores)
    best_index = scores.index(best_score)
    best_chunk = chunks[best_index]
    print(f"Источник: {best_chunk['source']}")
    print(f"Чанк: {best_chunk['chunk_id']}")
    print(f"Текст: {best_chunk['text']}")
    print(f"Сходство: {round(best_score, 4)}\n")