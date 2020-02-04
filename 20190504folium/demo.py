from requests_html import HTMLSession
import requests
url = 'http://www.gsxt.gov.cn/corp-query-search-advancetest.html?searchword=%E6%A0%BC%E5%8A%9B&tab=ent_tab&cStatus=0&eYear=0&area=0&filter=0&province=100000'
headers = {'Referer': 'http://www.gsxt.gov.cn/corp-query-search-1.html',
           'X-Requested-With': 'XMLHttpRequest',

    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
cookies = {'Cookie': '__jsluid=35f4a70749fff82dab9b8cda948fd3ba; __jsl_clearance=1556719025.565|0|xy2Jh94Amm1ptYdnwuweYXE%2FraI%3D; SECTOKEN=7147314018982298164; UM_distinctid=16a73af4642296-0673f55387e06c-366b7e03-ff000-16a73af46439d5; CNZZDATA1261033118=1780182076-1556713863-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1556713863; tlb_cookie=S172.16.12.114; gsxtBrowseHistory1=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219GEDDDDGEDED%40DDDDFFDD%40DCFFDDFEBSXS%11%1A%00%1A%15%19%11SNS%E4%B9%BE%E6%B4%83%E7%BF%BA%E6%A1%88%E5%8B%AF%E8%BC%8F%E5%91%BC%E9%86%A5%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEEGDXS%02%1D%07%1D%00%00%1D%19%11SNEAABCEMEDFGBG%09; JSESSIONID=1169270D40D08301507825D7323CF429-n1:4'}
resp = requests.get(url, headers=headers, cookies=cookies)
print(resp.text)