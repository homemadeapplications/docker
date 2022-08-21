
# rappel docker

## alias
<ul>
<li>ctn = conteneur</li>
</ul>

## commands

### lancer un ctn hello world:
```
docker run hello-world
```
### lancer un ctn de maniere interactice (run un ctn ubuntu en lance l'application bash dans le ctn)

```
docker run -it ubuntu bash 
```

### voir tous les conteneur :

```
docker ps
```

### arreter un conteneur : 
```
docker rm <id du ctn>
```

### creer une image à partir d'un Dockerfile :
```
docker build -t <nom de l'image> .
```

### run image en mappant le port 80 du ctn sur le port 80 de la machine :
```
docker run -p 80:80 <nom de l'image>
```

### run docker compose :
```
docker-compose up
```
### supprimer docker compose :
```
docker-compose down
```