# EMR Serverless

## Table of contents

- [What's included](#whats-included)
- [Set Up Work](#set-up)
- [Main Tutorial](#main-tutorial)
- [Useful Links](#useful-links)
- [Creators](#creators)

## What's included

The repo is to supplement the youtube video (link) on emr severless.

## Set up

1. Create EMR Notebook Role
- Open IAM and create the IAM role for the EMR notebook using the [emr notebook role json](emr_notebook_rol_priv.json)
- Attach AmazonElasticMapReduceEditorsRole policy
- Attached AmazonS3FullAccess policy 

2. Create EMR Servlerless Execution Role
- Open IAM and create the IAM role for the EMR Servlerless Execution using [emr serverless role](emr_serverless_role_priv.json)
- Attach [policy for permisions](emr_serverless_policy.json)

3. Create S3 bucket
- Open S3 console 
- create S3 bucket to use for the demo 

4. Create Folder To use in S3 Bucket 
- Create a `scripts` folder
- Create a `customers` folder (We use this to upload a CSV to)
- Create a `query-results` folder


## Main Tutorial

**Studio Setup**
1. Naviagte to EMR home from the AWS Console and select EMR Studio from the left handside. ![](images/spark/1._emr-service-home.png)

2. Select `Get Started` ![](images/spark/2._emr-studio-get-started.png)

3. Select `Create Studio` ![](images/spark/3._create-studio.png)

4. Insert Studio name ![](images/spark/4._name-studio.png)

5. Under `Networking and Security` select your default VPC and 3 public subnets. ![](images/spark/5._networking-security.png)

6. Select the EMR Studio role `emr-notebook-role-tutorial` created duing the [Set Up Work](#set-up) stage ![](images/spark/6._emr-service-role.png)

7. Select the S3 bucket created duing the [Set Up Work](#set-up) stage. (This will be your own customer bucket name) ![](images/spark/7._select-s3-bucket.png)

8. Select the `Studio access URL` ![](images/spark/8._select-the-studio-access-url.png)

**Spark App Setup**

9. Select `applications` under `serverless` from the left handside menu ![](images/spark/9._select-applications.png)

10 Select `create application` from the top right ![](images/spark/10._create-application.png)

11. Enter a name for the application. Leave the type as `Spark` and click `create application` ![](images/spark/11._name-spark-app.png)

12. Click into the application via the `name` ![](images/spark/12._click-into-application.png)

13. Click `submit job` ![](images/spark/13._click-submit-job.png)

14. Name job and select the service role created in the set up steps. ![](images/spark/14._name-job.png)

15. Click `Submit Job` ![](images/spark/15._submit-job.png)

16. job status will go from pending -> running -> success. ![](images/spark/16._job-status.png)

**Hive App Setup**

17. Create Application from applications ![](images/hive/17._create_hive_app.png)

18. Name and select Hive application ![](images/hive/18._name_hive_app.png)

19. Open hive application ![](images/hive/19._open-hive-emr-tutorial.png)

20. Submit the job ![](images/hive/20._submit-job.png)

21. Name the hive job, select hive script (change bucket name in script),and select service role. ![](images/hive/21._name_hive_job.png)

22. Copy and paste Hive config (change bucket name in json). ![](images/hive/22._hive_job_config.png)

23. Submit Job and monintor. Job status will go from pending -> running -> success. ![](images/hive/23._job_mon.png)

24. Navigate to Glue databases and click emrdb ![](images/hive/24._glue.png)

25. Look at table created ![](images/hive/25._glue_table.png)

26. Bonus - select data using athena and the created table. ![](images/hive/26._athena.png)

## Creators

**Johnny Chivers**

- <https://github.com/johnny-chivers/>

## Useful Links

- youtube video (link)
- [website](www.johnnychivers.co.uk)
- [buy me a coffee](https://www.buymeacoffee.com/johnnychivers)


Enjoy :metal:
