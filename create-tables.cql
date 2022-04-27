CREATE TABLE products (
	product_id int, 
	star_rating int, 
	review_body text, 
	PRIMARY KEY (product_id, star_rating));

CREATE TABLE customers (
	customer_id int,
	star_rating int, 
	review_body text, 
	PRIMARY KEY (customer_id, star_rating));
