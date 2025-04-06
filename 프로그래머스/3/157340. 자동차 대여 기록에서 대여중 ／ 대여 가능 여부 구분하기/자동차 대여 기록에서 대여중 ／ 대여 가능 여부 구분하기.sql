select car_id,
    case when max(case when '2022-10-16' between start_date and end_date then 1
                  else 0 end)=1 # 하나의 이력이라도 있으면 대여중
        then '대여중'
        else '대여 가능' 
    end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where 1=1
group by car_id #이력 한줄만 나오게 하기 위해서
order by car_id desc