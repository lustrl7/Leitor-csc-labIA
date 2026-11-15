As saídas abaixo foram capturadas por execuções locais do Pytest.
- initial_failure.log: versão defeituosa, com falha esperada no teste de preservação de valor zero.
- final_success.log: versão corrigida, com todos os testes aprovados.
Reproduza a falha: `cd demo/versao-com-falha && python -m pytest -v tests/test_csv_service.py`
Reproduza o sucesso: `python -m pytest -v tests/test_csv_service.py` na raiz.
