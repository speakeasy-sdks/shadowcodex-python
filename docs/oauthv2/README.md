# oauth_v2

### Available Operations

* [oauth_v2_access](#oauth_v2_access) - Exchanges a temporary OAuth verifier code for an access token.

## oauth_v2_access

Exchanges a temporary OAuth verifier code for an access token.

API method documentation
<https://api.slack.com/methods/oauth.v2.access>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.OauthV2AccessRequest(
    client_id='sed',
    client_secret='sit',
    code='vel',
    redirect_uri='nostrum',
)

res = s.oauth_v2.oauth_v2_access(req, operations.OauthV2AccessSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
