import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Cookie': 'acw_tc=276077a416644581487861080eba773c0d53fa0045bed504aaa30aa06c8dc3; xq_a_token=25916c3bfec27272745f6070d664a48d4b10d322; xqat=25916c3bfec27272745f6070d664a48d4b10d322; xq_r_token=2242d232b1aa6ffb6d9569d53e067311db16c12c; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2NzAwMjE2NSwiY3RtIjoxNjY0NDU4MTEzMjgzLCJjaWQiOiJkOWQwbjRBWnVwIn0.nAaBENJrrhuRtuLa4U14R2wfNhUHEH9oY3y6Fb-IIFPBd1Y7S9F2f5ie0EtueGQLTITVwbvLMCBlQxgXFDIVbZ5KOP8zOryY38tKu3ercuFLL7gjwVMnRjr_PdcU0pu1oDMuBHY_-HUhLFnxUnTpRtH04vsRxDeVsJKTn-mtQU_x-o3KQn6TXOPhjr6bzfkiOnxqAXWdeUEjVlBqzgupwlCabHybn9Hi6qr7Hud4oGL_S9xFcFbUGmUEDKKLMz94zxWY8sk1u63TE31n3OusNPY5meknOVUTwKBL7NkmqB0U57lOICBcrBMukIghGytB1Lq4MbIZ1AqtUPXc9pldNw; u=121664458148822; Hm_lvt_1db88642e346389874251b5a1eded6e3=1664458150; device_id=d639b659196d82603f9eabf774818000; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1664458630'
}

url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=401598&size=15'
response = requests.get(url, headers=headers)  # 返回JSON字符串
req = response.json()

print(type(req))
print(req)
