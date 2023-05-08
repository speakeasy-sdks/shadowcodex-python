# search

### Available Operations

* [search_messages](#search_messages) - Searches for messages matching a query.

## search_messages

Searches for messages matching a query.

API method documentation
<https://api.slack.com/methods/search.messages>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.SearchMessagesRequest(
    count=227759,
    highlight=False,
    page=826825,
    query='ea',
    sort='atque',
    sort_dir='error',
    token='officiis',
)

res = s.search.search_messages(req, operations.SearchMessagesSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
