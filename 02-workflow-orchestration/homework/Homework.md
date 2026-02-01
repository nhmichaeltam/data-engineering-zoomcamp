# Module 2 Homework: Workflow orchestration

## Question 1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?

Answer - 128.3 MiB

```
![alt text](image.png)

```

## Question 2. What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

Answer - green_tripdata_2020-04.csv

```
variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"

# Set_label task uses the above variable logic. {{inputs}} placeholders are replaced by selected values (i.e. green, 2020 and 04)

```

## Question 3. How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

Answer - 24,648,499

```
SELECT COUNT(*) 
FROM yellow_tripdata 
WHERE filename LIKE 'yellow_tripdata_2020-%'

```

## Question 4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?

Answer - 1,734,051

```
SELECT COUNT (*)
FROM green_tripdata
WHERE filename LIKE 'green_tripdata_2020-%'

```

## Question 5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file?

Answer - xx

```
xxx

```

## Question 6. xx

xxx

Answer - xx

```
xxx

```

