# mysql에서는 concat을 사용, ||는 mysql에서 사용할 수 없음. postgresql/ sqlite/ oracle 에서 사용 가능
select concat(max(length),'cm') as max_length
from fish_info
where 1=1
and length is not null;