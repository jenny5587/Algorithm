with temp as (
select year(DIFFERENTIATION_DATE) as year, max(size_of_colony) as max_size from ecoli_data
where 1=1
group by year(DIFFERENTIATION_DATE)
)

select t.year as year, t.max_size - a.size_of_colony as year_dev, a.id
from ecoli_data a, temp t
where 1=1
and t.year = year(a.DIFFERENTIATION_DATE)
order by year, year_dev asc