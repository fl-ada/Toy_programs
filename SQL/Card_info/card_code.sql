use train;

-- Q.1 customer with max no. of cards
select customer_id
from cardowner
group by customer_id
having count(card_id) = (
	select count(card_id) as cardCount
    from cardowner
    group by customer_id
    order by cardCount DESC
    LIMIT 1
);

-- Q.2 card that has max. balance
select *
from card
where balance = (
	select max(balance) from card
);

-- Q.3 highest balance card by each customer
select cardowner.customer_id, card.card_id, max(card.balance)
from cardowner, card
where cardowner.card_id = card.card_id
group by cardowner.customer_id;

-- Q.4 3rd highest card balance
select balance
from card
order by balance DESC
limit 1 offset 2;


-- Q.5 customers who took train at same station more than once in the same day
select customer_id, station_id, latest_date, count(*) no_visits
from cardusage
group by customer_id, station_id, latest_date
having count(*) > 1
order by latest_date DESC;

-- Q.6 first 2 even customer_id values
select customer_id
from customer
where customer_id%2 = 0
order by customer_id
limit 2;

-- Q.7 explain the differences
SELECT COUNT(*), SUM(1) FROM cardusage GROUP BY customer_id;
SELECT COUNT(*), SUM(2) FROM cardusage GROUP BY station_id;
SELECT COUNT(*), SUM(3) FROM cardusage GROUP BY latest_expense;
-- COUNT(*) counts no. of rows of such occurance, 
-- and sum(n) adds n every time such occurance happens.
-- COUNT(*) and sum(1) does same function here, so we can say
-- n * COUNT(*) = sum(n) for this case.


-- Q.8 sum of all positive card balance/negative
-- use select..from syntax only once
select sum(case when balance >= 0 then balance else 0 end) as positive,
		sum(case when balance <0 then balance else 0 end) as negative
from card;


-- Q.9 add 20 to nagative card balance, add 5 to positive card balance
select card_id, balance + 
	sum(case when balance >= 0 then 20 else 0 end) +
	sum(case when balance < 0 then 5 else 0 end) as newbalance
from card
group by card_id;

-- Q.10 no. of cards owned by customer with max. no of cards that was deducted to negative balance 
-- in the same station within the last ten days
select cus_id, cus_name, count(card) card_satisfied, s_name
from (
	select c.customer_id cus_id, card.card_id card, c.customer_name cus_name, s.station_name s_name,
		row_number() over (partition by (card.card_id)) n
	from customer c, station s, cardusage u, card
	where c.customer_id = u.customer_id and
		s.station_id = u.station_id and
		u.card_id = card.card_id and
		u.latest_date >= date_sub('2020-03-05', interval 10 day) and	-- within 10 days
		card.balance < 0
	group by card.card_id, s.station_id
	having c.customer_id in ( -- limit to the customers with max no. of cards
		select customer_id
		from cardowner
		group by customer_id
		having count(card_id) = (
			select count(card_id) as cardCount
			from cardowner
			group by customer_id
			order by cardCount DESC
			LIMIT 1
		))) t
where n = 1
group by cus_id, s_name;

    
