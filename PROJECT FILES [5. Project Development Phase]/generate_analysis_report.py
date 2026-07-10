from pathlib import Path
import base64
import io
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "Crop_recommendation.csv"
OUTPUT_PATH = ROOT / "analysis_report.html"


def fig_to_base64(fig):
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", dpi=150, bbox_inches="tight")
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def make_plot_section(title, figure):
    return f"""
    <section>
      <h2>{title}</h2>
      <img src="data:image/png;base64,{fig_to_base64(figure)}" alt="{title}" />
    </section>
    """


def build_report():
    sns.set_theme(style="whitegrid")
    df = pd.read_csv(DATA_PATH)

    overview_html = f"""
    <div class="card">
      <h2>Dataset Overview</h2>
      <p><strong>Rows:</strong> {df.shape[0]} &nbsp; <strong>Columns:</strong> {df.shape[1]}</p>
      <p><strong>Missing values:</strong> {int(df.isnull().sum().sum())}</p>
      <p><strong>Duplicate rows:</strong> {int(df.duplicated().sum())}</p>
    </div>
    """

    head_html = df.head(10).to_html(index=False, classes="dataframe")
    tail_html = df.tail(10).to_html(index=False, classes="dataframe")
    describe_html = df.describe().round(2).to_html(classes="dataframe")
    nulls_html = df.isnull().sum().to_frame(name="count").to_html(classes="dataframe")

    # Histogram section
    columns = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    hist_fig, axes = plt.subplots(3, 3, figsize=(15, 10))
    axes = axes.flatten()
    for ax, col in zip(axes, columns):
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(col)
    for ax in axes[len(columns):]:
        ax.axis("off")
    hist_fig.tight_layout()

    # Scatter section
    scatter_fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    axes = axes.flatten()
    for ax, feature in zip(axes, columns):
        sns.scatterplot(x=df[feature], y=df["label"], ax=ax)
        ax.set_title(f"{feature} vs Crop")
        ax.set_xlabel(feature)
        ax.set_ylabel("Crop")
    for ax in axes[len(columns):]:
        ax.axis("off")
    scatter_fig.tight_layout()

    # Correlation heatmap
    corr_fig, ax = plt.subplots(figsize=(10, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    ax.set_title("Correlation Heatmap")
    corr_fig.tight_layout()

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Crop Recommendation Analysis Report</title>
      <style>
        body {{ font-family: Arial, sans-serif; margin: 24px; background: #f7f9fc; color: #222; }}
        h1, h2 {{ color: #123; }}
        .card {{ background: white; padding: 16px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 20px; }}
        img {{ width: 100%; max-width: 1000px; height: auto; display: block; margin: 12px 0 24px; border: 1px solid #ddd; border-radius: 6px; background: white; }}
        .dataframe {{ border-collapse: collapse; width: 100%; margin-bottom: 16px; }}
        .dataframe th, .dataframe td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        .dataframe th {{ background: #eef3f8; }}
      </style>
    </head>
    <body>
      <h1>Crop Recommendation Analysis Report</h1>
      {overview_html}

      <div class="card">
        <h2>First 10 Rows</h2>
        {head_html}
      </div>

      <div class="card">
        <h2>Last 10 Rows</h2>
        {tail_html}
      </div>

      <div class="card">
        <h2>Dataset Summary</h2>
        {describe_html}
      </div>

      <div class="card">
        <h2>Missing Values</h2>
        {nulls_html}
      </div>

      {make_plot_section('Feature Distributions', hist_fig)}
      {make_plot_section('Feature vs Crop Label', scatter_fig)}
      {make_plot_section('Correlation Heatmap', corr_fig)}
    </body>
    </html>
    """

    OUTPUT_PATH.write_text(html, encoding="utf-8")
    plt.close("all")


if __name__ == "__main__":
    build_report()
    print(f"Report generated at {OUTPUT_PATH}")
