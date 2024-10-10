# Databricks notebook source
from framework.common_functions.metadata_functions import (
    read_yaml,
    get_spark_type_mapping,
)
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
    ])
data = [
    (4, "David", 34),
    (5, "Emma", 29)]


dbutils.widgets.text('env_name','')
dbutils.widgets.text('name_prefix','')
dbutils.widgets.text('databricks_version','')

if __name__ == "__main__":
    print("This is example 1")
    print(read_yaml("example1_columns"))
    print(get_spark_type_mapping())
    env_name = dbutils.widgets.get('env_name')
    name_prefix = dbutils.widgets.get('name_prefix')
    databricks_version = dbutils.widgets.get('databricks_version')
    print('env_name',env_name)
    print('name_prefix',name_prefix)
    print('databricks_version',databricks_version)
    df = spark.createDataFrame(data, schema)
    df.write.format("delta").mode("append").saveAsTable("demo_table")
    spark.read.format("delta").table("demo_table").display()
    