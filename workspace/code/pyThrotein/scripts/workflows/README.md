# pyThrotein/scripts/workflows

This directory contains files related to pyThrotein/scripts/workflows.
You can add your own content to this README.

## Structure

This script contains the snake file and config file for the pripeline

Also contains the scripts used in the pipeline.

Initially it will contain the documentation for the pipelines. Later it would be moved to Documentation folder of the proyect.



## How to run


```
# Print the DAG
snakemake -p --dag | dot -Tsvg > dag-full.svg
```

```
# dry run
snakemake -np
```

## Workflow steps

1. Rule for Reading Excel Metadata and Creating JSON:
   - Name: `r1_extract_metadata`
   - Input: `Excel file`
   - Output: `metadata.json`
   - Script: `extract_pyThrotein_metadata.py`

2. Rule for Creating DB Model from JSON Metadata:
   - Name: `r2_create_db_model`
   - Input: `metadata.json`
   - Output: `db_model.sql`, `init_db.sh`
   - Script: `create_db_model.py`

3. Rule for Initializing SQLite Database from DB Model:
   - Name: `r3_ initialize_db`
   - Input: `db_model.sql`
   - Output: `{data}/processed_data/logs/db-initialization.DONE`
      - <also> SQLite database file (e.g., `protein_purification.db`)
   - Script: `bash init_db.sh`

4. Rule for Reading Excel Sheet with Purification Data:
   - Name: `r4_read_and_split_purification_excel`
   - Input: `Excel file`, `{data}/processed_data/logs/db-initialization.DONE` 
   - Output: `/processed_data/purification_method_{{method}}.csv` ## one csv file for each purification method
   - Script: `split_purification_excel.py`

5. Rule for Loading Purification Data into the Database:
   - Name: `r5_load_data_into_db`
   - Input: `{data}/processed_data/purification_method_{{method}}.csv`# Purification CSV files by method
   - Output: `{data}/processed_data/logs/status_db_load-{{method}}.DONE` # Log files by method
   - Script: `load_data_into_db.py`

6. Rule for checking the db is fully loaded:
   - Name: `r6_check_db`
   - Input: `{data}/processed_data/logs/status_db_load-{{method}}.DONE` # Protein experiment IDs
   - Output: `{data}/processed_data/logs/test_db.OK`
   - Script: `check_db.py`

7. Rule for Creating PDF Reports for full Protein Purification Experiment:
   - Name: `r_7_1_gathered_analysis_report`
   - Input: `{data}/processed_data/logs/test_db.OK` # Database and other data
   - Output: `{data}/report-{iso_date}.pdf"`
   - Script: `create_pythrotein_general_report.py`

8.1. get list of experiments in a file
   - Name: `r8_1_get_experiment_list`
   - Input: `{data}/processed_data/logs/test_db.OK`
   - Output: `{data}/processed_data/experiments_list-{iso_date}.txt` 
   - Script: `get_experiment_list.py`

8.2 . Rule for writing pdf for each experiment
   - Name: `r8_2_generate_report_by_experiment`
   - input: `{data}/processed_data/experiments_list-{iso_date}.txt`
   - output: `{report_dir}/logs/rule8-experiment_pdf_reports.DONE`
   - script: `create_pythrotein_report.py`