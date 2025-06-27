FROM python:3.10-slim

WORKDIR /usr/app

RUN pip install -U pip
RUN pip install pipenv

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY macros/ macros/
COPY models/ models/
COPY seeds/ seeds/
COPY snapshots/ snapshots/
COPY tests/ tests/

COPY [ "dbt_project.yml", "packages.yml", "package-lock.yml", "./"]

RUN dbt deps

ENTRYPOINT [ "dbt" ]