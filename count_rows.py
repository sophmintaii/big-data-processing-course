from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('HomeworkProject').getOrCreate()

if __name__ == '__main__':
    df = spark.read.csv("PS_20174392719_1491204439457_log.csv")
    print(f'num rows: {df.count()}')
