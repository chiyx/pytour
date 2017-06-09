#!/usr/bin/env python

# 通过聚划算品牌团异步接口获取品牌id和logo

import requests
import json

fetch_num = 0
apiUrl = ('https://ju.taobao.com/json/tg/ajaxGetBrandsV2.json'
          '?psize=100&includeForecast=true&page=')
brand_logo_dict = {}


def getApi():
    page = 1
    while page <= 11:
        yield apiUrl + str(page)
        page += 1

api_gen = getApi()
# 获取数据
for api in api_gen:
    resp = requests.get(api)
    resp.raise_for_status()
    data = resp.json()
    brandList = data['brandList']
    for brand in brandList:
        brand_logo_dict[brand['baseInfo']['brandId']] = (
            'https:' + brand['materials']['brandLogoUrl'] + '_180x90Q90.jpg'
        )
# 写入文件中
json_str = json.dumps(brand_logo_dict, ensure_ascii=False, indent=4)
with open('brand_logo_file.json', 'w') as rs_file:
    rs_file.write(json_str)
print('Done')
