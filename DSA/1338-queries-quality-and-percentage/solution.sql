select query_name,
round(sum(rating/position)/count(query_name),2) quality,
round(sum(if(rating<3,1,0))*100/count(rating),2) as poor_query_percentage 
from queries where query_name is not null group by query_name ;






