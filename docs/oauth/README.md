# oauth

### Available Operations

* [oauth_access](#oauth_access) - Exchanges a temporary OAuth verifier code for an access token.
* [oauth_token](#oauth_token) - Exchanges a temporary OAuth verifier code for a workspace token.
* [oauth_v2_access](#oauth_v2_access) - Exchanges a temporary OAuth verifier code for an access token.

## oauth_access

Exchanges a temporary OAuth verifier code for an access token.

API method documentation
<https://api.slack.com/methods/oauth.access>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.OauthAccessRequest(
    client_id='magnam',
    client_secret='consequatur',
    code='esse',
    redirect_uri='ipsam',
    single_channel=False,
)

res = s.oauth.oauth_access(req, operations.OauthAccessSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## oauth_token

Exchanges a temporary OAuth verifier code for a workspace token.

API method documentation
<https://api.slack.com/methods/oauth.token>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.OauthTokenRequest(
    client_id='sit',
    client_secret='voluptatum',
    code='quas',
    redirect_uri='repudiandae',
    single_channel=False,
)

res = s.oauth.oauth_token(req, operations.OauthTokenSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

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
    client_id='corporis',
    client_secret='et',
    code='blanditiis',
    redirect_uri='ex',
)

res = s.oauth.oauth_v2_access(req, operations.OauthV2AccessSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
