-- Average temperatures of the cities
SELECT city, AVG(value) as avg_temp FROM temperatures group by city order by avg_temp desc;
