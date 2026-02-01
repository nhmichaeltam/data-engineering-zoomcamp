# Docker basics
docker ps -> lists all running containers on machine
docker ps -a -> lists all conatiners (running + stopped)
docker compose ps -> lists containers in current compose project
docker compose up -> starts container in foreground (terminal)
docker compose up -d -> starts container in background (detached)
docker compose down -> stops and removes containers + networks
docker images -> lists images on machine
docker stop <container> -> stops running container
docker start <container> -> starts existing stopped container
docker restart <container> -> stops and starts container again
docker rm <container> -> deletes a stopped container
