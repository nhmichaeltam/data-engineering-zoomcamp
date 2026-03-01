## BigQuery Setup

Create an external table using the Yellow Taxi Trip Records.

```
CREATE OR REPLACE EXTERNAL TABLE `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://03-data-warehouse-nhmichaeltam/yellow_tripdata_2024-*.parquet']
);

```

## Question 1. Install Spark and PySpark

Install Spark
Run PySpark
Create a local spark session
Execute spark.version.
What's the output?

Answer - Spark Version: 4.1.1

```
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

print(f"Spark Version: {spark.version}")

```

## Question 1. XX

xx

Answer - xx

```
xx

```
## Question 1. XX

xx

Answer - xx

```
xx

```
## Question 1. XX

xx

Answer - xx

```
xx

```
## Question 1. XX

xx

Answer - xx

```
xx

```
## Question 1. XX

xx

Answer - xx

```
xx

```
