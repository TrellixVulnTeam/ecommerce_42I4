
CONTAINERID=$(docker ps -a | grep postgresql_webbuy | awk '{print $1}')
echo "Starting a new database container ${CONTAINERID}"
docker stop $CONTAINERID
echo "Deleting the container ${CONTAINERID}"
docker rm $CONTAINERID

echo "Starting a new database container"
docker run -d --name postgresql_webbuy -p 5432:5432 -e POSTGRESQL_USERNAME=webbuy_user -e POSTGRESQL_PASSWORD=webbuy12890 -e POSTGRESQL_DATABASE=webbuy bitnami/postgresql:latest

