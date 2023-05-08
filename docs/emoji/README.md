# emoji

### Available Operations

* [emoji_list](#emoji_list) - Lists custom emoji for a team.

## emoji_list

Lists custom emoji for a team.

API method documentation
<https://api.slack.com/methods/emoji.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.EmojiListRequest(
    token='aperiam',
)

res = s.emoji.emoji_list(req, operations.EmojiListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
