# admin_users

### Available Operations

* [admin_users_assign](#admin_users_assign) - Add an Enterprise user to a workspace.
* [admin_users_invite](#admin_users_invite) - Invite a user to a workspace.
* [admin_users_list](#admin_users_list) - List users on a workspace
* [admin_users_remove](#admin_users_remove) - Remove a user from a workspace.
* [admin_users_set_admin](#admin_users_set_admin) - Set an existing guest, regular user, or owner to be an admin user.
* [admin_users_set_expiration](#admin_users_set_expiration) - Set an expiration for a guest user
* [admin_users_set_owner](#admin_users_set_owner) - Set an existing guest, regular user, or admin user to be a workspace owner.
* [admin_users_set_regular](#admin_users_set_regular) - Set an existing guest user, admin user, or owner to be a regular user.

## admin_users_assign

Add an Enterprise user to a workspace.

API method documentation
<https://api.slack.com/methods/admin.users.assign>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersAssignRequest(
    request_body=operations.AdminUsersAssignApplicationJSON(
        channel_ids='asperiores',
        is_restricted=False,
        is_ultra_restricted=False,
        team_id='nihil',
        user_id='ipsum',
    ),
    token='voluptate',
)

res = s.admin_users.admin_users_assign(req, operations.AdminUsersAssignSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_invite

Invite a user to a workspace.

API method documentation
<https://api.slack.com/methods/admin.users.invite>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersInviteRequest(
    request_body=operations.AdminUsersInviteApplicationJSON(
        channel_ids='id',
        custom_message='saepe',
        email='Brigitte75@gmail.com',
        guest_expiration_ts='accusamus',
        is_restricted=False,
        is_ultra_restricted=False,
        real_name='ad',
        resend=False,
        team_id='saepe',
    ),
    token='suscipit',
)

res = s.admin_users.admin_users_invite(req, operations.AdminUsersInviteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_list

List users on a workspace

API method documentation
<https://api.slack.com/methods/admin.users.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersListRequest(
    cursor='deserunt',
    limit=588317,
    team_id='minima',
    token='repellendus',
)

res = s.admin_users.admin_users_list(req, operations.AdminUsersListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_remove

Remove a user from a workspace.

API method documentation
<https://api.slack.com/methods/admin.users.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersRemoveRequest(
    request_body=operations.AdminUsersRemoveApplicationJSON(
        team_id='totam',
        user_id='similique',
    ),
    token='alias',
)

res = s.admin_users.admin_users_remove(req, operations.AdminUsersRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_set_admin

Set an existing guest, regular user, or owner to be an admin user.

API method documentation
<https://api.slack.com/methods/admin.users.setAdmin>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersSetAdminRequest(
    request_body=operations.AdminUsersSetAdminApplicationJSON(
        team_id='at',
        user_id='quaerat',
    ),
    token='tempora',
)

res = s.admin_users.admin_users_set_admin(req, operations.AdminUsersSetAdminSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_set_expiration

Set an expiration for a guest user

API method documentation
<https://api.slack.com/methods/admin.users.setExpiration>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersSetExpirationRequest(
    request_body=operations.AdminUsersSetExpirationApplicationJSON(
        expiration_ts=425451,
        team_id='quod',
        user_id='officiis',
    ),
    token='qui',
)

res = s.admin_users.admin_users_set_expiration(req, operations.AdminUsersSetExpirationSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_set_owner

Set an existing guest, regular user, or admin user to be a workspace owner.

API method documentation
<https://api.slack.com/methods/admin.users.setOwner>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersSetOwnerRequest(
    request_body=operations.AdminUsersSetOwnerApplicationJSON(
        team_id='dolorum',
        user_id='a',
    ),
    token='esse',
)

res = s.admin_users.admin_users_set_owner(req, operations.AdminUsersSetOwnerSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_users_set_regular

Set an existing guest user, admin user, or owner to be a regular user.

API method documentation
<https://api.slack.com/methods/admin.users.setRegular>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsersSetRegularRequest(
    request_body=operations.AdminUsersSetRegularApplicationJSON(
        team_id='harum',
        user_id='iusto',
    ),
    token='ipsum',
)

res = s.admin_users.admin_users_set_regular(req, operations.AdminUsersSetRegularSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
