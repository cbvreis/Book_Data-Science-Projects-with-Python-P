from pyspark.sql import SparkSession


def map_function(df):
    return df.rdd.map(lambda x: (x[0], x[1]))


def reduce_function(df):
    return df.rdd.reduceByKey(lambda x, y: max(x, y))


if '__name__' == '__main__':
    spark = SparkSession.builder.appName('map_reduce').getOrCreate()
    df = spark.read.csv('data/dados.csv', header=True, inferSchema=True)
    df_map = map_function(df)
    df_reduce = reduce_function(df)
    df_map.show()
    df_reduce.show()
    spark.stop()

