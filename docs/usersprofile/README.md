# users_profile

### Available Operations

* [users_profile_get](#users_profile_get) - Retrieves a user's profile information.
* [users_profile_set](#users_profile_set) - Set the profile information for a user.

## users_profile_get

Retrieves a user's profile information.

API method documentation
<https://api.slack.com/methods/users.profile.get>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersProfileGetRequest(
    include_labels=False,
    token='ullam',
    user='quasi',
)

res = s.users_profile.users_profile_get(req, operations.UsersProfileGetSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_profile_get_schema is not None:
    # handle response
```

## users_profile_set

Set the profile information for a user.

API method documentation
<https://api.slack.com/methods/users.profile.set>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersProfileSetRequest(
    request_body=operations.UsersProfileSetApplicationJSON(
        name='Gordon O'Hara',
        profile='animi',
        user='ex',
        value='aliquid',
    ),
    token='accusantium',
)

res = s.users_profile.users_profile_set(req, operations.UsersProfileSetSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_profile_set_schema is not None:
    # handle response
```
