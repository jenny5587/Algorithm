with temp as (
select *
from car_rental_company_rental_history
where 1=1
and start_date between '2022-08-01' and '2022-10-31'
group by car_id
having count(car_id) >= 5
)
select month(a.start_date) as month, a.car_id as car_id, count(*) as records
from car_rental_company_rental_history a join temp b
on a.car_id = b.car_id
where 1=1
and a.start_date between '2022-08-01' and '2022-10-31'
group by month(a.start_date), a.car_id
having count(b.car_id) != 0
order by month asc, car_id desc