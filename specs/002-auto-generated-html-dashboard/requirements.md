# Spec 002 - Auto Generated HTML Dashboard

## Contexto

O projeto bot_godytec ja possui:

- dataset fake com leads B2B da Godytec;
- script de analise em Python;
- relatorio Markdown;
- graficos PNG;
- dashboard HTML manual;
- pipeline runner.

Atualmente o arquivo dashboard/clinic_leads_dashboard.html possui KPIs escritos manualmente.

Isso nao e ideal, porque se o dataset mudar, os numeros do dashboard HTML nao serao atualizados automaticamente.

## Objetivo

Criar um script Python que gere automaticamente o dashboard HTML a partir do CSV e dos graficos existentes.

O novo fluxo esperado e:

data/godytec_ghl_clinic_leads.csv
-> scripts/analyze_clinic_leads.py
-> scripts/generate_clinic_leads_charts.py
-> scripts/generate_html_dashboard.py
-> dashboard/clinic_leads_dashboard.html

## Arquivo a criar

Criar o script:

scripts/generate_html_dashboard.py

Esse script deve ler o CSV:

data/godytec_ghl_clinic_leads.csv

E gerar o arquivo:

dashboard/clinic_leads_dashboard.html

## Regras

1. O dashboard HTML deve ser gerado automaticamente.
2. Os KPIs nao devem ficar escritos manualmente no HTML.
3. O script deve calcular os KPIs diretamente do CSV.
4. O dashboard deve usar os graficos PNG existentes em analysis/charts.
5. O layout deve continuar simples, limpo e executivo.
6. O script deve criar a pasta dashboard se ela nao existir.
7. O script nao deve alterar o dataset.
8. O script nao deve alterar arquivos PBIP.
9. O script deve funcionar no Windows usando o ambiente virtual do projeto.

## KPIs obrigatorios

O dashboard HTML deve exibir:

- Total de leads
- Leads ganhos
- Leads perdidos
- Leads abertos ou em nutricao
- Taxa de conversao
- Receita mensal potencial
- Receita mensal ganha
- Ticket medio estimado
- Lead score medio
- Probabilidade media de fechamento

## Graficos obrigatorios

O dashboard HTML deve exibir os seguintes graficos:

- analysis/charts/leads_by_pipeline_stage.png
- analysis/charts/leads_by_source.png
- analysis/charts/revenue_by_pipeline_stage.png
- analysis/charts/top_campaigns_by_leads.png
- analysis/charts/lost_reasons.png

## Atualizacao do pipeline runner

Atualizar o arquivo:

scripts/run_analysis_pipeline.py

Para executar tambem:

scripts/generate_html_dashboard.py

A ordem correta deve ser:

1. analyze_clinic_leads.py
2. generate_clinic_leads_charts.py
3. generate_html_dashboard.py
4. validar saidas esperadas

## Saidas esperadas

Depois de rodar:

python "scripts\run_analysis_pipeline.py"

Devem existir:

- analysis/001-clinic-leads-funnel-summary.md
- analysis/charts/leads_by_pipeline_stage.png
- analysis/charts/leads_by_source.png
- analysis/charts/revenue_by_pipeline_stage.png
- analysis/charts/top_campaigns_by_leads.png
- analysis/charts/lost_reasons.png
- dashboard/clinic_leads_dashboard.html

## Criterios de aceite

A implementacao sera aceita se:

1. O script scripts/generate_html_dashboard.py existir.
2. O dashboard HTML for gerado automaticamente.
3. Os KPIs do HTML vierem do CSV.
4. O pipeline runner executar o novo script.
5. O comando python "scripts\run_analysis_pipeline.py" terminar com sucesso.
6. O dashboard abrir no navegador.
7. O git status ficar limpo apos commit.
