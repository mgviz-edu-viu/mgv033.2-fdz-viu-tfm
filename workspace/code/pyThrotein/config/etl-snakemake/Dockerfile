FROM snakemake/snakemake:v7.32.4

# current working directory
WORKDIR /workspaces/mgv033.2-fdz-viu-tfm/workspace/code/pyThrotein/scripts/workflows/

# Copy the file with the requirements to the /app directory.
COPY ./requirements.txt /opt/requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt

# Copy the ./src directory inside the /app directory.
COPY ../data/raw_data/TFM_database.xlsx /workspaces/mgv033.2-fdz-viu-tfm/workspace/code/pyThrotein/data/raw_data/TFM_database.xlsx

# command to run the uvicorn server.
CMD ["snakemake", "-s", "/workspaces/mgv033.2-fdz-viu-tfm/workspace/code/pyThrotein/scripts/workflows/Snakefile"]
