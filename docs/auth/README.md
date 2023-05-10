# auth

### Available Operations

* [auth_revoke](#auth_revoke) - Revokes a token.
* [auth_test](#auth_test) - Checks authentication & identity.

## auth_revoke

Revokes a token.

API method documentation
<https://api.slack.com/methods/auth.revoke>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AuthRevokeRequest(
    test=False,
    token='facilis',
)

res = s.auth.auth_revoke(req, operations.AuthRevokeSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.auth_revoke_schema is not None:
    # handle response
```

## auth_test

Checks authentication & identity.

API method documentation
<https://api.slack.com/methods/auth.test>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AuthTestRequest(
    token='aliquid',
)

res = s.auth.auth_test(req, operations.AuthTestSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.auth_test_success_schema is not None:
    # handle response
```
