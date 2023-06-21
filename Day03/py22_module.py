# 모듈 사용(2가지 방법, import / from ~ import)
# import datetime as dt
from datetime import datetime #as dt
from os import getcwd

# curr_date = datetime.datetime.now() -> datetime의 이름을 dt로 변경했기때문에 사용 못함
# curr_date = dt.datetime.now()
curr_date = datetime.now()
# curr_date = dt.now()
print(curr_date)

print(getcwd())