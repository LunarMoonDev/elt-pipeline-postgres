# elt-pipeline-postgres
This toy project uses dbt for ELT and Airflow for orchestration, runs on infrastructure managed via Docker and Compose, and includes bash scripts detailed in the README for easy execution.


## Global Variables

- **LOCAL_TAG**: The current date in `YYYY-MM-DD` format, used for tagging images.
- **LOCAL_IMAGE_NAME**: The Docker image name for the dbt project, including the date tag.

## Targets

### `init`
Initializes the database environment.
```sh
make init
```
*Runs `scripts/setup-database-init.sh`.*

---

### `set_database`
Boots up the database server.
```sh
make set_database
```
*Runs `scripts/boot_database.sh`.*

---

### `set_dbt_image`
Builds the Docker image for the dbt project.
```sh
make set_dbt_image
```
*Runs `scripts/create-docker-image.sh`.*

---

### `set_airflow`
Boots up the Airflow environment, passing the `LOCAL_IMAGE_NAME` as an environment variable.
```sh
make set_airflow
```
*Runs `scripts/setup-airflow.sh` with `LOCAL_IMAGE_NAME` set.*

---

### `stop_servers`
Stops all running servers.
```sh
make stop_servers
```
*Runs `scripts/stop-servers.sh`.*

---

## Usage

Run any of the above targets with `make <target>`.  
For example, to build the dbt Docker image:
```sh
make set_dbt_image
```

## Notes

- Ensure you have GNU Make and Bash installed.
- The scripts referenced in the Makefile should have executable permissions.
- The `LOCAL_IMAGE_NAME` is automatically generated based on the current date, but can be overridden if needed.

---
```# ELT Pipeline Postgres – Makefile Usage

This project uses a `Makefile` to automate common setup and management tasks for the ELT pipeline environment. Below is a description of each target and how to use them.

## Global Variables

- **LOCAL_TAG**: The current date in `YYYY-MM-DD` format, used for tagging images.
- **LOCAL_IMAGE_NAME**: The Docker image name for the dbt project, including the date tag.

## Targets

### `init`
Initializes the database environment.
```sh
make init
```
*Runs `scripts/setup-database-init.sh`.*

---

### `set_database`
Boots up the database server.
```sh
make set_database
```
*Runs `scripts/boot_database.sh`.*

---

### `set_dbt_image`
Builds the Docker image for the dbt project.
```sh
make set_dbt_image
```
*Runs `scripts/create-docker-image.sh`.*

---

### `set_airflow`
Boots up the Airflow environment, passing the `LOCAL_IMAGE_NAME` as an environment variable.
```sh
make set_airflow
```
*Runs `scripts/setup-airflow.sh` with `LOCAL_IMAGE_NAME` set.*

---

### `stop_servers`
Stops all running servers.
```sh
make stop_servers
```
*Runs `scripts/stop-servers.sh`.*

---

## Usage
Start with `make init` to initialize the database.
Then, run any of the above targets with `make <target>`.  
For example, to build the dbt Docker image:
```sh
make set_dbt_image
```

## Notes

- Ensure you have GNU Make and Bash installed.
- The `LOCAL_IMAGE_NAME` is automatically generated based on the current date, but can be overridden if needed.

---