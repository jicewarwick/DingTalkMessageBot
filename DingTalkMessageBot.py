import base64
import hashlib
import hmac
import json
import time
import urllib.parse

import requests


class DingTalkMessageBot(object):
    msg_template = {
        "msgtype": "text",
        "text": {
            "content": ""
        }
    }
    header = {
        'Content-Type': 'application/json',
        'Charset': 'UTF-8'
    }

    def __init__(self, token: str, secret: str = None):
        self.token = token
        self.secret = secret

    def _generate_url(self):
        if self.secret:
            timestamp = str(round(time.time() * 1000))
            secret_enc = self.secret.encode('utf-8')
            string_to_sign = '{}\n{}'.format(timestamp, self.secret)
            string_to_sign_enc = string_to_sign.encode('utf-8')
            hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
            sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
            return f'https://oapi.dingtalk.com/robot/send?access_token={self.token}&timestamp={timestamp}&sign={sign}'
        else:
            return f'https://oapi.dingtalk.com/robot/send?access_token={self.token}'

    def send_message(self, msg: str):
        info = self.msg_template.copy()
        info['text']['content'] = msg
        requests.post(self._generate_url(), json=info, headers=self.header)

    @classmethod
    def from_config(cls, json_loc: str, bot_name: str):
        with open(json_loc, 'r', encoding='utf-8') as f:
            config = json.load(f)

        assert 'ding_bot' in config.keys(), 'config file must contain entry "ding_bot"'
        assert bot_name in config['ding_bot'].keys(), f'config file does not contain {bot_name} in entry "ding_bot"'
        assert 'token' in config['ding_bot'][bot_name].keys(), f"config does not provide {bot_name}'s token"
        token = config['ding_bot'][bot_name]['token']

        if 'secret' in config['ding_bot'][bot_name].keys():
            secret = config['ding_bot'][bot_name]['secret']
        else:
            secret = None

        return cls(token, secret)
