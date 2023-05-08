# admin_users_session

### Available Operations

* [admin_users_session_invalidate](#admin_users_session_invalidate) - Invalidate a single session for a user by session_id
* [admin_users_session_reset](#admin_users_session_reset) - Wipes all valid sessions on all devices for a given user

## admin_users_session_invalidate

Invalidate a single session for a user by session_id

API method documentation
<https://api.slack.com/methods/admin.users.session.invalidate>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersSessionInvalidateRequest(
    request_body=operations.AdminUsersSessionInvalidateApplicationJSON(
        session_id=788740,
        team_id='tenetur',
    ),
    token='amet',
)

res = s.admin_users_session.admin_users_session_invalidate(req, operations.AdminUsersSessionInvalidateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_session_reset

Wipes all valid sessions on all devices for a given user

API method documentation
<https://api.slack.com/methods/admin.users.session.reset>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersSessionResetRequest(
    request_body=operations.AdminUsersSessionResetApplicationJSON(
        mobile_only=False,
        user_id='tempore',
        web_only=False,
    ),
    token='accusamus',
)

res = s.admin_users_session.admin_users_session_reset(req, operations.AdminUsersSessionResetSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
