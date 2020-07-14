-- Number of matches in Score
SELECT score, count(*) AS number FROM second_table GROUP BY score DESC;
