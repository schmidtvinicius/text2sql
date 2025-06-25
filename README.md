# text2sql
A repository containing the text2sql experiments carried out for my Research Internship at Radboud University. The pre-computed results can be found in the [text2sql_results folder](./text2sql_results/)

## Running experiments
Make sure your [`config.ini` file](config.ini) is populated with valid fields for both the Azure OpenAI API and the database. Be aware that if you run the [experiments notebook](./text2sql_experiments.ipynb), it will overwrite the results saved in [text2sql_results folder](./text2sql_results/), which will impact the [analysis notebook](./text2sql_analysis.ipynb)

### Azure OpenAI
In the [`config.ini` file](config.ini), insert your API key and endpoint, so that the code for the experiments can connect to it:

```ini
[AZURE]
api_key=
api_version=2024-08-01-preview
azure_endpoint=
azure_deployment=o1-mini
model=o1-mini
```

### Database
In our experiments, we used a docker container to simulate the vulnerabilities database, but as long as you have a MariaDB/MySQL instance running to which you can connect, the experiments should work. In any case, make sure to fill in the values in the [`config.ini` file](config.ini):

```ini
[DB]
user=
password=
host=
database=
```

If you decide to use our docker container, make sure to create a `.env` file with the following fields:

```env
ROOT_PASSWORD=
MYSQL_ROOT_PASSWORD=
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

Then, run the following command before running the experiments/analysis:

```sh
docker-compose up -d
```