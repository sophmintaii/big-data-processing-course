# Homework 3: Cassandra data modeling

## Comments on selected keys

* customers: як partition key обраний customer_id, оскільки за ним можна найрівномірніше розділити дані та за ним відбувається вибір рядків. Як clustering key обраний star_rating, оскільки значення за цим ключем треба порівнювати між собою.

* products - як partition key обраний product_id, оскільки за ним можна найрівномірніше розділити дані та за ним відбувається вибір рядків. Як clustering key обраний star_rating, оскільки значення за цим ключем треба порівнювати між собою.
