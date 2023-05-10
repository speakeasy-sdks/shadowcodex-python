# usergroups_users

### Available Operations

* [usergroups_users_list](#usergroups_users_list) - List all users in a User Group
* [usergroups_users_update](#usergroups_users_update) - Update the list of users for a User Group

## usergroups_users_list

List all users in a User Group

API method documentation
<https://api.slack.com/methods/usergroups.users.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsergroupsUsersListRequest(
    include_disabled=False,
    token='ratione',
    usergroup='laborum',
)

res = s.usergroups_users.usergroups_users_list(req, operations.UsergroupsUsersListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_users_list_schema is not None:
    # handle response
```

## usergroups_users_update

Update the list of users for a User Group

API method documentation
<https://api.slack.com/methods/usergroups.users.update>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsergroupsUsersUpdateRequest(
    request_body=operations.UsergroupsUsersUpdateApplicationJSON(
        include_count=False,
        usergroup='distinctio',
        users='voluptatum',
    ),
    token='rem',
)

res = s.usergroups_users.usergroups_users_update(req, operations.UsergroupsUsersUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_users_update_schema is not None:
    # handle response
```
