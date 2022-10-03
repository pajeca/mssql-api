# mssql-api
To run application locally

Create image from dockerfile:
docker build -t <image_name> .

run the image:
docker run -d --name <container_name> -p 8000:80 <image_name>

Access the application in browser and check documents @ container-hostip:8000/docs
