for i in range(1,11):
    print(i)
     #conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(1) > div.rank_cntt > div.rank_info > p > a
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child({i}) > div.rank_cntt > div.rank_info > p > a')
print(f'{i}위 {title.text}')