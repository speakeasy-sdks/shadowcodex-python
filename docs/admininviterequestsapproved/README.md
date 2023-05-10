# admin_invite_requests_approved

### Available Operations

* [admin_invite_requests_approved_list](#admin_invite_requests_approved_list) - List all approved workspace invite requests.

## admin_invite_requests_approved_list

List all approved workspace invite requests.

API method documentation
<https://api.slack.com/methods/admin.inviteRequests.approved.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminInviteRequestsApprovedListRequest(
    cursor='error',
    limit=50370,
    team_id='occaecati',
    token='rerum',
)

res = s.admin_invite_requests_approved.admin_invite_requests_approved_list(req, operations.AdminInviteRequestsApprovedListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
