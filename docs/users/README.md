# users

### Available Operations

* [users_conversations](#users_conversations) - List conversations the calling user may access.
* [users_delete_photo](#users_delete_photo) - Delete the user profile photo
* [users_get_presence](#users_get_presence) - Gets user presence information.
* [users_identity](#users_identity) - Get a user's identity.
* [users_info](#users_info) - Gets information about a user.
* [users_list](#users_list) - Lists all users in a Slack team.
* [users_lookup_by_email](#users_lookup_by_email) - Find a user with an email address.
* [users_profile_get](#users_profile_get) - Retrieves a user's profile information.
* [users_profile_set](#users_profile_set) - Set the profile information for a user.
* [users_set_active](#users_set_active) - Marked a user as active. Deprecated and non-functional.
* [users_set_photo](#users_set_photo) - Set the user profile photo
* [users_set_presence](#users_set_presence) - Manually sets user presence.

## users_conversations

List conversations the calling user may access.

API method documentation
<https://api.slack.com/methods/users.conversations>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersConversationsRequest(
    cursor='aliquam',
    exclude_archived=False,
    limit=320565,
    token='repellat',
    types='alias',
    user='corporis',
)

res = s.users.users_conversations(req, operations.UsersConversationsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_conversations_success_schema is not None:
    # handle response
```

## users_delete_photo

Delete the user profile photo

API method documentation
<https://api.slack.com/methods/users.deletePhoto>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersDeletePhotoRequestBody(
    token='perspiciatis',
)

res = s.users.users_delete_photo(req, operations.UsersDeletePhotoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_delete_photo_schema is not None:
    # handle response
```

## users_get_presence

Gets user presence information.

API method documentation
<https://api.slack.com/methods/users.getPresence>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersGetPresenceRequest(
    token='nihil',
    user='mollitia',
)

res = s.users.users_get_presence(req, operations.UsersGetPresenceSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.api_method_users_get_presence is not None:
    # handle response
```

## users_identity

Get a user's identity.

API method documentation
<https://api.slack.com/methods/users.identity>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersIdentityRequest(
    token='voluptas',
)

res = s.users.users_identity(req, operations.UsersIdentitySecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_identity_schema is not None:
    # handle response
```

## users_info

Gets information about a user.

API method documentation
<https://api.slack.com/methods/users.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersInfoRequest(
    include_locale=False,
    token='alias',
    user='maiores',
)

res = s.users.users_info(req, operations.UsersInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_info_success_schema is not None:
    # handle response
```

## users_list

Lists all users in a Slack team.

API method documentation
<https://api.slack.com/methods/users.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersListRequest(
    cursor='reiciendis',
    include_locale=False,
    limit=174658,
    token='id',
)

res = s.users.users_list(req, operations.UsersListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_list_schema is not None:
    # handle response
```

## users_lookup_by_email

Find a user with an email address.

API method documentation
<https://api.slack.com/methods/users.lookupByEmail>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersLookupByEmailRequest(
    email='Elda6@gmail.com',
    token='recusandae',
)

res = s.users.users_lookup_by_email(req, operations.UsersLookupByEmailSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_lookup_by_email_success_schema is not None:
    # handle response
```

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
    token='omnis',
    user='quaerat',
)

res = s.users.users_profile_get(req, operations.UsersProfileGetSecurity(
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
        name='Carla Graham',
        profile='debitis',
        user='laudantium',
        value='eum',
    ),
    token='nemo',
)

res = s.users.users_profile_set(req, operations.UsersProfileSetSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_profile_set_schema is not None:
    # handle response
```

## users_set_active

Marked a user as active. Deprecated and non-functional.

API method documentation
<https://api.slack.com/methods/users.setActive>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersSetActiveRequest(
    token='recusandae',
)

res = s.users.users_set_active(req, operations.UsersSetActiveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_set_active_schema is not None:
    # handle response
```

## users_set_photo

Set the user profile photo

API method documentation
<https://api.slack.com/methods/users.setPhoto>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersSetPhotoRequestBody(
    crop_w='esse',
    crop_x='provident',
    crop_y='quis',
    image='eum',
    token='reiciendis',
)

res = s.users.users_set_photo(req, operations.UsersSetPhotoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_set_photo_schema is not None:
    # handle response
```

## users_set_presence

Manually sets user presence.

API method documentation
<https://api.slack.com/methods/users.setPresence>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.UsersSetPresenceRequest(
    request_body=operations.UsersSetPresenceApplicationJSON(
        presence='provident',
    ),
    token='aspernatur',
)

res = s.users.users_set_presence(req, operations.UsersSetPresenceSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.users_set_presence_schema is not None:
    # handle response
```
