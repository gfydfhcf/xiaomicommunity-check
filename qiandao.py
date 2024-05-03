import requests
import datetime

url = "https://api.vip.miui.com/mtop/planet/vip/user/checkinV2"
params = {
    "ref": "vipAccountShortcut",
    "pathname": "/mio/checkIn",
    "version": "dev.240402",
    "miui_version": "V13.0.7.0.RKCCNXM",
    "android_version": "11",
    "oaid": "1494a75ac79176e2",
    "device": "sagit",
    "miui_big_version": "V130",
    "model": "MI 6",
    "androidVersion": "11",
    "miuiBigVersion": "V130"
}

headers = {
    "Host": "api.vip.miui.com",
    "Connection": "keep-alive",
    "Content-Length": "578",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Android WebView\";v=\"122\"",
    "Accept": "application/json",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryKqqsUHKQPPCuOXNT",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; MI 6 Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.15 Mobile Safari/537.36XiaoMi/HybridView/ app/vipaccount/dev.240402",
    "sec-ch-ua-platform": "\"Android\"",
    "Origin": "https://web.vip.miui.com",
    "X-Requested-With": "com.xiaomi.vipaccount",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://web.vip.miui.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "cUserId=d2wpGijtf5vo6NPvvEPznKAQl8w; miui_vip_w_serviceToken=LWo0bv4LE7mLUpSBrGMJeIYbHf0BfuZosS9DwuWjV6T5Vj4uMN0FAOE42fIbQe6QvsndYz96ZRecNouo18xOkpVsqRn8b6X/gi89Ic/nd9trJUY/sz+laayA6WaGpQmzDUi6ywiXPgEUTflUaqHE14JcBb8sSHnFkphK/T3TEQIZK25daKRrIwH8Xmu2e3xq9C9l7P/OwCLmlG2PC/NLtExV+rCMKmA5a83G+U5o5UeJvSh5efMZ6U7qFLLhnAAt9ITgZF97wiNT+OvOJbDbuw==; miui_vip_w_slh=hqgSkCZV9MFlp2Za719hya9Ibvs=; miui_vip_w_ph=N8kkVbzaQkfkawzPNoLM1g==; miui_vip_ph=ffZWWbTiyLxYgemZe4cBuw==; miui_vip_slh=kV/+ejLi6ZhI4F4dCxhPqa0ie0c=; miui_vip_serviceToken=Iiu8vRUU8tQufjvOpM+vNghjkBlkQYUYvKIbmSowymMXk9LJl0qBYndUqQ4UJ4z8aKzK+Gj+K/ZKAroOlohWbcBChHw4hj7Z74xpbaFIW1R6eEOV/wV3dByCsCBITHa/gNpkVXtqOQl8ABsdF6BgyVCK500JLBj5uiww75wuAkVBYekogXObnH5oNmGKQGciUKADMmMrFbKnAx1YuF6sE9mbbEvsu//GDyB42lg0Kzrz6dME5YB+g5Q23ZFHpabcNRhzPXVXYfBgfrqoG7+BQg=="
}

body = """------WebKitFormBoundaryKqqsUHKQPPCuOXNT
Content-Disposition: form-data; name="token"

4DVaoR/4usyBp/M6N4ee48Rj3JKcp4ssRnmhyRTkUPm+OBGR9sbEZkwr6cboUsTtJ+iIkcOGbhfR4TrLcw6KsrcWCe5dwCXFHrNIqsc0xYCjPyKAv4FbdqromFqVkz4Sw5dZnox7Forfx+rhJls+wKnuas8F7n+DcQRCne1BC3Wd6Fl5YIED2EuAgYXVnynpmG0v/RGiGJc/uErPta80EQOVD1Vj0oG/0PotOciEgQFKdPFWFHeSuYSWHaDLR7h49yP7jsfQu4VVi0ip2PuC4WH4YIVrVyWdNfW4WwWl3wf11XuWg0XIFeaBqIrwTGSf
------WebKitFormBoundaryKqqsUHKQPPCuOXNT
Content-Disposition: form-data; name="miui_vip_ph"

ffZWWbTiyLxYgemZe4cBuw==
------WebKitFormBoundaryKqqsUHKQPPCuOXNT--"""

response = requests.post(url, params=params, headers=headers, data=body)

log_file_path = "checkin_log.txt"  # 设置日志文件路径

if response.status_code == 200:
    response_data = response.json()
    if response_data.get("message") == "success":
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = "签到成功，时间：{}".format(current_time)
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = "签到失败，时间：{}".format(current_time)
else:
    log_message = "请求失败，状态码：{}".format(response.status_code)

with open(log_file_path, "a") as log_file:
    log_file.write(log_message + "\n")
