# EMR Serverless

## Table of contents

- [What's included](#whats-included)
- [Set Up Work](#set-up)
- [Main Tutorial](#main-tutorial)
- [Useful Links](#useful-links)
- [Creators](#creators)
- [Thanks](#thanks)

## What's included

The repo is to supplement the youtube video (link) on emr severless. 
The contents of the repo are denoted below. 

```text
folder1/
└── folder2/
    ├── folder3/
    │   ├── file1
    │   └── file2
    └── folder4/
        ├── file3
        └── file4
```

## Set up

1. Create EMR Notebook Role
- Open IAM and create the IAM role for the EMR notebook using FILE
- Attach AmazonElasticMapReduceEditorsRole policy
- Attached AmazonS3FullAccess policy 

2. Create EMR Servlerless Execution Role
- Open IAM and create the IAM role for the EMR Servlerless Execution using FILE
- Attach FILE policy for permisions

3. Create S3 bucket
- Open S3 console 
- create S3 bucket to use for the demo 

4. Create Folder To use in S3 Bucket 
- Create a `scripts` folder
- Create a `customers` folder (We use this to upload a CSV to)
- Create a `query-results` folder


## Main Tutorial

**Hive**
1. Naviagte to EMR home from the AWS Console and select EMR Studio from the left handside. ![](images/hive/1._emr-service-home.png)

2. Select `Get Started` ![](images/hive/2._emr-studio-get-started.png)

3. Select `Create Studio` ![](images/hive/3._create-studio.png)

4. Insert Studio name ![](images/hive/4._name-studio.png)

5. Under `Networking and Security` select your default VPC and 3 public subnets. ![](images/hive/5._networking-security.png)

6. Select the EMR Studio role `emr-notebook-role-tutorial` created duing the [Set Up Work](#set-up) stage ![](images/hive/6._emr-service-role.png)

7. Select the S3 bucket created duing the [Set Up Work](#set-up) stage. (This will be your own customer bucket name) ![](images/hive/7._select-s3-bucket.png)

8. Select the `Studio access URL` ![](images/hive/8._select-the-studio-access-url.png)

9. Select `applications` under `serverless` from the left handside menu ![](images/hive/9._select-applications.png)

10 Select `create application` from the top right ![](images/hive/10._create-application.png)

11. Enter a name for the application. Leave the type as `Spark` and click `create application` ![](images/hive/11._name-spark-app.png)

12. Click into the application via the `name` ![](images/hive/12._click-into-application.png)

13. Click `submit job` ![](images/hive/13._click-submit-job.png)

14. Name job and select the service role created in the set up steps. ![](images/hive/14._name-job.png)

15. Click `Submit Job` ![](images/hive/15._submit-job.png)

16. job status will go from pending -> running -> success. ![](images/hive/16._job-status.png)


## Creators

**Johnny Chivers**

- <https://github.com/johnny-chivers/>

## Useful Links

- youtube video (link)
- website 
- buy me a coffee


Enjoy :metal:
