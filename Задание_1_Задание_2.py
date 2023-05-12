Задание 1.1.
Необходимо вывести доход, который принесли только хорошие клики (good_clicks)?
-- предполагаем, что в stat_collector хранится общий доход от показа блока + общее количество "хороших" и "фродовых" кликов
-- также предполагаем, что доход от клика одинаковый, вне зависимости от того  "хороший" или "фродовый" это клик кликов
-- при этих вводных суммарный доход всех блоков от хороших кликов можно получить:

SELECT SUM((revenue / (good_clicks + fraud_clicks)) * good_clicks) AS good_clicks_revenue 
FROM stat_collector
WHERE good_clicks + fraud_clicks > 0;

— вторую таблицу можем использовать для вывода доходности "хороших" кликов с разбиением по сайтам
SELECT domain_id, 
       domain_name,
       SUM((revenue / (good_clicks + fraud_clicks)) * good_clicks) AS good_clicks_revenue 
FROM stat_collector
INNER JOIN block_domains ON stat_collector.block_id = block_domains.block_id
WHERE good_clicks + fraud_clicks > 0
GROUP BY domain_id, domain_name;


Задание 1.2.
Необходимо вывести топ-10 сайтов по обороту среди тех, которые имеют более 25% плохих кликов.
-- предполагаем, что в stat_collector хранится общий доход от показа блока + общее количество "хороших" и "фродовых" кликов
SELECT domain_id, 
       domain_name,
       SUM(revenue * (good_clicks + fraud_clicks)) AS total_revenue 
FROM stat_collector
INNER JOIN block_domains ON stat_collector.block_id = block_domains.block_id
WHERE fraud_clicks / (good_clicks + fraud_clicks) > 0,25
GROUP BY domain_id, domain_name
LIMIT 10;