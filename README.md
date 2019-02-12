**Emoji detection in a container**

This is a containerized version of MIT's Deepmoji (https://github.com/bfelbo/DeepMoji), using python and Flask.

Usage: 

```
docker build -t mydeepmoji .

docker run -it -p 5000:5000 mydeepmoji

```

Navigate to: 

http://localhost:5000

http://localhost:5000/well%20at%20least%20your%20mom%20thinks%20you're%20pretty
