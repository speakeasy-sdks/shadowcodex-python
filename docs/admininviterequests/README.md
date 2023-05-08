# admin_invite_requests

### Available Operations

* [admin_invite_requests_approve](#admin_invite_requests_approve) - Approve a workspace invite request.
* [admin_invite_requests_deny](#admin_invite_requests_deny) - Deny a workspace invite request.
* [admin_invite_requests_list](#admin_invite_requests_list) - List all pending workspace invite requests.

## admin_invite_requests_approve

Approve a workspace invite request.

API method documentation
<https://api.slack.com/methods/admin.inviteRequests.approve>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminInviteRequestsApproveRequest(
    request_body=operations.AdminInviteRequestsApproveApplicationJSON(
        invite_request_id='nostrum',
        team_id='hic',
    ),
    token='recusandae',
)

res = s.admin_invite_requests.admin_invite_requests_approve(req, operations.AdminInviteRequestsApproveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_invite_requests_deny

Deny a workspace invite request.

API method documentation
<https://api.slack.com/methods/admin.inviteRequests.deny>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminInviteRequestsDenyRequest(
    request_body=operations.AdminInviteRequestsDenyApplicationJSON(
        invite_request_id='omnis',
        team_id='facilis',
    ),
    token='perspiciatis',
)

res = s.admin_invite_requests.admin_invite_requests_deny(req, operations.AdminInviteRequestsDenySecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_invite_requests_list

List all pending workspace invite requests.

API method documentation
<https://api.slack.com/methods/admin.inviteRequests.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminInviteRequestsListRequest(
    cursor='voluptatem',
    limit=783645,
    team_id='consequuntur',
    token='blanditiis',
)

res = s.admin_invite_requests.admin_invite_requests_list(req, operations.AdminInviteRequestsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
