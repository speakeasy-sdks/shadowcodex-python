# rtm

### Available Operations

* [rtm_connect](#rtm_connect) - Starts a Real Time Messaging session.

## rtm_connect

Starts a Real Time Messaging session.

API method documentation
<https://api.slack.com/methods/rtm.connect>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.RtmConnectRequest(
    batch_presence_aware=False,
    presence_sub=False,
    token='esse',
)

res = s.rtm.rtm_connect(req, operations.RtmConnectSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.rtm_connect_schema is not None:
    # handle response
```
