CREATE KEYSPACE hw8_myntiuk WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE hw8_myntiuk;

CREATE TABLE IF NOT EXISTS 
uid_fraud (
	step int, 
	type text, 
	amount float,
	nameOrig ascii,
	oldbalanceOrg float,
	newbalanceOrig float,
	nameDest ascii,
	oldbalanceDest float,
	newbalanceDest float,
	isFraud int,
	isFlaggedFraud int,
	transactionDate date,
	PRIMARY KEY (nameOrig, isFraud)
	);
	
CREATE TABLE IF NOT EXISTS 
uid_date (
	step int, 
	type text, 
	amount float,
	nameOrig ascii,
	oldbalanceOrg float,
	newbalanceOrig float,
	nameDest ascii,
	oldbalanceDest float,
	newbalanceDest float,
	isFraud int,
	isFlaggedFraud int,
	transactionDate date,
	PRIMARY KEY (nameDest, transactionDate)
	);
