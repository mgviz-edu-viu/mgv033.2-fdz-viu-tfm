RADME code
===========

// project
* [x] script to generate the project


// scripts

* [X] read metadata and create json
* [ ] read json and create db model
* [ ] read database excel sheet and 
  * [ ] add the exp_id to each purification table 
  * [ ] split into one csv file per purification
* [ ] read each purification sheet and load database
* [ ] read all experiments ids
  * for each experiment create a PDF report
* [ ] create sankey plot of the full purification ecosistem
* [ ] write the anual report of the service for protein purification

// workflows

* [ ] Snakemake wrapper for the pipeline

==========================================================================

DATA:
------

All the files 


==========================================================================

Normas
------

Environmental varialbes in config

working_directory:
data_dir:
software_base_dir:
temp_dir:
workflow_dir:


==========================================================================

Ideal Project structure  

```
project_name/
│
├── data/
│   ├── raw_data/
│   ├── processed_data/
│   └── annotations/
│
├── modules/
│   ├── module1/
│   │   ├── __init__.py
│   │   ├── module1_code.py
│   │   └── tests/
│   │       ├── test_module1.py
│   │       └── ...
│   ├── module2/
│   │   ├── __init__.py
│   │   ├── module2_code.py
│   │   └── tests/
│   │       ├── test_module2.py
│   │       └── ...
│   └── ...
│
├── scripts/
│   ├── preprocessing/
│   ├── analysis/
│   └── visualization/
│
├── tests/
│   ├── test_preprocessing/
│   ├── test_analysis/
│   └── test_visualization/
│
├── results/
│   ├── figures/
│   ├── tables/
│   └── reports/
│
└── documentation/
    ├── README.md
    ├── requirements.txt
    ├── notes.txt
    ├── changelog.txt
    └── docs/
```

==========================

Workflow
---------------

