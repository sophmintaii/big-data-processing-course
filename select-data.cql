// task 1 - select all products with given product_id
SELECT review
FROM products
WHERE product_id = 3;

// task 2 - select all products with given product_id and star_rating
SELECT review
FROM products
WHERE product_id = 3 AND star_rating = 3;

// task 3 - select all the reviews written by customer
SELECT review
FROM customers
WHERE customer_id = 2;

// task 4 - select customers that left more than N reviews and also left review on the product with given product_id


// task 5 - select number of reviews left by given user
SELECT COUNT(*)
FROM customers
WHERE customer_id = 1 AND star_rating > 3);
