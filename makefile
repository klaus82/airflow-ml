NAME   := klaus/docker-airflow-ml
#TAG    := $$(git log -1 --pretty=%!H(MISSING))
TAG    := 1.0.1
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:latest
 
build:
  @docker build -t ${IMG} .
#  @docker tag ${IMG} ${LATEST}
 
#push:
#  @docker push ${NAME}
 
#login:
#  @docker log -u ${DOCKER_USER} -p ${DOCKER_PASS}