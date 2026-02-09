## BigQuery Setup

Create an external table using the Yellow Taxi Trip Records.

```
CREATE OR REPLACE EXTERNAL TABLE `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://03-data-warehouse-nhmichaeltam/yellow_tripdata_2024-*.parquet']
);

```

## Question 1. Counting records

What is count of records for the 2024 Yellow Taxi Data?

Answer - 20,332,093

```
SELECT 
  COUNT(*) AS total_records
FROM 
  `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024_external`;

```

## Question 2. Data read estimation

Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.

What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

Answer - 0 MB for the External Table and 155.12 MB for the Materialized Table

```
-- External Table
SELECT COUNT(DISTINCT(PULocationID)) 
FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024_external`;

-- Regular Table
SELECT COUNT(DISTINCT(PULocationID)) 
FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024`;

```

## Question 3. Understanding columnar storage

Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table.

Why are the estimated number of Bytes different?

Answer - BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

```
-- One column - 155.12 MB
SELECT PULocationID FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024`;

-- Two columns - 310.24 MB
SELECT PULocationID, DOLocationID FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024`;

```

## Question 4. Counting zero fare trips

How many records have a fare_amount of 0?

Answer - 8,333

```
SELECT count(*) 
FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024`
WHERE fare_amount = 0;

```

## Question 5. Partitioning and clustering

What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

Answer - Create new table that is partitioned by dropoff datetime and clustered by VendorID.

```
CREATE OR REPLACE TABLE `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024`;

```

## Question 6. Partition benefits

Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values?

Choose the answer which most closely matches.

Answer - 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

```
-- Non partitioned
SELECT DISTINCT(VendorID)
FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

-- Partitioned
SELECT DISTINCT(VendorID)
FROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024_clustered`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

```

## Question 7. External table storage

Where is the data stored in the External Table you created?

Answer - GCP Bucket

It's external as the data remains in original location (i.e. GCP storage)

## Question 8. Clustering best practices

It is best practice in Big Query to always cluster your data:

Answer - True. Exception being for tables <1GB which won't show much improvement.  

## Question 9. Understanding table scans

No Points: Write a SELECT count(*) query FROM the materialized table you created. How many bytes does it estimate will be read? Why?

Answer - The estimate number of bytes is 0 B, this is because BigQuery retrieves the count of entries directly from table metadata, and not from the actual data.

```
SELECT COUNT(*) 
ROM `nhmichaeltam-de-zoomcamp.trips_data_all.yellow_tripdata_2024`;

```