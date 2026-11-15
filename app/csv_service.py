import csv
import io

REQUIRED_COLUMNS = ("id", "nome", "email", "valor")

class CSVValidationError(ValueError):
    pass

def process_csv(content: str) -> str:
    reader = csv.DictReader(io.StringIO(content))
    if reader.fieldnames is None:
        raise CSVValidationError("CSV vazio ou sem cabeçalho.")
    missing = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
    if missing:
        raise CSVValidationError(f"Colunas obrigatórias ausentes: {', '.join(missing)}")
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=list(REQUIRED_COLUMNS) + ["valor_com_taxa"])
    writer.writeheader()
    for line_number, row in enumerate(reader, start=2):
        try:
            amount = float(row["valor"].replace(",", "."))
        except (AttributeError, ValueError):
            raise CSVValidationError(f"Valor inválido na linha {line_number}: {row.get('valor')!r}")
        # CORREÇÃO: valores zero também são registros válidos.
        writer.writerow({
            "id": row["id"], "nome": row["nome"], "email": row["email"],
            "valor": f"{amount:.2f}", "valor_com_taxa": f"{amount * 1.10:.2f}"
        })
    return output.getvalue()
