# admin_invite_requests_denied

### Available Operations

* [admin_invite_requests_denied_list](#admin_invite_requests_denied_list) - List all denied workspace invite requests.

## admin_invite_requests_denied_list

List all denied workspace invite requests.

API method documentation
<https://api.slack.com/methods/admin.inviteRequests.denied.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminInviteRequestsDeniedListRequest(
    cursor='adipisci',
    limit=992397,
    team_id='earum',
    token='modi',
)

res = s.admin_invite_requests_denied.admin_invite_requests_denied_list(req, operations.AdminInviteRequestsDeniedListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
