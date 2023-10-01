setup a venv
```
python -m venv name_of_environment
```

- pip install datasets\
https://pypi.org/project/datasets/ 
 
- pip install langchain\
https://pypi.org/project/langchain/

- pip install "cassio>=0.1.0"\
https://pypi.org/project/cassio/    

- pip install openai\
https://pypi.org/project/openai/

- pip install tiktoken\
https://pypi.org/project/tiktoken/

- install all dependencies in one command\
pip install datasets langchain openai tiktoken "cassio>=0.1.0" python-dotenv

pip install psycopg2-binary pgvector

docker run --name pgvector -e POSTGRES_PASSWORD=testing -p 5432:5432 ankane/pgvector


get models from existing db

python manage.py inspectdb > models.py



SELECT * FROM langchain_pg_embedding
WHERE uuid='7fea1dce-1d4f-430f-9a34-c56392f696a5'