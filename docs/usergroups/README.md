# usergroups

### Available Operations

* [usergroups_create](#usergroups_create) - Create a User Group
* [usergroups_disable](#usergroups_disable) - Disable an existing User Group
* [usergroups_enable](#usergroups_enable) - Enable a User Group
* [usergroups_list](#usergroups_list) - List all User Groups for a team
* [usergroups_update](#usergroups_update) - Update an existing User Group
* [usergroups_users_list](#usergroups_users_list) - List all users in a User Group
* [usergroups_users_update](#usergroups_users_update) - Update the list of users for a User Group

## usergroups_create

Create a User Group

API method documentation
<https://api.slack.com/methods/usergroups.create>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsergroupsCreateRequest(
    request_body=operations.UsergroupsCreateApplicationJSON(
        channels='consequuntur',
        description='occaecati',
        handle='officiis',
        include_count=False,
        name='Arnold Ferry',
    ),
    token='consequuntur',
)

res = s.usergroups.usergroups_create(req, operations.UsergroupsCreateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_create_schema is not None:
    # handle response
```

## usergroups_disable

Disable an existing User Group

API method documentation
<https://api.slack.com/methods/usergroups.disable>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsergroupsDisableRequest(
    request_body=operations.UsergroupsDisableApplicationJSON(
        include_count=False,
        usergroup='fugit',
    ),
    token='id',
)

res = s.usergroups.usergroups_disable(req, operations.UsergroupsDisableSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_disable_schema is not None:
    # handle response
```

## usergroups_enable

Enable a User Group

API method documentation
<https://api.slack.com/methods/usergroups.enable>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsergroupsEnableRequest(
    request_body=operations.UsergroupsEnableApplicationJSON(
        include_count=False,
        usergroup='quis',
    ),
    token='reprehenderit',
)

res = s.usergroups.usergroups_enable(req, operations.UsergroupsEnableSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_enable_schema is not None:
    # handle response
```

## usergroups_list

List all User Groups for a team

API method documentation
<https://api.slack.com/methods/usergroups.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsergroupsListRequest(
    include_count=False,
    include_disabled=False,
    include_users=False,
    token='error',
)

res = s.usergroups.usergroups_list(req, operations.UsergroupsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_list_schema is not None:
    # handle response
```

## usergroups_update

Update an existing User Group

API method documentation
<https://api.slack.com/methods/usergroups.update>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsergroupsUpdateRequest(
    request_body=operations.UsergroupsUpdateApplicationJSON(
        channels='illo',
        description='corporis',
        handle='quidem',
        include_count=False,
        name='Ms. Melvin Thiel IV',
        usergroup='quae',
    ),
    token='molestiae',
)

res = s.usergroups.usergroups_update(req, operations.UsergroupsUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_update_schema is not None:
    # handle response
```

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
    token='eveniet',
    usergroup='qui',
)

res = s.usergroups.usergroups_users_list(req, operations.UsergroupsUsersListSecurity(
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
        usergroup='cum',
        users='iure',
    ),
    token='necessitatibus',
)

res = s.usergroups.usergroups_users_update(req, operations.UsergroupsUsersUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.usergroups_users_update_schema is not None:
    # handle response
```
