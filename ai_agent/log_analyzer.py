import os
import sys
from pathlib import Path

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("logs/pytest.log")
    if not path.exists():
        print(f"[WARN] Log não encontrado: {path}")
        return 0
    log_text = path.read_text(encoding="utf-8", errors="replace")
    if not os.getenv("OPENAI_API_KEY"):
        print("[INFO] OPENAI_API_KEY não configurada; log disponível para análise manual.")
        return 0
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        result = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            instructions="Analise logs de testes Python. Identifique evidências, causa provável, correção mínima e testes de regressão. Não altere o código.",
            input="Analise o log de CI do processamento CSV:\\n" + log_text[-15000:]
        )
        print(result.output_text)
    except Exception as exc:
        print(f"[WARN] Análise IA indisponível: {type(exc).__name__}: {exc}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
