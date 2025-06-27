FROM apache/airflow:3.0.2-python3.10

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.2/constraints-3.10.txt"

ENTRYPOINT [ "airflow" ]