# 第一次做数据库的题 不算难
# Write your MySQL query statement below
SELECT * FROM cinema
            WHERE id%2 = 1
            AND description != 'boring'
            ORDER BY  rating DESC