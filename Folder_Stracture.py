from pathlib import Path

# Root project folder
ROOT = Path(r"C:\DrSuad3\Paper_2")

# Folder structure
folders = [
    "datasets/raw",
    "datasets/processed",
    "datasets/sampled",
    "datasets/feature_selected",

    "notebooks",

    "src/preprocessing",
    "src/models",
    "src/xai",
    "src/deployment",
    "src/evaluation",

    "models/trained",
    "models/tflite",
    "models/checkpoints",

    "results/figures",
    "results/tables",
    "results/logs",
    "results/reports",

    "paper/abstract",
    "paper/introduction",
    "paper/related_work",
    "paper/methodology",
    "paper/experiments",
    "paper/results_discussion",
    "paper/conclusion",
    "paper/references",

    "diagrams/architecture",
    "diagrams/workflow",
    "diagrams/xai_visualizations",

    "references/papers",
    "references/surveys",
    "references/notes",

    "presentations/proposal",
    "presentations/progress",
    "presentations/final_presentation",
]

# Create folders
for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)

# Create base files
base_files = [
    "README.md",
    "requirements.txt",
    "project_plan.md",
]

for file in base_files:
    (ROOT / file).touch(exist_ok=True)

# Create starter notebooks
starter_notebooks = [
    "01_dataset_exploration.ipynb",
    "02_data_preprocessing.ipynb",
    "03_feature_selection.ipynb",
    "04_baseline_models.ipynb",
    "05_tinyml_conversion.ipynb",
    "06_xai_analysis.ipynb",
    "07_resource_evaluation.ipynb",
    "08_final_experiments.ipynb",
]

for nb in starter_notebooks:
    (ROOT / "notebooks" / nb).touch(exist_ok=True)

print("Paper2 project structure created successfully!")