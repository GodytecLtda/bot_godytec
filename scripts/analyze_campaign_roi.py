from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path("data/godytec_ghl_clinic_leads.csv")
OUTPUT_PATH = Path("analysis/003-campaign-roi-analysis.md")
CHARTS_DIR = Path("analysis/charts/campaign_roi")
DEFAULT_CAMPAIGN_COST_BRL = 1500

CAMPAIGN_COSTS_BRL = {
    "Dental Growth BR - Facebook": 3500,
    "Implantes Agenda Cheia - Google": 4200,
    "Consultorios Premium - LinkedIn": 3000,
    "WhatsApp Automation Sprint": 1800,
    "Webinar Agenda Cheia": 1500,
    "Prospeccao Sudeste": 1200,
    "Reativacao Consultorios": 1000,
}


def money(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def percent(value: float) -> str:
    return f"{value * 100:.2f}%"


def calculate_campaign_metrics(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for campaign_name, campaign_df in df.groupby("campaign_name"):
        total_leads = len(campaign_df)
        won_leads = int((campaign_df["lead_status"] == "Won").sum())
        lost_leads = int((campaign_df["lead_status"] == "Lost").sum())
        open_leads = int(campaign_df["lead_status"].isin(["Open", "Nurturing"]).sum())
        cost = CAMPAIGN_COSTS_BRL.get(campaign_name, DEFAULT_CAMPAIGN_COST_BRL)
        potential_revenue = float(campaign_df["estimated_monthly_value_brl"].sum())
        won_revenue = float(
            campaign_df.loc[
                campaign_df["lead_status"] == "Won", "estimated_monthly_value_brl"
            ].sum()
        )
        conversion_rate = won_leads / total_leads if total_leads else 0
        estimated_roi = (won_revenue - cost) / cost if cost else 0

        rows.append(
            {
                "campaign_name": campaign_name,
                "total_leads": total_leads,
                "won_leads": won_leads,
                "lost_leads": lost_leads,
                "open_leads": open_leads,
                "potential_monthly_revenue_brl": potential_revenue,
                "won_monthly_revenue_brl": won_revenue,
                "average_ticket_brl": float(
                    campaign_df["estimated_monthly_value_brl"].mean()
                ),
                "average_lead_score": float(campaign_df["lead_score"].mean()),
                "average_probability_to_close": float(
                    campaign_df["probability_to_close"].mean()
                ),
                "simulated_campaign_cost_brl": cost,
                "conversion_rate": conversion_rate,
                "estimated_roi": estimated_roi,
            }
        )

    return pd.DataFrame(rows)


def save_bar_chart(
    series: pd.Series,
    title: str,
    xlabel: str,
    output_file: Path,
    value_format: str = "number",
) -> None:
    chart_data = series.sort_values(ascending=True)

    plt.figure(figsize=(11, 6))
    ax = chart_data.plot(kind="barh")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Campanha")

    for container in ax.containers:
        labels = []
        for value in container.datavalues:
            if value_format == "money":
                labels.append(money(float(value)))
            elif value_format == "percent":
                labels.append(percent(float(value)))
            else:
                labels.append(f"{value:.0f}")
        ax.bar_label(container, labels=labels, padding=3, fontsize=8)

    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()


def generate_charts(metrics: pd.DataFrame) -> None:
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    indexed = metrics.set_index("campaign_name")

    save_bar_chart(
        indexed["total_leads"],
        "Volume de Leads por Campanha",
        "Quantidade de Leads",
        CHARTS_DIR / "campaign_leads_count.png",
    )
    save_bar_chart(
        indexed["potential_monthly_revenue_brl"],
        "Receita Mensal Potencial por Campanha",
        "Receita Mensal Potencial BRL",
        CHARTS_DIR / "campaign_potential_revenue.png",
        "money",
    )
    save_bar_chart(
        indexed["won_monthly_revenue_brl"],
        "Receita Mensal Ganha por Campanha",
        "Receita Mensal Ganha BRL",
        CHARTS_DIR / "campaign_won_revenue.png",
        "money",
    )
    save_bar_chart(
        indexed["conversion_rate"],
        "Taxa de Conversao por Campanha",
        "Taxa de Conversao",
        CHARTS_DIR / "campaign_conversion_rate.png",
        "percent",
    )
    save_bar_chart(
        indexed["estimated_roi"],
        "ROI Estimado por Campanha",
        "ROI Estimado",
        CHARTS_DIR / "campaign_estimated_roi.png",
        "percent",
    )


def ranking_table(metrics: pd.DataFrame, sort_column: str) -> list[str]:
    lines = [
        "| Posicao | Campanha | Leads | Ganhos | Receita Ganha | Receita Potencial | Conversao | ROI Estimado |",
        "|---:|---|---:|---:|---:|---:|---:|---:|",
    ]

    ranking = metrics.sort_values(sort_column, ascending=False).reset_index(drop=True)
    for index, row in ranking.iterrows():
        lines.append(
            "| "
            f"{index + 1} | "
            f"{row['campaign_name']} | "
            f"{int(row['total_leads'])} | "
            f"{int(row['won_leads'])} | "
            f"{money(float(row['won_monthly_revenue_brl']))} | "
            f"{money(float(row['potential_monthly_revenue_brl']))} | "
            f"{percent(float(row['conversion_rate']))} | "
            f"{percent(float(row['estimated_roi']))} |"
        )

    return lines


def build_report(metrics: pd.DataFrame) -> str:
    best_roi = metrics.sort_values("estimated_roi", ascending=False).iloc[0]
    best_won_revenue = metrics.sort_values(
        "won_monthly_revenue_brl", ascending=False
    ).iloc[0]
    best_potential = metrics.sort_values(
        "potential_monthly_revenue_brl", ascending=False
    ).iloc[0]
    best_volume = metrics.sort_values("total_leads", ascending=False).iloc[0]
    review_candidates = metrics.sort_values(
        ["estimated_roi", "conversion_rate", "won_monthly_revenue_brl"],
        ascending=[True, True, True],
    ).head(3)

    lines = []
    lines.append("# Analise 003 - ROI Simulado por Campanha")
    lines.append("")
    lines.append("## Resumo executivo")
    lines.append("")
    lines.append(
        f"A analise avaliou {len(metrics)} campanhas a partir do dataset {DATA_PATH}."
    )
    lines.append(
        f"A campanha com maior ROI estimado foi {best_roi['campaign_name']}, com ROI de {percent(float(best_roi['estimated_roi']))}."
    )
    lines.append(
        f"A maior receita mensal ganha veio de {best_won_revenue['campaign_name']}, com {money(float(best_won_revenue['won_monthly_revenue_brl']))}."
    )
    lines.append(
        f"A maior receita mensal potencial esta em {best_potential['campaign_name']}, com {money(float(best_potential['potential_monthly_revenue_brl']))}."
    )
    lines.append("")
    lines.append("## Metricas por campanha")
    lines.append("")
    lines.append(
        "| Campanha | Leads | Ganhos | Perdidos | Abertos/Nutricao | Custo Simulado | Ticket Medio | Score Medio | Prob. Media | Conversao | Receita Potencial | Receita Ganha | ROI Estimado |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for _, row in metrics.sort_values("campaign_name").iterrows():
        lines.append(
            "| "
            f"{row['campaign_name']} | "
            f"{int(row['total_leads'])} | "
            f"{int(row['won_leads'])} | "
            f"{int(row['lost_leads'])} | "
            f"{int(row['open_leads'])} | "
            f"{money(float(row['simulated_campaign_cost_brl']))} | "
            f"{money(float(row['average_ticket_brl']))} | "
            f"{float(row['average_lead_score']):.2f} | "
            f"{percent(float(row['average_probability_to_close']))} | "
            f"{percent(float(row['conversion_rate']))} | "
            f"{money(float(row['potential_monthly_revenue_brl']))} | "
            f"{money(float(row['won_monthly_revenue_brl']))} | "
            f"{percent(float(row['estimated_roi']))} |"
        )
    lines.append("")

    sections = [
        ("## Ranking por ROI estimado", "estimated_roi"),
        ("## Ranking por receita ganha", "won_monthly_revenue_brl"),
        ("## Ranking por receita potencial", "potential_monthly_revenue_brl"),
        ("## Ranking por volume de leads", "total_leads"),
    ]

    for title, sort_column in sections:
        lines.append(title)
        lines.append("")
        lines.extend(ranking_table(metrics, sort_column))
        lines.append("")

    lines.append("## Interpretacao das melhores campanhas")
    lines.append("")
    lines.append(
        f"- {best_roi['campaign_name']} lidera em ROI estimado, indicando melhor eficiencia entre receita ganha e custo simulado."
    )
    lines.append(
        f"- {best_won_revenue['campaign_name']} lidera em receita mensal ganha e deve ser observada como referencia de conversao comercial."
    )
    lines.append(
        f"- {best_potential['campaign_name']} concentra a maior receita potencial e pode justificar priorizacao do time comercial."
    )
    lines.append(
        f"- {best_volume['campaign_name']} gera o maior volume de leads, mas deve ser comparada com conversao e ROI antes de receber mais investimento."
    )
    lines.append("")
    lines.append("## Campanhas que precisam de revisao")
    lines.append("")
    for _, row in review_candidates.iterrows():
        lines.append(
            f"- {row['campaign_name']}: ROI estimado de {percent(float(row['estimated_roi']))}, "
            f"conversao de {percent(float(row['conversion_rate']))} e receita ganha de {money(float(row['won_monthly_revenue_brl']))}."
        )
    lines.append("")
    lines.append(
        "Campanhas com ROI negativo, baixa conversao ou baixa receita ganha devem ser revisadas antes de novos investimentos."
    )
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    metrics = calculate_campaign_metrics(df)
    generate_charts(metrics)
    OUTPUT_PATH.write_text(build_report(metrics), encoding="utf-8")

    print(f"Campaign ROI report generated: {OUTPUT_PATH}")
    print("Campaign ROI charts generated:")
    for chart_path in sorted(CHARTS_DIR.glob("*.png")):
        print(f"- {chart_path}")


if __name__ == "__main__":
    main()
