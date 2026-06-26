select u.name,sum(t.amount)
balance from users u join 
transactions t
on u.account=t.account
group by u.account
having sum(t.amount)>10000;
