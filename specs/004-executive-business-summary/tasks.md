# Tasks - Spec 004: Executive Business Summary

## Objetivo

Criar um relatorio executivo de negocio para transformar as analises tecnicas do projeto em recomendacoes claras para tomada de decisao da Godytec.

O relatorio final deve ser:

analysis/004-executive-business-summary.md

---

## Task 1 - Criar script generate_executive_summary.py

Criar o arquivo:

scripts/generate_executive_summary.py

O script deve:

- ler data/godytec_ghl_clinic_leads.csv;
- calcular indicadores principais;
- identificar melhores e piores campanhas;
- gerar um relatorio Markdown executivo;
- criar a pasta analysis caso ela nao exista.

Criterio de aceite:

- O arquivo scripts/generate_executive_summary.py existe.
- O script executa sem erro.

---

## Task 2 - Calcular indicadores executivos

O script deve calcular:

- total de leads;
- leads ganhos;
- leads perdidos;
- leads abertos ou em nutricao;
- taxa de conversao geral;
- receita mensal potencial;
- receita mensal ganha;
- ticket medio;
- melhor campanha por ROI estimado;
- melhor campanha por receita ganha;
- melhor campanha por receita potencial;
- campanhas com menor ROI estimado.

Criterio de aceite:

- Todos os indicadores aparecem no relatorio.
- Os valores devem vir do CSV e dos calculos internos.

---

## Task 3 - Criar narrativa executiva

O relatorio deve conter as secoes:

1. Resumo executivo
2. Diagnostico do funil comercial
3. Receita potencial e receita ganha
4. Performance das campanhas
5. Campanhas recomendadas para investimento
6. Campanhas recomendadas para revisao
7. Riscos e pontos de atencao
8. Recomendacoes praticas para a Godytec
9. Proximos passos sugeridos

Criterio de aceite:

- O texto deve ser claro para uma pessoa de negocio.
- O relatorio nao deve parecer apenas uma saida tecnica de script.
- Deve conter interpretacao e recomendacoes.

---

## Task 4 - Gerar arquivo Markdown

Criar o arquivo:

analysis/004-executive-business-summary.md

Criterio de aceite:

- O arquivo existe.
- O arquivo esta em UTF-8.
- O arquivo pode ser aberto corretamente no VS Code.

---

## Task 5 - Atualizar pipeline runner

Atualizar:

scripts/run_analysis_pipeline.py

Para executar tambem:

scripts/generate_executive_summary.py

A ordem final deve ser:

1. scripts/analyze_clinic_leads.py
2. scripts/generate_clinic_leads_charts.py
3. scripts/generate_html_dashboard.py
4. scripts/analyze_campaign_roi.py
5. scripts/generate_executive_summary.py

Criterio de aceite:

- O comando python "scripts\run_analysis_pipeline.py" executa tudo com sucesso.
- O pipeline valida tambem o arquivo analysis/004-executive-business-summary.md.

---

## Task 6 - Garantir que arquivos fora de escopo nao sejam alterados

Nao alterar:

- data/godytec_ghl_clinic_leads.csv
- arquivos PBIP
- arquivos de dataset existente

Criterio de aceite:

- git status nao deve mostrar alteracoes em data/ ou arquivos PBIP.

---

## Task 7 - Validar implementacao

Depois de implementar, rodar:

python "scripts\run_analysis_pipeline.py"

Validar existencia de:

analysis/004-executive-business-summary.md

Criterio de aceite:

- Pipeline termina com sucesso.
- O relatorio executivo existe.
- O relatorio contem recomendacoes praticas.

---

## Task 8 - Versionamento

Depois da revisao:

git status
git add
git commit
git push

Mensagem de commit sugerida:

Add executive business summary

Criterio de aceite:

- O git status fica limpo apos commit e push.
