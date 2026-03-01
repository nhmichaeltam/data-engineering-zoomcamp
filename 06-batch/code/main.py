from pyspark.sql import SparkSession

# Create a local Spark session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

# Execute and print the version
print(f"Spark Version: {spark.version}")