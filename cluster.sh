aws emr create-cluster --name "Cluster Spark" --release-label emr-5.34.0 \
--applications Name=Spark \
--log-uri s3://bucket/logs/ \
--ec2-attributes KeyName \
--instance-type m5.xlarge \
--instance-count 3 \
--steps Type=Spark,Name="Spark Program",ActionOnFailure=CONTINUE,Args=[--deploy-mode,client,s3://livrosaplicacaofacul/pyspark-script/data-processing.py] \
--use-default-roles
