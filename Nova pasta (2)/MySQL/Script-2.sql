select
*
from estudosmysql.nestle as n
join estudosmysql.cereal as c
on n.id_cereais = c.id
join estudosmysql.prestigio as p
on c.id_prestigio = n.id