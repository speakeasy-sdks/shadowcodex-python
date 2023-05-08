# admin_conversations_restrict_access

### Available Operations

* [admin_conversations_restrict_access_add_group](#admin_conversations_restrict_access_add_group) - Add an allowlist of IDP groups for accessing a channel
* [admin_conversations_restrict_access_list_groups](#admin_conversations_restrict_access_list_groups) - List all IDP Groups linked to a channel
* [admin_conversations_restrict_access_remove_group](#admin_conversations_restrict_access_remove_group) - Remove a linked IDP group linked from a private channel

## admin_conversations_restrict_access_add_group

Add an allowlist of IDP groups for accessing a channel

API method documentation
<https://api.slack.com/methods/admin.conversations.restrictAccess.addGroup>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsRestrictAccessAddGroupRequestBody(
    channel_id='quo',
    group_id='illum',
    team_id='pariatur',
    token='maxime',
)

res = s.admin_conversations_restrict_access.admin_conversations_restrict_access_add_group(req, operations.AdminConversationsRestrictAccessAddGroupSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_conversations_restrict_access_list_groups

List all IDP Groups linked to a channel

API method documentation
<https://api.slack.com/methods/admin.conversations.restrictAccess.listGroups>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsRestrictAccessListGroupsRequest(
    channel_id='ea',
    team_id='excepturi',
    token='odit',
)

res = s.admin_conversations_restrict_access.admin_conversations_restrict_access_list_groups(req, operations.AdminConversationsRestrictAccessListGroupsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_conversations_restrict_access_remove_group

Remove a linked IDP group linked from a private channel

API method documentation
<https://api.slack.com/methods/admin.conversations.restrictAccess.removeGroup>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsRestrictAccessRemoveGroupRequestBody(
    channel_id='ea',
    group_id='accusantium',
    team_id='ab',
    token='maiores',
)

res = s.admin_conversations_restrict_access.admin_conversations_restrict_access_remove_group(req, operations.AdminConversationsRestrictAccessRemoveGroupSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
