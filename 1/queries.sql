/* Question A1 */
/* Monthly order total */
SELECT AVG(MPrice) FROM
(SELECT SUM(price) as MPrice, COUNT(DISTINCT userId) as MUsers, strftime('%Y-%m', date)
FROM Items
INNER JOIN Purchases USING(itemId)
INNER JOIN Users USING(userId)
WHERE age >= 18 AND age <=25
GROUP BY strftime('%Y-%m', date));

/* Monthly order by user */
SELECT AVG(MPrice)/MUsers FROM
(SELECT SUM(price) as MPrice, COUNT(DISTINCT userId) as MUsers, strftime('%Y-%m', date)
FROM Items
INNER JOIN Purchases USING(itemId)
INNER JOIN Users USING(userId)
WHERE age >= 18 AND age <=25
GROUP BY strftime('%Y-%m', date));


/* Question A2 */
/* Monthly order total */
SELECT AVG(MPrice) FROM
(SELECT SUM(price) as MPrice, COUNT(DISTINCT userId) as MUsers, strftime('%Y-%m', date)
FROM Items
INNER JOIN Purchases USING(itemId)
INNER JOIN Users USING(userId)
WHERE age >= 18 AND age <=25
GROUP BY strftime('%Y-%m', date));

/* Monthly order by user */
SELECT AVG(MPrice)/MUsers FROM
(SELECT SUM(price) as MPrice, COUNT(DISTINCT userId) as MUsers, strftime('%Y-%m', date)
FROM Items
INNER JOIN Purchases USING(itemId)
INNER JOIN Users USING(userId)
WHERE age >= 18 AND age <=25
GROUP BY strftime('%Y-%m', date));


/* Question B */
SELECT Month FROM
(SELECT Month, MAX(MonthlySum) 
FROM
(SELECT SUM(price) AS MonthlySum, strftime('%m',date) AS Month
FROM Items
INNER JOIN Purchases USING(itemId)
INNER JOIN Users USING(userId)
WHERE age > 35
GROUP BY Month));


/* Question C */

SELECT itemId FROM
(SELECT itemId, MAX(lastYearPrice) FROM
(SELECT itemId, SUM(price) as lastYearPrice
FROM Items
INNER JOIN Purchases USING(itemId)
WHERE date > date('now','-1 year')
GROUP BY itemId));

/* Question D */
SELECT itemId, SUM(price) as IdYearTotal, 
strftime('%Y', date) as Year,
100*SUM(price)/(SELECT SUM(price) FROM Items
INNER JOIN Purchases USING(itemId)
WHERE strftime('%Y', date) = '2017')
FROM (SELECT * FROM Items
INNER JOIN Purchases USING(itemId)
WHERE strftime('%Y', date) = '2017') AS TEM
GROUP BY itemId, Year
ORDER BY IdYearTotal DESC
LIMIT 3;
