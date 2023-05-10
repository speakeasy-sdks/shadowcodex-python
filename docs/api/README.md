# api

### Available Operations

* [api_test](#api_test) - Checks API calling code.

## api_test

Checks API calling code.

API method documentation
<https://api.slack.com/methods/api.test>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.APITestRequest(
    error='numquam',
    foo='enim',
)

res = s.api.api_test(req, operations.APITestSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.api_test_success_schema is not None:
    # handle response
```
