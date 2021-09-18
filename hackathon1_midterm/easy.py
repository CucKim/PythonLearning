# 1
from datetime import datetime


def day_diff(release_date, code_complete_day):
    from datetime import datetime
    rd="19/12/2021"
    date_format="%d/%m/%Y"
    release_date = datetime.strptime(rd,date_format)
    cd= "2021-17-05"
    date_format1="%Y/%d/%m"
    code_complete_day = datetime.strptime(cd,date_format1)
    result=release_date-code_complete_day
    return result
# 2
def alpha_num(sentence):
    import re
    str = sentence.split()
    result_str=re.findall("\d+[a-zA-Z]+|[a-zA-Z]*\d+",sentence)
    return result_str
    
