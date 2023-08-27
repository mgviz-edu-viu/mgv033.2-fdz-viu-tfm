#########################
# Initialization script #
#########################

# Create the folders for the analysis
#
#
#
# project_name/
# │
# ├── DATA/
# │   ├── raw_data/
# │   ├── processed_data/
# │   ├── annotations/
# │   └── references/
# │
# ├── scripts/
# │   ├── preprocessing/
# │   ├── analysis/
# │   └── visualization/
# |
# ├── tests/
# │
# ├── results/
# │   ├── figures/
# │   ├── tables/
# │   └── reports/
# │
# └── documentation/
#     ├── README.md
#     ├── requirements.txt
#     ├── notes.txt
#     ├── changelog.txt
#     └── docs/

echo "[note] Creating the initial directories and README files"
mkdir -p \
  DATA/raw_data \
  DATA/processed_data \
  DATA/annotations \
  DATA/references \
  \
  scripts/preprocessing \
  scripts/analysis \
  scripts/analysis/workflow \
  scripts/visualization \
  scripts/scratch \
  \
  tests\
  \
  results/figures \
  results/tables \
  results/reports \
  \
  documentation/docs \
  \
  _scratch \

touch \
  DATA/README.md \
  scripts/README.md \
  results/README.MD \
  documentation/README.md \
  tests/README.md \
  \
  DATA/raw_data/README.md \
  DATA/processed_data/README.md \
  DATA/annotations/README.md \
  DATA/references/README.md \
  \
  scripts/preprocessing/README.md \
  scripts/analysis/README.md \
  scripts/analysis/workflow/README.md \
  scripts/visualization/README.md \
  scripts/scratch/README.md \
  \
  tests/README.md \
  \
  results/figures/README.md \
  results/tables/README.md \
  results/reports/README.md \
  \
  documentation/docs/README.md \
  \
  _scratch/README.md \


tree -F
