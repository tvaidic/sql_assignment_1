-- Count how many rows you have
SELECT COUNT(*) FROM titanic;

-- How many people survived?
SELECT COUNT(*) FROM titanic WHERE "Survived" = 1;

-- What passenger class has the largest population?
SELECT "Pclass", COUNT(*) as "Passenger_Count"
FROM titanic
GROUP BY "Pclass"
ORDER BY "Passenger_Count" DESC
LIMIT 1;
