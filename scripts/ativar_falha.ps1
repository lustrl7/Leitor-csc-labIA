# Execute na raiz do projeto, depois de publicar a branch main corrigida.
$ErrorActionPreference = "Stop"
git switch main
git pull
git switch -c demonstracao-falha
Copy-Item demo/versao-com-falha/app/csv_service.py app/csv_service.py -Force
Copy-Item demo/versao-com-falha/tests/test_csv_service.py tests/test_csv_service.py -Force
git add app/csv_service.py tests/test_csv_service.py
git commit -m "test: reproduce zero-value CSV processing bug"
git push -u origin demonstracao-falha
