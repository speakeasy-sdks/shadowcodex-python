# bots

### Available Operations

* [bots_info](#bots_info) - Gets information about a bot user.

## bots_info

Gets information about a bot user.

API method documentation
<https://api.slack.com/methods/bots.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.BotsInfoRequest(
    bot='quam',
    token='molestias',
)

res = s.bots.bots_info(req, operations.BotsInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.bots_info_schema is not None:
    # handle response
```
