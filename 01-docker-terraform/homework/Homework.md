# Module 1 Homework: Docker & SQL

## Question 1. Understanding Docker images

Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image? 

Answer - 25.3

```
docker run -it --rm --entrypoint=bash python:3.13

pip --version
```

## Question 2. Understanding Docker networking and docker-compose

Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

postgres:5433
localhost:5432
db:5433
postgres:5432
db:5432

If multiple answers are correct, select any

```
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

Answer - db:5432

```
docker compose up

docker compose ps
```

## Question 3. Counting short trips

For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

Answer - 8,007

```
SELECT count(*) 
FROM green_taxi_trips_2025_11
WHERE lpep_pickup_datetime >= '2025-11-01' 
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;

```

## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

Use the pick up time for your calculations.

Answer - 2025-11-14

```
SELECT
    DATE(lpep_pickup_datetime) AS pickup_date,
    MAX(trip_distance) AS max_trip_distance
FROM green_taxi_trips_2025_11
WHERE trip_distance < 100
GROUP BY pickup_date
ORDER BY max_trip_distance DESC
LIMIT 1;

```


## Question 5. Biggest pickup zone

Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?


Answer - East Harlem North

```
SELECT
    z."Zone",
    SUM(t.total_amount) AS total_revenue
FROM "green_taxi_trips_2025_11" t
JOIN "zones" z 
	ON t."PULocationID" = z."LocationID"
WHERE t."lpep_pickup_datetime" 
    BETWEEN '2025-11-18' AND '2025-11-19'
GROUP BY z."Zone"
ORDER BY total_revenue DESC
LIMIT 1;

```


## Question 6. Largest tip

For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

Note: it's tip , not trip. We need the name of the zone, not the ID.

Answer - Yorkville West

```
xSELECT z_do."Zone" AS dropoff_zone, MAX(t."tip_amount") AS max_tip
FROM "green_taxi_trips_2025_11" t
JOIN "zones" z_do ON t."DOLocationID" = z_do."LocationID"
JOIN "zones" z_pu ON t."PULocationID" = z_pu."LocationID"
WHERE z_pu."Zone" = 'East Harlem North'
  AND t."lpep_pickup_datetime" 
  BETWEEN '2025-11-01' AND '2025-12-01'
GROUP BY z_do."Zone"
ORDER BY max_tip DESC
LIMIT 1;

```


## Question 7. Terraform Workflow

Which of the following sequences, respectively, describes the workflow for:

- Downloading the provider plugins and setting up backend
- Generating proposed changes and auto-executing the plan
- Remove all resources managed by terraform

Answer - terraform init, terraform apply -auto-approve, terraform destroy

