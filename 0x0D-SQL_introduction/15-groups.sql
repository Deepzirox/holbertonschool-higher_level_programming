-- Number of matches in Score
SELECT score, count(*) as number from second_table GROUP by score desc;
