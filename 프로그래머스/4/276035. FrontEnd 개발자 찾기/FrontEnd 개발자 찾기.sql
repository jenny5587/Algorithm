select id,email,first_name,last_name
from DEVELOPERS
where skill_code &(select sum(CODE) from SKILLCODES where CATEGORY = 'Front End')
order by id asc

# 특정 조건에 따라 플래그를 설정하거나 확인할 때 비트 연산자 사용
# 비트가 1일 때 해당 위치의 기술을 보유하고 있는 것으로 가정
# ex)
# (skill_code) & 10256
# 400 / 10256
# 2048 / 10256 해서 비트로 보유 여부 결정