import requests
import json
from datetime import datetime
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hifiti_sign.log'),
        logging.StreamHandler()
    ]
)

class HifitiSign:
    def __init__(self):
        self.base_url = "https://www.hifiti.com"
        self.sign_url = f"{self.base_url}/sg_sign.htm"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Origin': self.base_url,
            'Referer': self.base_url,
            'X-Requested-With': 'XMLHttpRequest'
        })

    def set_cookies(self, cookies_str):
        """设置cookies"""
        try:
            cookies = {}
            for cookie in cookies_str.split(';'):
                if '=' in cookie:
                    key, value = cookie.strip().split('=', 1)
                    cookies[key.strip()] = value.strip()
            self.session.cookies.update(cookies)
            logging.info("Cookies设置成功")
            return True
        except Exception as e:
            logging.error(f"设置Cookies失败: {str(e)}")
            return False

    def sign(self):
        """执行签到"""
        try:
            response = self.session.post(
                self.sign_url,
                timeout=10
            )
            
            if response.status_code == 200:
                logging.info(f"签到请求发送成功，响应内容: {response.text}")
                return True
            else:
                logging.error(f"签到失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            logging.error(f"签到过程发生错误: {str(e)}")
            return False

def main():
    # 这里需要填入你的cookies
    cookies_str = open('cookie.txt', 'r').read()
    
    signer = HifitiSign()
    if signer.set_cookies(cookies_str):
        if signer.sign():
            logging.info("签到成功完成")
        else:
            logging.error("签到失败")
    else:
        logging.error("初始化失败")

if __name__ == "__main__":
    main() 