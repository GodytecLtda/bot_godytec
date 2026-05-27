# Tasks - Spec 002: Auto Generated HTML Dashboard

## Objetivo

Criar um dashboard HTML gerado automaticamente por Python, usando os dados do CSV e os graficos ja existentes.

O dashboard final deve continuar sendo:

dashboard/clinic_leads_dashboard.html

Mas agora ele deve ser gerado por:

scripts/generate_html_dashboard.py

---

## Task 1 - Criar script generate_html_dashboard.py

Criar o arquivo:

scripts/generate_html_dashboard.py

O script deve:

- ler data/godytec_ghl_clinic_leads.csv;
- calcular KPIs automaticamente;
- montar o HTML como string;
- salvar o resultado em dashboard/clinic_leads_dashboard.html;
- criar a pasta dashboard caso ela nao exista.

Criterio de aceite:

- O arquivo scripts/generate_html_dashboard.py existe.
- O script executa sem erro.

---

## Task 2 - Calcular KPIs a partir do CSV

O script deve calcular:

- total de leads;
- leads ganhos;
- leads perdidos;
- leads abertos ou em nutricao;
- taxa de conversao;
- receita mensal potencial;
- receita mensal ganha;
- ticket medio estimado;
- lead score medio;
- probabilidade media de fechamento.

Criterio de aceite:

- Os KPIs do HTML nao devem estar fixos manualmente.
- Os valores devem ser calculados a partir do CSV.

---

## Task 3 - Usar graficos existentes

O dashboard deve exibir os graficos localizados em:

analysis/charts/leads_by_pipeline_stage.png
analysis/charts/leads_by_source.png
analysis/charts/revenue_by_pipeline_stage.png
analysis/charts/top_campaigns_by_leads.png
analysis/charts/lost_reasons.png

Criterio de aceite:

- Todos os graficos aparecem no HTML.
- Os caminhos relativos funcionam ao abrir o HTML localmente no navegador.

---

## Task 4 - Atualizar pipeline runner

Atualizar o arquivo:

scripts/run_analysis_pipeline.py

Para executar tambem:

scripts/generate_html_dashboard.py

A ordem deve ser:

1. scripts/analyze_clinic_leads.py
2. scripts/generate_clinic_leads_charts.py
3. scripts/generate_html_dashboard.py
4. validar todos os arquivos esperados.

Criterio de aceite:

- O comando python "scripts\run_analysis_pipeline.py" deve gerar relatorio, graficos e dashboard HTML.

---

## Task 5 - Validar saidas esperadas

Depois de rodar o pipeline, verificar se existem:

analysis/001-clinic-leads-funnel-summary.md
analysis/charts/leads_by_pipeline_stage.png
analysis/charts/leads_by_source.png
analysis/charts/revenue_by_pipeline_stage.png
analysis/charts/top_campaigns_by_leads.png
analysis/charts/lost_reasons.png
dashboard/clinic_leads_dashboard.html

Criterio de aceite:

- O pipeline deve falhar se algum arquivo esperado nao existir.
- O pipeline deve mostrar mensagem de sucesso se tudo estiver correto.

---

## Task 6 - Testar no navegador

Abrir:

dashboard/clinic_leads_dashboard.html

Conferir:

- titulo do dashboard;
- cards de KPI;
- resumo executivo;
- graficos;
- layout responsivo basico.

Criterio de aceite:

- O dashboard abre corretamente no navegador.
- Os valores exibidos batem com o dataset atual.

---

## Task 7 - Versionamento

Depois da implementacao e teste:

git status
git add
git commit
git push

Mensagem de commit sugerida:

Generate HTML dashboard from dataset

Criterio de aceite:

- O git status deve ficar limpo apos commit e push.
