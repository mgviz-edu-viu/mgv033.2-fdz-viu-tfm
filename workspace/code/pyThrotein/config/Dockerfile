FROM snakemake/snakemake:v7.32.4

# current working directory
WORKDIR /app

# Copy the file with the requirements to the /app directory.
COPY ./requirements.txt /app/requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the ./src directory inside the /app directory.
COPY ./src /app/src

# command to run the uvicorn server.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
