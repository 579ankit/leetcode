select date_format(trans_date,'%Y-%m') as month,country,count(id) trans_count,
sum(if(state='approved',1,0)) approved_count,sum(amount) trans_total_amount,sum(if(state='approved',amount,0)) approved_total_amount from transactions group by country,DATE_FORMAT(trans_date, '%Y-%m')


