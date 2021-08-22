from pyspark.sql import SparkSession

## entry point for python program



if __name__ == "__main__":
    print("pyspark tutorial")

    spark = SparkSession.\
        builder.\
        appName("Testing Pyspark Examples").master("local[*]").\
        getOrCreate()



