# VERSION 1.0.1
# AUTHOR: Claudio "Klaus" Masolo
# DESCRIPTION: Airflow container with data science library
# BUILD: docker build --rm -t klaus/docker-airflow-ml .
# SOURCE: https://github.com/puckel/docker-airflow

FROM puckel/docker-airflow:1.10.1
RUN pip install --user scikit-learn
