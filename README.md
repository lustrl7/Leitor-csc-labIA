# DevOps + GenAI: CSV Pipeline Diagnostics

Aplicação Flask para receber CSV, validar o contrato, calcular `valor_com_taxa` (acréscimo de 10%) e devolver o arquivo processado. Pytest valida o comportamento; GitLab CI executa os testes; o agente GenAI pode analisar logs de falha.

## Executar
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
pytest -v
```

## API
```bash
flask --app app.api run --debug
curl -X POST http://127.0.0.1:5000/upload -F "file=@sample_data/entrada.csv" -o arquivo_processado.csv
```

## GenAI
Configure `OPENAI_API_KEY` localmente ou em Settings > CI/CD > Variables no GitLab. Opcional: `OPENAI_MODEL` (padrão `gpt-4.1-mini`). O agente recomenda correções, mas não altera código.

## Demonstração da falha
A versão inicial está em `demo/versao-com-falha`. Ela contém o defeito intencional de descartar linhas com valor zero. O teste `test_preserves_zero_value_record` reprova. O código na raiz é a versão corrigida e deve aprovar os cinco testes. Os testes do serviço CSV usam apenas Pytest e biblioteca padrão; a API Flask também está incluída para demonstração de upload/download.

## Segurança
Não envie CSVs com dados pessoais/confidenciais a serviços externos sem autorização. A API didática não possui autenticação nem limites de tamanho e não deve ser exposta publicamente sem proteções adicionais. Valide toda recomendação da IA.


## Guia de publicação e demonstração

Consulte [`GUIA_PUBLICACAO.md`](GUIA_PUBLICACAO.md) para os passos de publicação no GitLab, configuração opcional da chave OpenAI, teste da API e reprodução controlada da falha.
