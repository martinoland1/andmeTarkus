-- 11. ALAMPÄRINGUD - viide teisele päringule: Millised töötajad on keskmiselt andnud allahindlust üle 7,5%?

select sales_rep_name, sales_rep_id
from salesrep_table st 
where st.sales_rep_id in (
	select st2.sales_rep_id 
	from sales_table st2
	group by st2.sales_rep_id 
	having avg(discount) > 0.075);

-- 12. AJUTISED PÄRINGUTULEMUSED (Common Table Expressions - CTEs): : Millised töötajad on keskmiselt andnud allahindlust üle 7,5% ja kui suur on keskmine antud allahindlus?

with salesrep_discount as (
	select sales_rep_id, avg(discount) as avg_discount
	from sales_table
	group by sales_rep_id
	having avg(discount) > 0.075)
select salesrep_table.sales_rep_name , salesrep_discount.sales_rep_id, salesrep_discount.avg_discount
from salesrep_discount
left join salesrep_table on salesrep_discount.sales_rep_id = salesrep_table.sales_rep_id;

----- HARJUTAMISEKS: tegelik müük vs eelarve müügiesindaja kaupa

with actual_sale as (
	select SUM(st.quanitity * st.unit_price * (1-st.discount )) as sales_total_quanitity, st.sales_rep_id
	from sales_table st
	group by st.sales_rep_id
)
select actual_sale.sales_rep_id as sales_sales_rep_id, bt.sales_rep_id as budget_sales_rep_id, bt.budget_sum as budget_sum, actual_sale.sales_total_quanitity, st.sales_rep_name 
from salesrep_table st
left join budget_table bt on st.sales_rep_id = bt.sales_rep_id
full outer join actual_sale on actual_sale.sales_rep_id = bt.sales_rep_id;


-- 13. TABELITE KOMBINEERIMINE
-- 13.1. Leia tabelite pealt unikaalsed väärtused: Leia kliendid, kellel oli müüke 2025. aastal või enne 2021. aastat -- UNION

select customer_id, product_id, sum(st.quanitity)
from sales_table st 
where st.sale_date >= '2025-01-01'
group by customer_id , product_id
union
select customer_id, product_id, sum(st.quanitity)
from sales_table st
where st.sale_date < '2021-12-31'
group by customer_id , product_id;



-- 13.2. Leia kõik väärtused mitmest tabelist: Leia kõik müügid 2025. aastal või enne 2021. aastat -- UNION ALL

select *
from sales_table st 
where st.sale_date >= '2025-01-01'
union all
select *
from sales_table st
where st.sale_date < '2021-12-31';
