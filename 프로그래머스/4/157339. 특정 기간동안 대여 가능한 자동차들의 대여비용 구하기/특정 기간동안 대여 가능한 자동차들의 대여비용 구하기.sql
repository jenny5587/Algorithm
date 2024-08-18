SELECT car_id, a.car_type, round(daily_fee * 30 *((100-discount_rate)/100),0) AS fee
FROM (select * from CAR_RENTAL_COMPANY_CAR where car_type in ('세단', 'SUV')) as a
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN b
ON a.car_type = b.car_type
and b.DURATION_TYPE = '30일 이상'
where a.car_id not in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                      where ('2022-11-01' between start_date and end_date)
                      or ('2022-11-30' between start_date and end_date))
GROUP BY a.car_id
having fee >= 500000 and fee < 2000000
order by fee desc, a.car_type, a.car_id desc