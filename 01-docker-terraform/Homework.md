# Module 1 Homework: Docker & SQL

## Question 1. Understanding Docker images

Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image? - 25.3

```
docker run -it --rm --entrypoint=bash python:3.13

pip --version
```

