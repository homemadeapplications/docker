# docker from scratch

## Creation de l'environmement virtuel python
```
python -m venv venv
```
## démarrage de l'environnement viretuel sous windows
```
venv\Scripts\activate
```
## build de l'image avec dockerfile
```
docker build -t chuck_norris_image .
```
## lancement de l'image (facultatif)
```
docker run --name chuch_norris_contener chuck_norris_image
```
## lancement du docker compose
```
docker compose up
```
## arret du docker compose
```
docker compose down
```
