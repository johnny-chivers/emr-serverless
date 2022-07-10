-- create database
CREATE DATABASE IF NOT EXISTS emrdb;

-- create table; 
CREATE EXTERNAL TABLE emrdb.customer
    (
    `CustomerID` 	INT, 	
	`NameStyle` 	STRING,	
	`Title`	 	STRING,
	`FirstName`	STRING,
	`MiddleName`	STRING,
	`LastName`	STRING,
	`Suffix`	STRING,
	`CompanyName`	STRING,
	`SalesPerson`	STRING,
	`EmailAddress`	STRING,
	`Phone`		STRING,
	`PasswordHash`	STRING,
	`PasswordSalt`	STRING,
	`rowguid`	STRING,
	`ModifiedDate`  STRING
    )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://<s3-bucket-name>/customers/'
TBLPROPERTIES ('skip.header.line.count'='1')
;


