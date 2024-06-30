--Denormalization is a strategy used on a previously-normalized database to increase performance.
--By reducing the number of joins and complex queries, denormalization can lower the load on the database server, making it more efficient to handle high traffic, it also can Improve Read Performance.
--example:
SELECT o-id, o-date, o-date, email
FROM orders 
JOIN customers ON o-id = c-id;
SELECT id, o-date, o-date, email
FROM orders;
--data are stored in two tables. To fetch customer and order details, a join is required by Denormalized we combine data so we have one table
