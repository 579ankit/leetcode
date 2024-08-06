select Email from person group by email having count(email)>1;
