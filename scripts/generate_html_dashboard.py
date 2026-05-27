from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/godytec_ghl_clinic_leads.csv")
DASHBOARD_DIR = Path("dashboard")
OUTPUT_PATH = DASHBOARD_DIR / "clinic_leads_dashboard.html"

CHARTS = [
    (
        "Leads por Etapa do Pipeline",
        "../analysis/charts/leads_by_pipeline_stage.png",
        "Leads por etapa do pipeline",
    ),
    (
        "Leads por Origem",
        "../analysis/charts/leads_by_source.png",
        "Leads por origem",
    ),
    (
        "Receita Potencial por Etapa",
        "../analysis/charts/revenue_by_pipeline_stage.png",
        "Receita potencial por etapa",
    ),
    (
        "Top Campanhas por Leads",
        "../analysis/charts/top_campaigns_by_leads.png",
        "Top campanhas por leads",
    ),
    (
        "Motivos de Perda",
        "../analysis/charts/lost_reasons.png",
        "Motivos de perda",
    ),
]


def money(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def percent(value: float) -> str:
    return f"{value:.2f}%"


def calculate_kpis(df: pd.DataFrame) -> dict[str, str]:
    total_leads = len(df)
    won_leads = int((df["lead_status"] == "Won").sum())
    lost_leads = int((df["lead_status"] == "Lost").sum())
    open_leads = int(df["lead_status"].isin(["Open", "Nurturing"]).sum())

    conversion_rate = (won_leads / total_leads) * 100 if total_leads else 0
    potential_revenue = float(df["estimated_monthly_value_brl"].sum())
    won_revenue = float(
        df.loc[df["lead_status"] == "Won", "estimated_monthly_value_brl"].sum()
    )
    avg_ticket = float(df["estimated_monthly_value_brl"].mean())
    avg_score = float(df["lead_score"].mean())
    avg_probability = float(df["probability_to_close"].mean() * 100)

    return {
        "Total de Leads": f"{total_leads}",
        "Leads Ganhos": f"{won_leads}",
        "Leads Perdidos": f"{lost_leads}",
        "Leads Abertos ou em Nutricao": f"{open_leads}",
        "Taxa de Conversao": percent(conversion_rate),
        "Receita Mensal Potencial": money(potential_revenue),
        "Receita Mensal Ganha": money(won_revenue),
        "Ticket Medio Estimado": money(avg_ticket),
        "Lead Score Medio": f"{avg_score:.2f}",
        "Probabilidade Media de Fechamento": percent(avg_probability),
    }


def build_kpi_cards(kpis: dict[str, str]) -> str:
    cards = []
    for label, value in kpis.items():
        cards.append(
            f"""      <div class="card">
        <h3>{label}</h3>
        <div class="value">{value}</div>
      </div>"""
        )
    return "\n\n".join(cards)


def build_chart_cards() -> str:
    cards = []
    for title, source, alt in CHARTS:
        cards.append(
            f"""      <div class="chart-card">
        <h2>{title}</h2>
        <img src="{source}" alt="{alt}">
      </div>"""
        )
    return "\n\n".join(cards)


def build_html(kpis: dict[str, str]) -> str:
    kpi_cards = build_kpi_cards(kpis)
    chart_cards = build_chart_cards()

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Godytec - Dashboard de Leads Odontologicos</title>
  <style>
    body {{
      margin: 0;
      font-family: Arial, sans-serif;
      background: #f4f6f8;
      color: #1f2937;
    }}

    header {{
      background: #111827;
      color: white;
      padding: 32px;
      text-align: center;
    }}

    header h1 {{
      margin: 0;
      font-size: 32px;
    }}

    header p {{
      margin-top: 8px;
      color: #d1d5db;
    }}

    main {{
      max-width: 1200px;
      margin: 32px auto;
      padding: 0 24px;
    }}

    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 20px;
      margin-bottom: 32px;
    }}

    .card {{
      background: white;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }}

    .card h3 {{
      margin: 0;
      font-size: 13px;
      color: #6b7280;
      text-transform: uppercase;
    }}

    .card .value {{
      margin-top: 10px;
      font-size: 26px;
      font-weight: bold;
      color: #111827;
    }}

    .section-title {{
      font-size: 24px;
      margin: 32px 0 16px;
    }}

    .chart-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
    }}

    .chart-card {{
      background: white;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }}

    .chart-card h2 {{
      margin-top: 0;
      font-size: 20px;
    }}

    .chart-card img {{
      width: 100%;
      border-radius: 8px;
      border: 1px solid #e5e7eb;
    }}

    .insight {{
      background: #ecfdf5;
      border-left: 6px solid #10b981;
      padding: 18px;
      border-radius: 8px;
      margin-bottom: 32px;
    }}

    footer {{
      text-align: center;
      padding: 24px;
      color: #6b7280;
      font-size: 14px;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Godytec - Dashboard de Leads Odontologicos</h1>
    <p>Analise simulada do funil B2B para captacao de consultorios odontologicos via GoHighLevel</p>
  </header>

  <main>
    <section class="kpi-grid">
{kpi_cards}
    </section>

    <section class="insight">
      <strong>Resumo executivo:</strong>
      A Godytec possui {kpis["Total de Leads"]} leads B2B simulados no funil comercial para consultorios odontologicos.
      A taxa de conversao atual e {kpis["Taxa de Conversao"]}, com {kpis["Leads Ganhos"]} leads ganhos
      e {kpis["Receita Mensal Ganha"]} em receita mensal ganha.
    </section>

    <h2 class="section-title">Graficos do Funil Comercial</h2>

    <section class="chart-grid">
{chart_cards}
    </section>
  </main>

  <footer>
    Projeto de analise de dados criado no VS Code com Python, pandas, matplotlib, Git e GitHub.
  </footer>
</body>
</html>
"""


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    kpis = calculate_kpis(df)
    OUTPUT_PATH.write_text(build_html(kpis), encoding="utf-8")

    print(f"HTML dashboard generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
