import csv
import io
import pytest
from app.csv_service import CSVValidationError, process_csv

def rows_of(csv_text):
    return list(csv.DictReader(io.StringIO(csv_text)))

def test_processes_regular_record_and_calculates_fee():
    result = rows_of(process_csv("id,nome,email,valor\n1,Ana,ana@example.com,100\n"))
    assert len(result) == 1
    assert result[0]["valor_com_taxa"] == "110.00"

def test_preserves_zero_value_record():
    result = rows_of(process_csv("id,nome,email,valor\n2,Bruno,bruno@example.com,0\n"))
    assert len(result) == 1
    assert result[0]["id"] == "2"
    assert result[0]["valor_com_taxa"] == "0.00"

def test_rejects_missing_required_column():
    with pytest.raises(CSVValidationError, match="valor"):
        process_csv("id,nome,email\n1,Ana,ana@example.com\n")

def test_rejects_invalid_numeric_value():
    with pytest.raises(CSVValidationError, match="Valor inválido"):
        process_csv("id,nome,email,valor\n1,Ana,ana@example.com,abc\n")

def test_accepts_decimal_point():
    result = rows_of(process_csv("id,nome,email,valor\n3,Caio,caio@example.com,10.50\n"))
    assert result[0]["valor"] == "10.50"
    assert result[0]["valor_com_taxa"] == "11.55"
