import json
from typing import List
import click

# Define a mapping of data types to SQLite-compatible data types
SQLITE_TYPE_MAP = {
    "int": "INTEGER",
    "str": "TEXT",
    "enum": "TEXT",
    "float": "REAL",
}

# Define a function to generate the SQL script for a single table
def generate_sql_script_for_table(table_name, metadata_entries):
    sql_script = f"-- Table: {table_name}\n"
    sql_script += f"CREATE TABLE IF NOT EXISTS {table_name} (\n"

    for entry in metadata_entries:
        variable_name = entry["variable_name"]
        data_type = entry["type"]
        comment = entry["comments"]

        nullability = ''
        if variable_name in ["exp_id", "id"]:
            nullability = "NOT NULL"
            
        # Map data type to SQLite-compatible data type
        sqlite_data_type = SQLITE_TYPE_MAP.get(data_type, "TEXT")

        # Handle enum types and values
        if data_type == "enum":
            enum_values = ", ".join(f"'{value}'" for value in entry["values_limit"])
            column_definition = f"    {variable_name} {sqlite_data_type} CHECK({variable_name} IN ({enum_values})) {nullability}, -- {comment}\n"
        else:
            column_definition = f"    {variable_name} {sqlite_data_type} {nullability}, -- {comment}\n"
        ## column_definition = f"    {variable_name} {sqlite_data_type} -- {comment}\n"
        sql_script += column_definition

    primary_key = f"    PRIMARY KEY ( exp_id, id)\n"
    sql_script += primary_key
    sql_script += ");\n\n"
    return sql_script

# Define a function to generate the SQL script
def generate_sql_script(metadata: dict, output_filename: str):
    with open(output_filename, "w") as sql_file:
        for table_name, entries in metadata.items():
            print(f"# [INFO] generating te sql model for {table_name}")
            table_sql = generate_sql_script_for_table(table_name, entries)
            sql_file.write(table_sql)

    print(f"SQL script has been generated in {output_filename}")

# Define a function to generate the Bash script to load SQL into SQLite
def generate_bash_script(sql_filename: str, db_filename: str, output_filename: str):
    print(f"# [INFO] creating script {output_filename} for loading model to db {db_filename}")
    with open(output_filename, "w") as bash_script:
        bash_script.write(f"sqlite3 {db_filename} < {sql_filename}\n")

    print(f"Bash script to load SQL into SQLite has been generated in {output_filename}")

@click.command()
@click.option("--input", help="Path to the JSON metadata file", type=click.Path(exists=True))
@click.option("--output-sql", help="Path to the output SQL script file", default="create_tables.sql", type=str)
@click.option("--output-bash", help="Path to the output Bash script file", default="initialize_sqlite.sh", type=str)
@click.option("--db-path", help="Path to the db", default="../../data/processed_data/protein_data.db", type=str)
def main(input, output_sql, output_bash, db_path):
    # Read JSON metadata
    with open(input, "r") as json_file:
        metadata = json.load(json_file)

    # Generate the SQL script
    generate_sql_script(metadata, output_sql)

    # Generate the Bash script to load SQL into SQLite
    generate_bash_script(output_sql, db_path, output_bash)

if __name__ == "__main__":
    main()
