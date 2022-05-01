#!/bin/bash
DDL_commands="CREATE KEYSPACE hw4_myntiuk WITH REPLICATION = {
                    'class' : 'SimpleStrategy',  
                    'replication_factor' : 1 }; 
                    
                USE hw4_myntiuk; 
                
                CREATE TABLE products ( 
                    customer_id int,  
                    product_id ascii,  
                    product_title text,  
                    review_body text,
                    star_rating tinyint, 	
                    PRIMARY KEY (product_id, star_rating)); 
                    
                CREATE TABLE reviews ( 
                    customer_id int,  
                    review_id ascii,  
                    product_id ascii,  
                    product_title text,  
                    star_rating tinyint, 	
                    verified_purchase text,  
                    review_body text,  
                    review_date date,  
                    PRIMARY KEY (customer_id, review_id));"

docker exec -it node1 cqlsh -e "${DDL_commands}"
