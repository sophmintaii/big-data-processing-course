CREATE KEYSPACE hw8_myntiuk WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE hw8_myntiuk;

CREATE TABLE IF NOT EXISTS uid_fraud (
	uid text,
	is_fraud int,
	amount float,
    	transaction_date date,
    	transaction_type text,
    	PRIMARY KEY (uid, isFraud)
    	);
    	
    	
CREATE TABLE IF NOT EXISTS uid_large (
	uid text,
	is_fraud int,
	amount float,
	transaction_date date,	
	transaction_type text,
	PRIMARY KEY (uid, amount)
	);
	
	
CREATE TABLE IF NOT EXISTS uid_income (
	uid text,
	is_fraud int,
	amount float,
	transaction_date date,	
	transaction_type text,
	PRIMARY KEY (uid, transaction_date)
	);

