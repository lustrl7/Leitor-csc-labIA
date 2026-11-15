from flask import Flask, jsonify, request, Response
from app.csv_service import CSVValidationError, process_csv

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/upload")
def upload_csv():
    uploaded = request.files.get("file")
    if uploaded is None or uploaded.filename == "":
        return jsonify({"error": "Envie um arquivo no campo 'file'."}), 400
    if not uploaded.filename.lower().endswith(".csv"):
        return jsonify({"error": "Formato inválido. Envie um arquivo CSV."}), 400
    try:
        content = uploaded.read().decode("utf-8-sig")
        processed = process_csv(content)
    except UnicodeDecodeError:
        return jsonify({"error": "O arquivo deve estar codificado em UTF-8."}), 400
    except CSVValidationError as exc:
        return jsonify({"error": str(exc)}), 422
    return Response(processed, mimetype="text/csv",
                    headers={"Content-Disposition": 'attachment; filename="arquivo_processado.csv"'})
