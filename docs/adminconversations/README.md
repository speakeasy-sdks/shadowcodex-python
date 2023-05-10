# admin_conversations

### Available Operations

* [admin_conversations_archive](#admin_conversations_archive) - Archive a public or private channel.
* [admin_conversations_convert_to_private](#admin_conversations_convert_to_private) - Convert a public channel to a private channel.
* [admin_conversations_create](#admin_conversations_create) - Create a public or private channel-based conversation.
* [admin_conversations_delete](#admin_conversations_delete) - Delete a public or private channel.
* [admin_conversations_disconnect_shared](#admin_conversations_disconnect_shared) - Disconnect a connected channel from one or more workspaces.
* [admin_conversations_get_conversation_prefs](#admin_conversations_get_conversation_prefs) - Get conversation preferences for a public or private channel.
* [admin_conversations_get_teams](#admin_conversations_get_teams) - Get all the workspaces a given public or private channel is connected to within this Enterprise org.
* [admin_conversations_invite](#admin_conversations_invite) - Invite a user to a public or private channel.
* [admin_conversations_rename](#admin_conversations_rename) - Rename a public or private channel.
* [admin_conversations_search](#admin_conversations_search) - Search for public or private channels in an Enterprise organization.
* [admin_conversations_set_conversation_prefs](#admin_conversations_set_conversation_prefs) - Set the posting permissions for a public or private channel.
* [admin_conversations_set_teams](#admin_conversations_set_teams) - Set the workspaces in an Enterprise grid org that connect to a public or private channel.
* [admin_conversations_unarchive](#admin_conversations_unarchive) - Unarchive a public or private channel.

## admin_conversations_archive

Archive a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.archive>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsArchiveRequest(
    request_body=operations.AdminConversationsArchiveApplicationJSON(
        channel_id='magnam',
    ),
    token='distinctio',
)

res = s.admin_conversations.admin_conversations_archive(req, operations.AdminConversationsArchiveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_archive_schema is not None:
    # handle response
```

## admin_conversations_convert_to_private

Convert a public channel to a private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.convertToPrivate>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsConvertToPrivateRequest(
    request_body=operations.AdminConversationsConvertToPrivateApplicationJSON(
        channel_id='id',
    ),
    token='labore',
)

res = s.admin_conversations.admin_conversations_convert_to_private(req, operations.AdminConversationsConvertToPrivateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_convert_to_private_schema is not None:
    # handle response
```

## admin_conversations_create

Create a public or private channel-based conversation.

API method documentation
<https://api.slack.com/methods/admin.conversations.create>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsCreateRequest(
    request_body=operations.AdminConversationsCreateApplicationJSON(
        description='labore',
        is_private=False,
        name='Ada Rohan',
        org_wide=False,
        team_id='aspernatur',
    ),
    token='architecto',
)

res = s.admin_conversations.admin_conversations_create(req, operations.AdminConversationsCreateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_create_schema is not None:
    # handle response
```

## admin_conversations_delete

Delete a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.delete>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsDeleteRequest(
    request_body=operations.AdminConversationsDeleteApplicationJSON(
        channel_id='magnam',
    ),
    token='et',
)

res = s.admin_conversations.admin_conversations_delete(req, operations.AdminConversationsDeleteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_delete_schema is not None:
    # handle response
```

## admin_conversations_disconnect_shared

Disconnect a connected channel from one or more workspaces.

API method documentation
<https://api.slack.com/methods/admin.conversations.disconnectShared>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsDisconnectSharedRequest(
    request_body=operations.AdminConversationsDisconnectSharedApplicationJSON(
        channel_id='excepturi',
        leaving_team_ids='ullam',
    ),
    token='provident',
)

res = s.admin_conversations.admin_conversations_disconnect_shared(req, operations.AdminConversationsDisconnectSharedSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_rename_schema is not None:
    # handle response
```

## admin_conversations_get_conversation_prefs

Get conversation preferences for a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.getConversationPrefs>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsGetConversationPrefsRequest(
    channel_id='quos',
    token='sint',
)

res = s.admin_conversations.admin_conversations_get_conversation_prefs(req, operations.AdminConversationsGetConversationPrefsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_get_conversation_prefs_schema is not None:
    # handle response
```

## admin_conversations_get_teams

Get all the workspaces a given public or private channel is connected to within this Enterprise org.

API method documentation
<https://api.slack.com/methods/admin.conversations.getTeams>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsGetTeamsRequest(
    channel_id='accusantium',
    cursor='mollitia',
    limit=968962,
    token='mollitia',
)

res = s.admin_conversations.admin_conversations_get_teams(req, operations.AdminConversationsGetTeamsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_get_teams_schema is not None:
    # handle response
```

## admin_conversations_invite

Invite a user to a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.invite>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsInviteRequest(
    request_body=operations.AdminConversationsInviteApplicationJSON(
        channel_id='ad',
        user_ids='eum',
    ),
    token='dolor',
)

res = s.admin_conversations.admin_conversations_invite(req, operations.AdminConversationsInviteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_invite_schema is not None:
    # handle response
```

## admin_conversations_rename

Rename a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.rename>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsRenameRequest(
    request_body=operations.AdminConversationsRenameApplicationJSON(
        channel_id='necessitatibus',
        name='Vivian Boyle',
    ),
    token='debitis',
)

res = s.admin_conversations.admin_conversations_rename(req, operations.AdminConversationsRenameSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_rename_schema is not None:
    # handle response
```

## admin_conversations_search

Search for public or private channels in an Enterprise organization.

API method documentation
<https://api.slack.com/methods/admin.conversations.search>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsSearchRequest(
    cursor='eius',
    limit=806194,
    query='deleniti',
    search_channel_types='facilis',
    sort='in',
    sort_dir='architecto',
    team_ids='architecto',
    token='repudiandae',
)

res = s.admin_conversations.admin_conversations_search(req, operations.AdminConversationsSearchSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_search_schema is not None:
    # handle response
```

## admin_conversations_set_conversation_prefs

Set the posting permissions for a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.setConversationPrefs>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsSetConversationPrefsRequest(
    request_body=operations.AdminConversationsSetConversationPrefsApplicationJSON(
        channel_id='ullam',
        prefs='expedita',
    ),
    token='nihil',
)

res = s.admin_conversations.admin_conversations_set_conversation_prefs(req, operations.AdminConversationsSetConversationPrefsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_set_conversation_prefs_schema is not None:
    # handle response
```

## admin_conversations_set_teams

Set the workspaces in an Enterprise grid org that connect to a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.setTeams>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsSetTeamsRequest(
    request_body=operations.AdminConversationsSetTeamsApplicationJSON(
        channel_id='repellat',
        org_channel=False,
        target_team_ids='quibusdam',
        team_id='sed',
    ),
    token='saepe',
)

res = s.admin_conversations.admin_conversations_set_teams(req, operations.AdminConversationsSetTeamsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_conversations_unarchive

Unarchive a public or private channel.

API method documentation
<https://api.slack.com/methods/admin.conversations.unarchive>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsUnarchiveRequest(
    request_body=operations.AdminConversationsUnarchiveApplicationJSON(
        channel_id='pariatur',
    ),
    token='accusantium',
)

res = s.admin_conversations.admin_conversations_unarchive(req, operations.AdminConversationsUnarchiveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_unarchive_schema is not None:
    # handle response
```
