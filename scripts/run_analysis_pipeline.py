import subprocess
import sys
from pathlib import Path


REQUIRED_OUTPUTS = [
    Path("analysis/001-clinic-leads-funnel-summary.md"),
    Path("analysis/charts/leads_by_pipeline_stage.png"),
    Path("analysis/charts/leads_by_source.png"),
    Path("analysis/charts/revenue_by_pipeline_stage.png"),
    Path("analysis/charts/top_campaigns_by_leads.png"),
    Path("analysis/charts/lost_reasons.png"),
    Path("dashboard/clinic_leads_dashboard.html"),
    Path("analysis/003-campaign-roi-analysis.md"),
    Path("analysis/charts/campaign_roi/campaign_leads_count.png"),
    Path("analysis/charts/campaign_roi/campaign_potential_revenue.png"),
    Path("analysis/charts/campaign_roi/campaign_won_revenue.png"),
    Path("analysis/charts/campaign_roi/campaign_conversion_rate.png"),
    Path("analysis/charts/campaign_roi/campaign_estimated_roi.png"),
]


def run_command(command: list[str]) -> None:
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, check=False)

    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}")


def validate_outputs() -> None:
    missing_files = [path for path in REQUIRED_OUTPUTS if not path.exists()]

    if missing_files:
        print("Missing output files:")
        for path in missing_files:
            print(f"- {path}")
        raise FileNotFoundError("Analysis pipeline did not generate all expected files.")

    print("All expected output files were generated successfully.")


def main() -> None:
    print("Starting clinic leads analysis pipeline...")

    run_command([sys.executable, "scripts/analyze_clinic_leads.py"])
    run_command([sys.executable, "scripts/generate_clinic_leads_charts.py"])
    run_command([sys.executable, "scripts/generate_html_dashboard.py"])
    run_command([sys.executable, "scripts/analyze_campaign_roi.py"])

    validate_outputs()

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
