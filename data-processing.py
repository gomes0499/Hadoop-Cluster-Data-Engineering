from pyspark.sql import SparkSession

# Crie uma sessão Spark
spark = SparkSession.builder.getOrCreate()

# Use o método read.csv do SparkSession para ler o arquivo CSV
df = spark.read.format('csv') \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .option('delimiter', ';') \
    .load('s3://livrosaplicacaofacul/bronze-layer/')

# Escreva o DataFrame em formato Parquet no caminho especificado
df.write.parquet('s3://livrosaplicacaofacul/silver-layer/', mode='overwrite')
