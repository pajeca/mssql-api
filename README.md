# mssql-api

This repo is public, however, the application will not work unless a postgres db is created with the necessary data required by the application.  
The Postgres DB is deployed via k8s within ../k8s/postgres/  
The local volume created by the postgres-pv.yaml file will need to be populated with the necessary tables and data required by the app.
Tables and required data can viewed in ../app/models.py

A postgres-configmap.yaml file will need to be created within ../k8s/postgres/ which will be used within the postgres-statefulset.yaml file.  
The configmap yaml file will need to contain:  
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-config
  namespace: mssql-app
  labels:
    db: postgres
    app: mssql_app
data:
  POSTGRES_PASSWORD: <postgres db password>
  POSTGRES_USER: <postgress db username>
  POSTGRES_DB: mssql_app_db
```

**Run app from a Docker Container:**    
Once the postgres DB is set with the required schema/tables/data and the statefulset deployed, the application can be run locally from a docker container: 

create a local_settings.py file under /app which will contain  
```
postgresql = {'pguser': '<postgres db username>',
'pgpasswd': '<postgres db password>',
'pghost': '<container host ip>',
'pgport': 30432,
'pgdb': 'mssql_app_db'}
```
The app within the container will connect to the postgres db via the postgres-service-nodeport on port 30432.

Create image from dockerfile:  
docker build -t <image_name> .

run the image:  
docker run -d --name <container_name> -p 8000:8000 <image_name>

Access the application in browser and check documents @:    
```
container-hostip:8000/docs
```

**Deploy App to K8s:**   
Deploy all files within ../k8s/postgres and ensure all data required is created.
Deploy all files within ../k8s/app

Access the api via:  
```
http://<container host node>:30800/docs
```


SQL Version and Build data is from this google doc provided by sqlserverbuilds.blogspot.com:  
https://docs.google.com/spreadsheets/d/16Ymdz80xlCzb6CwRFVokwo0onkofVYFoSkc7mYe6pgw/view#gid=0
