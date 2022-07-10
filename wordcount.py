#
# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
#      http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#

import os
import sys
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

if __name__ == "__main__":
    """
        Usage: wordcount [destination path]
    """
    spark = SparkSession\
        .builder\
        .appName("WordCount")\
        .getOrCreate()

    output_path = None

    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    else:
        print("S3 output location not specified printing top 10 results to output stream")

    region = os.getenv("AWS_REGION")
    text_file = spark.sparkContext.textFile("s3://" + region  + ".elasticmapreduce/emr-containers/samples/wordcount/input")
    counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).sortBy(lambda x: x[1], False)
    counts_df = counts.toDF(["word","count"])

    if output_path:
        counts_df.write.mode("overwrite").csv(output_path)
        print("WordCount job completed successfully. Refer output at S3 path: " + output_path)
    else:
        counts_df.show(10, False)
        print("WordCount job completed successfully.")

    spark.stop()