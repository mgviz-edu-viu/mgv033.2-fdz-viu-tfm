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
   - Name: `Extract_metadata`
   - Input: `Excel file`
   - Output: `metadata.json`
   - Script: `extract_pyThrotein_metadata.py`

2. Rule for Creating DB Model from JSON Metadata:
   - Name: `create_db_model`
   - Input: `metadata.json`
   - Output: `db_model.sql`, `init_db.sh`
   - Script: `create_db_model.py`

3. Rule for Initializing SQLite Database from DB Model:
   - Name: `initialize_sqlite_db`
   - Input: `db_model.sql`
   - Output: `logs/db-initialization.DONE`
      - <also> SQLite database file (e.g., `protein_purification.db`)
   - Script: `bash init_db.sh`

4. Rule for Reading Excel Sheet with Purification Data:
   - Name: `read_purification_excel`
   - Input: Excel file
   - Output: Multiple CSV files (one for each purification method)
   - Script: `read_purification_excel.py`

5. Rule for Loading Purification Data into the Database:
   - Name: `load_data_into_db`
   - Input: Purification CSV files
   - Output: Log files (e.g., `"loaded_data_for_{purification_method}-{iso-date}.log"`)
   - Script: `load_data_into_db.py`

6. Rule for Creating PDF Reports for Each Protein Purification Experiment:
   - Name: `create_pdf_reports`
   - Input: Protein experiment IDs
   - Output: PDF reports (one for each experiment)
   - Script: `create_pdf_reports.py`

7. Rule for Creating Sankey Plot of the Purification Ecosystem:
   - Name: `create_sankey_plot`
   - Input: Database and other data
   - Output: Sankey plot image file (e.g., `sankey_plot.png`)
   - Script: `create_sankey_plot.py`

8. Rule for Writing the Annual Report:
   - Name: `write_annual_report`
   - Input: Database and other data
   - Output: Annual report document (e.g., `annual_report.pdf` or `annual_report.docx`)
   - Script: `write_annual_report.py`
