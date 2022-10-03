# mssql-api
To run application locally

Create image from dockerfile:
docker build -t <image_name> .

run the image:
docker run -d --name <container_name> -p 8000:80 <image_name>

access the application in browser @ container-hostip:8000
