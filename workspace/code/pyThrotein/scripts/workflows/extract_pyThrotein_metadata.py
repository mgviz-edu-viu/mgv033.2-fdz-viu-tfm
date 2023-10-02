import pandas as pd
import json
import click

# Función para transformar values_limit en una lista o lista vacía
def transform_values_limit(value):
    print("# [INFO] transforming value limits")
    # this is now a try/except to being able to split the nan and also return 
    # only a [] if empty string or nan (converted to empty string with fillna())
    try:
        if value is None or value == '':
            return [""] 
        return str(value).split(',')
    except (TypeError, AttributeError):
        return [""]

# Función para procesar cada grupo y crear un JSON para cada uno
def process_group(group_data):
    print("# [INFO]  processing group")
    # use fillna() to avoinf to have "nan" in the json and the become a  ['nan'],
    #  makeing it '' we can end up with a [] in the value_limits
    group_json = group_data.fillna("").to_dict(orient='records')
    
    # Transformar values_limit en una lista o lista vacía
    for item in group_json:
        item['values_limit'] = transform_values_limit(item.get('values_limit'))
    
    return group_json

# Función para realizar la lectura del archivo Excel y generar el JSON
def generate_json_from_excel(excel_file_path, metadata_sheet_name):
    # Leer el archivo Excel en un DataFrame
    excel_data = pd.read_excel(excel_file_path, sheet_name=metadata_sheet_name)

    # Agrupar los datos por el factor de purificación (table_name)
    print("# [INFO]  grouping excel datq")
    grouped_data = excel_data.groupby('table_name')

    # Crear un diccionario para almacenar el JSON resultante
    result_json = {}

    # Iterar a través de cada grupo y crear un JSON para cada uno
    for group_name, group_data in grouped_data:
        # group_data only contains the indexes of the rows
        # .get_group() is needed to get the subtable for a group
        result_json[group_name] = process_group(grouped_data.get_group(group_name))

    return result_json

# Función para guardar el JSON en un archivo
def save_json_to_file(json_data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

@click.command()
@click.option('-d', '--debug', is_flag=True, help='Imprimir el JSON en la consola para depuración')
#@click.argument('excel_file_path', type=click.Path(exists=True), metavar='EXCEL_FILE_PATH', callback=lambda ctx, param, value: value or None)
@click.option('-i', '--input-file', type=click.Path(exists=True), help='Ruta al archivo Excel', metavar='EXCEL_FILE_PATH')
#@click.argument('output_file_path', type=click.Path(), metavar='OUTPUT_FILE_PATH', callback=lambda ctx, param, value: value or None)
@click.option('-o', '--output-file', type=click.Path(), help='Ruta al archivo de salida JSON', metavar='OUTPUT_FILE_PATH')
@click.option('--metadata-sheet-name', default='metadata', help='Nombre de la hoja de metadata')
def main(debug, input_file, output_file, metadata_sheet_name):

    excel_file_path = input_file
    output_file_path = output_file

    # Verificar si se proporciona el parámetro de entrada (excel_file_path)
    if not excel_file_path:
        click.echo("Debe proporcionar un archivo de entrada con -if, --input-file o como argumento.")
        return

    # Generar el JSON a partir del archivo Excel
    print("# [INFO]  generate_json_from_exce")
    result_json = generate_json_from_excel(excel_file_path, metadata_sheet_name)

    # Imprimir el JSON solo si se proporciona el parámetro de depuración
    if debug:
        click.echo(json.dumps(result_json, indent=4))

    # Verificar si se proporciona el parámetro de salida (output_file_path) y usarlo si está presente
    print("# [INFO] saving JSON")
    if output_file_path:
        save_json_to_file(result_json, output_file_path)
        click.echo(f"JSON guardado en: {output_file_path}")
    else:
        print("# [INFO] the output file has not been given. No JSON file created")

if __name__ == "__main__":
    main()