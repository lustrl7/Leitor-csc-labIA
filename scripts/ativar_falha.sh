#!/usr/bin/env bash
set -euo pipefail
# Execute na raiz do projeto, depois de publicar a branch main corrigida.
git switch main
git pull
git switch -c demonstracao-falha
cp demo/versao-com-falha/app/csv_service.py app/csv_service.py
cp demo/versao-com-falha/tests/test_csv_service.py tests/test_csv_service.py
git add app/csv_service.py tests/test_csv_service.py
git commit -m "test: reproduce zero-value CSV processing bug"
git push -u origin demonstracao-falha
