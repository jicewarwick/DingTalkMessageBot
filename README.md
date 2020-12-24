# DingTalk Message Bot

## Usage:
``` python
from DingTalkMessageBot import DingTalkMessageBot

token = "****************************************************************"
secret = "*******************************************************************"

ding_messenger = DingTalkMessageBot(token, secret)

msg = 'test_message'
ding_messenger.send_message(msg)

```

OR

``` python
from DingTalkMessageBot import DingTalkMessageBot

ding_messenger = DingTalkMessageBot.from_config('config.json', 'test')

msg = 'test_message'
ding_messenger.send_message(msg)

```
