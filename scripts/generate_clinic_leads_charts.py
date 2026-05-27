from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path("data/godytec_ghl_clinic_leads.csv")
CHARTS_DIR = Path("analysis/charts")


def save_bar_chart(series: pd.Series, title: str, xlabel: str, ylabel: str, output_file: Path) -> None:
    plt.figure(figsize=(10, 6))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    pipeline_order = [
        "New Lead",
        "Contacted",
        "Qualified",
        "Meeting Scheduled",
        "Proposal Sent",
        "Negotiation",
        "Won",
        "Lost",
    ]

    leads_by_stage = df["pipeline_stage"].value_counts().reindex(pipeline_order).fillna(0)
    save_bar_chart(
        leads_by_stage,
        "Leads por Etapa do Pipeline",
        "Etapa do Pipeline",
        "Quantidade de Leads",
        CHARTS_DIR / "leads_by_pipeline_stage.png",
    )

    leads_by_source = df["lead_source"].value_counts()
    save_bar_chart(
        leads_by_source,
        "Leads por Origem",
        "Origem do Lead",
        "Quantidade de Leads",
        CHARTS_DIR / "leads_by_source.png",
    )

    revenue_by_stage = (
        df.groupby("pipeline_stage")["estimated_monthly_value_brl"]
        .sum()
        .reindex(pipeline_order)
        .fillna(0)
    )
    save_bar_chart(
        revenue_by_stage,
        "Receita Potencial por Etapa do Pipeline",
        "Etapa do Pipeline",
        "Receita Potencial Mensal BRL",
        CHARTS_DIR / "revenue_by_pipeline_stage.png",
    )

    top_campaigns = df["campaign_name"].value_counts().head(10)
    save_bar_chart(
        top_campaigns,
        "Top 10 Campanhas por Leads",
        "Campanha",
        "Quantidade de Leads",
        CHARTS_DIR / "top_campaigns_by_leads.png",
    )

    lost_reasons = df.loc[df["lead_status"] == "Lost", "lost_reason"].value_counts()
    save_bar_chart(
        lost_reasons,
        "Motivos de Perda",
        "Motivo de Perda",
        "Quantidade de Leads",
        CHARTS_DIR / "lost_reasons.png",
    )

    print("Charts generated:")
    for chart_path in sorted(CHARTS_DIR.glob("*.png")):
        print(f"- {chart_path}")


if __name__ == "__main__":
    main()
