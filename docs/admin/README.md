# admin

### Available Operations

* [admin_apps_approve](#admin_apps_approve) - Approve an app for installation on a workspace.
* [admin_apps_approved_list](#admin_apps_approved_list) - List approved apps for an org or workspace.
* [admin_apps_requests_list](#admin_apps_requests_list) - List app requests for a team/workspace.
* [admin_apps_restrict](#admin_apps_restrict) - Restrict an app for installation on a workspace.
* [admin_apps_restricted_list](#admin_apps_restricted_list) - List restricted apps for an org or workspace.
* [admin_conversations_archive](#admin_conversations_archive) - Archive a public or private channel.
* [admin_conversations_convert_to_private](#admin_conversations_convert_to_private) - Convert a public channel to a private channel.
* [admin_conversations_create](#admin_conversations_create) - Create a public or private channel-based conversation.
* [admin_conversations_delete](#admin_conversations_delete) - Delete a public or private channel.
* [admin_conversations_disconnect_shared](#admin_conversations_disconnect_shared) - Disconnect a connected channel from one or more workspaces.
* [admin_conversations_ekm_list_original_connected_channel_info](#admin_conversations_ekm_list_original_connected_channel_info) - List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.
* [admin_conversations_get_conversation_prefs](#admin_conversations_get_conversation_prefs) - Get conversation preferences for a public or private channel.
* [admin_conversations_get_teams](#admin_conversations_get_teams) - Get all the workspaces a given public or private channel is connected to within this Enterprise org.
* [admin_conversations_invite](#admin_conversations_invite) - Invite a user to a public or private channel.
* [admin_conversations_rename](#admin_conversations_rename) - Rename a public or private channel.
* [admin_conversations_restrict_access_add_group](#admin_conversations_restrict_access_add_group) - Add an allowlist of IDP groups for accessing a channel
* [admin_conversations_restrict_access_list_groups](#admin_conversations_restrict_access_list_groups) - List all IDP Groups linked to a channel
* [admin_conversations_restrict_access_remove_group](#admin_conversations_restrict_access_remove_group) - Remove a linked IDP group linked from a private channel
* [admin_conversations_search](#admin_conversations_search) - Search for public or private channels in an Enterprise organization.
* [admin_conversations_set_conversation_prefs](#admin_conversations_set_conversation_prefs) - Set the posting permissions for a public or private channel.
* [admin_conversations_set_teams](#admin_conversations_set_teams) - Set the workspaces in an Enterprise grid org that connect to a public or private channel.
* [admin_conversations_unarchive](#admin_conversations_unarchive) - Unarchive a public or private channel.
* [admin_emoji_add](#admin_emoji_add) - Add an emoji.
* [admin_emoji_add_alias](#admin_emoji_add_alias) - Add an emoji alias.
* [admin_emoji_list](#admin_emoji_list) - List emoji for an Enterprise Grid organization.
* [admin_emoji_remove](#admin_emoji_remove) - Remove an emoji across an Enterprise Grid organization
* [admin_emoji_rename](#admin_emoji_rename) - Rename an emoji.
* [admin_invite_requests_approve](#admin_invite_requests_approve) - Approve a workspace invite request.
* [admin_invite_requests_approved_list](#admin_invite_requests_approved_list) - List all approved workspace invite requests.
* [admin_invite_requests_denied_list](#admin_invite_requests_denied_list) - List all denied workspace invite requests.
* [admin_invite_requests_deny](#admin_invite_requests_deny) - Deny a workspace invite request.
* [admin_invite_requests_list](#admin_invite_requests_list) - List all pending workspace invite requests.
* [admin_teams_admins_list](#admin_teams_admins_list) - List all of the admins on a given workspace.
* [admin_teams_create](#admin_teams_create) - Create an Enterprise team.
* [admin_teams_list](#admin_teams_list) - List all teams on an Enterprise organization
* [admin_teams_owners_list](#admin_teams_owners_list) - List all of the owners on a given workspace.
* [admin_teams_settings_info](#admin_teams_settings_info) - Fetch information about settings in a workspace
* [admin_teams_settings_set_default_channels](#admin_teams_settings_set_default_channels) - Set the default channels of a workspace.
* [admin_teams_settings_set_description](#admin_teams_settings_set_description) - Set the description of a given workspace.
* [admin_teams_settings_set_discoverability](#admin_teams_settings_set_discoverability) - An API method that allows admins to set the discoverability of a given workspace
* [admin_teams_settings_set_icon](#admin_teams_settings_set_icon) - Sets the icon of a workspace.
* [admin_teams_settings_set_name](#admin_teams_settings_set_name) - Set the name of a given workspace.
* [admin_usergroups_add_channels](#admin_usergroups_add_channels) - Add one or more default channels to an IDP group.
* [admin_usergroups_add_teams](#admin_usergroups_add_teams) - Associate one or more default workspaces with an organization-wide IDP group.
* [admin_usergroups_list_channels](#admin_usergroups_list_channels) - List the channels linked to an org-level IDP group (user group).
* [admin_usergroups_remove_channels](#admin_usergroups_remove_channels) - Remove one or more default channels from an org-level IDP group (user group).
* [admin_users_assign](#admin_users_assign) - Add an Enterprise user to a workspace.
* [admin_users_invite](#admin_users_invite) - Invite a user to a workspace.
* [admin_users_list](#admin_users_list) - List users on a workspace
* [admin_users_remove](#admin_users_remove) - Remove a user from a workspace.
* [admin_users_session_invalidate](#admin_users_session_invalidate) - Invalidate a single session for a user by session_id
* [admin_users_session_reset](#admin_users_session_reset) - Wipes all valid sessions on all devices for a given user
* [admin_users_set_admin](#admin_users_set_admin) - Set an existing guest, regular user, or owner to be an admin user.
* [admin_users_set_expiration](#admin_users_set_expiration) - Set an expiration for a guest user
* [admin_users_set_owner](#admin_users_set_owner) - Set an existing guest, regular user, or admin user to be a workspace owner.
* [admin_users_set_regular](#admin_users_set_regular) - Set an existing guest user, admin user, or owner to be a regular user.

## admin_apps_approve

Approve an app for installation on a workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.approve>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsApproveRequest(
    request_body=operations.AdminAppsApproveApplicationJSON(
        app_id='unde',
        request_id='nulla',
        team_id='corrupti',
    ),
    token='illum',
)

res = s.admin.admin_apps_approve(req, operations.AdminAppsApproveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_apps_approved_list

List approved apps for an org or workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.approved.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsApprovedListRequest(
    cursor='vel',
    enterprise_id='error',
    limit=645894,
    team_id='suscipit',
    token='iure',
)

res = s.admin.admin_apps_approved_list(req, operations.AdminAppsApprovedListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_apps_requests_list

List app requests for a team/workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.requests.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsRequestsListRequest(
    cursor='magnam',
    limit=891773,
    team_id='ipsa',
    token='delectus',
)

res = s.admin.admin_apps_requests_list(req, operations.AdminAppsRequestsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_apps_restrict

Restrict an app for installation on a workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.restrict>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsRestrictRequest(
    request_body=operations.AdminAppsRestrictApplicationJSON(
        app_id='tempora',
        request_id='suscipit',
        team_id='molestiae',
    ),
    token='minus',
)

res = s.admin.admin_apps_restrict(req, operations.AdminAppsRestrictSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_apps_restricted_list

List restricted apps for an org or workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.restricted.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsRestrictedListRequest(
    cursor='placeat',
    enterprise_id='voluptatum',
    limit=479977,
    team_id='excepturi',
    token='nisi',
)

res = s.admin.admin_apps_restricted_list(req, operations.AdminAppsRestrictedListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

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
        channel_id='recusandae',
    ),
    token='temporibus',
)

res = s.admin.admin_conversations_archive(req, operations.AdminConversationsArchiveSecurity(
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
        channel_id='ab',
    ),
    token='quis',
)

res = s.admin.admin_conversations_convert_to_private(req, operations.AdminConversationsConvertToPrivateSecurity(
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
        description='veritatis',
        is_private=False,
        name='Christopher Hills',
        org_wide=False,
        team_id='quo',
    ),
    token='odit',
)

res = s.admin.admin_conversations_create(req, operations.AdminConversationsCreateSecurity(
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
        channel_id='at',
    ),
    token='at',
)

res = s.admin.admin_conversations_delete(req, operations.AdminConversationsDeleteSecurity(
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
        channel_id='maiores',
        leaving_team_ids='molestiae',
    ),
    token='quod',
)

res = s.admin.admin_conversations_disconnect_shared(req, operations.AdminConversationsDisconnectSharedSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_rename_schema is not None:
    # handle response
```

## admin_conversations_ekm_list_original_connected_channel_info

List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

API method documentation
<https://api.slack.com/methods/admin.conversations.ekm.listOriginalConnectedChannelInfo>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminConversationsEkmListOriginalConnectedChannelInfoRequest(
    channel_ids='quod',
    cursor='esse',
    limit=520478,
    team_ids='porro',
    token='dolorum',
)

res = s.admin.admin_conversations_ekm_list_original_connected_channel_info(req, operations.AdminConversationsEkmListOriginalConnectedChannelInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
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
    channel_id='dicta',
    token='nam',
)

res = s.admin.admin_conversations_get_conversation_prefs(req, operations.AdminConversationsGetConversationPrefsSecurity(
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
    channel_id='officia',
    cursor='occaecati',
    limit=143353,
    token='deleniti',
)

res = s.admin.admin_conversations_get_teams(req, operations.AdminConversationsGetTeamsSecurity(
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
        channel_id='hic',
        user_ids='optio',
    ),
    token='totam',
)

res = s.admin.admin_conversations_invite(req, operations.AdminConversationsInviteSecurity(
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
        channel_id='beatae',
        name='Tanya Gleason',
    ),
    token='cum',
)

res = s.admin.admin_conversations_rename(req, operations.AdminConversationsRenameSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_rename_schema is not None:
    # handle response
```

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
    channel_id='esse',
    group_id='ipsum',
    team_id='excepturi',
    token='aspernatur',
)

res = s.admin.admin_conversations_restrict_access_add_group(req, operations.AdminConversationsRestrictAccessAddGroupSecurity(
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
    channel_id='perferendis',
    team_id='ad',
    token='natus',
)

res = s.admin.admin_conversations_restrict_access_list_groups(req, operations.AdminConversationsRestrictAccessListGroupsSecurity(
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
    channel_id='sed',
    group_id='iste',
    team_id='dolor',
    token='natus',
)

res = s.admin.admin_conversations_restrict_access_remove_group(req, operations.AdminConversationsRestrictAccessRemoveGroupSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
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
    cursor='laboriosam',
    limit=943749,
    query='saepe',
    search_channel_types='fuga',
    sort='in',
    sort_dir='corporis',
    team_ids='iste',
    token='iure',
)

res = s.admin.admin_conversations_search(req, operations.AdminConversationsSearchSecurity(
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
        channel_id='saepe',
        prefs='quidem',
    ),
    token='architecto',
)

res = s.admin.admin_conversations_set_conversation_prefs(req, operations.AdminConversationsSetConversationPrefsSecurity(
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
        channel_id='ipsa',
        org_channel=False,
        target_team_ids='reiciendis',
        team_id='est',
    ),
    token='mollitia',
)

res = s.admin.admin_conversations_set_teams(req, operations.AdminConversationsSetTeamsSecurity(
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
        channel_id='laborum',
    ),
    token='dolores',
)

res = s.admin.admin_conversations_unarchive(req, operations.AdminConversationsUnarchiveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.admin_conversations_unarchive_schema is not None:
    # handle response
```

## admin_emoji_add

Add an emoji.

API method documentation
<https://api.slack.com/methods/admin.emoji.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiAddRequestBody(
    name='Stacy Champlin',
    token='omnis',
    url='nemo',
)

res = s.admin.admin_emoji_add(req, operations.AdminEmojiAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_add_alias

Add an emoji alias.

API method documentation
<https://api.slack.com/methods/admin.emoji.addAlias>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiAddAliasRequestBody(
    alias_for='minima',
    name='Brian Kessler',
    token='sapiente',
)

res = s.admin.admin_emoji_add_alias(req, operations.AdminEmojiAddAliasSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_list

List emoji for an Enterprise Grid organization.

API method documentation
<https://api.slack.com/methods/admin.emoji.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiListRequest(
    cursor='architecto',
    limit=652790,
    token='dolorem',
)

res = s.admin.admin_emoji_list(req, operations.AdminEmojiListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_remove

Remove an emoji across an Enterprise Grid organization

API method documentation
<https://api.slack.com/methods/admin.emoji.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiRemoveRequestBody(
    name='Carlos Ziemann',
    token='numquam',
)

res = s.admin.admin_emoji_remove(req, operations.AdminEmojiRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_rename

Rename an emoji.

API method documentation
<https://api.slack.com/methods/admin.emoji.rename>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiRenameRequestBody(
    name='Claudia Krajcik',
    new_name='quia',
    token='quis',
)

res = s.admin.admin_emoji_rename(req, operations.AdminEmojiRenameSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

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
        invite_request_id='vitae',
        team_id='laborum',
    ),
    token='animi',
)

res = s.admin.admin_invite_requests_approve(req, operations.AdminInviteRequestsApproveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

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
    cursor='enim',
    limit=138183,
    team_id='quo',
    token='sequi',
)

res = s.admin.admin_invite_requests_approved_list(req, operations.AdminInviteRequestsApprovedListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_invite_requests_denied_list

List all denied workspace invite requests.

API method documentation
<https://api.slack.com/methods/admin.inviteRequests.denied.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminInviteRequestsDeniedListRequest(
    cursor='tenetur',
    limit=368725,
    team_id='id',
    token='possimus',
)

res = s.admin.admin_invite_requests_denied_list(req, operations.AdminInviteRequestsDeniedListSecurity(
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
        invite_request_id='aut',
        team_id='quasi',
    ),
    token='error',
)

res = s.admin.admin_invite_requests_deny(req, operations.AdminInviteRequestsDenySecurity(
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
    cursor='temporibus',
    limit=673660,
    team_id='quasi',
    token='reiciendis',
)

res = s.admin.admin_invite_requests_list(req, operations.AdminInviteRequestsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_admins_list

List all of the admins on a given workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.admins.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsAdminsListRequest(
    cursor='voluptatibus',
    limit=878194,
    team_id='nihil',
    token='praesentium',
)

res = s.admin.admin_teams_admins_list(req, operations.AdminTeamsAdminsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_create

Create an Enterprise team.

API method documentation
<https://api.slack.com/methods/admin.teams.create>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsCreateRequest(
    request_body=operations.AdminTeamsCreateApplicationJSON(
        team_description='voluptatibus',
        team_discoverability='ipsa',
        team_domain='omnis',
        team_name='voluptate',
    ),
    token='cum',
)

res = s.admin.admin_teams_create(req, operations.AdminTeamsCreateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_list

List all teams on an Enterprise organization

API method documentation
<https://api.slack.com/methods/admin.teams.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsListRequest(
    cursor='perferendis',
    limit=39187,
    token='reprehenderit',
)

res = s.admin.admin_teams_list(req, operations.AdminTeamsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_owners_list

List all of the owners on a given workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.owners.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsOwnersListRequest(
    cursor='ut',
    limit=979587,
    team_id='dicta',
    token='corporis',
)

res = s.admin.admin_teams_owners_list(req, operations.AdminTeamsOwnersListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_settings_info

Fetch information about settings in a workspace

API method documentation
<https://api.slack.com/methods/admin.teams.settings.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsSettingsInfoRequest(
    team_id='dolore',
    token='iusto',
)

res = s.admin.admin_teams_settings_info(req, operations.AdminTeamsSettingsInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_settings_set_default_channels

Set the default channels of a workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.settings.setDefaultChannels>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsSettingsSetDefaultChannelsRequestBody(
    channel_ids='dicta',
    team_id='harum',
    token='enim',
)

res = s.admin.admin_teams_settings_set_default_channels(req, operations.AdminTeamsSettingsSetDefaultChannelsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_settings_set_description

Set the description of a given workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.settings.setDescription>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsSettingsSetDescriptionRequest(
    request_body=operations.AdminTeamsSettingsSetDescriptionApplicationJSON(
        description='accusamus',
        team_id='commodi',
    ),
    token='repudiandae',
)

res = s.admin.admin_teams_settings_set_description(req, operations.AdminTeamsSettingsSetDescriptionSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_settings_set_discoverability

An API method that allows admins to set the discoverability of a given workspace

API method documentation
<https://api.slack.com/methods/admin.teams.settings.setDiscoverability>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsSettingsSetDiscoverabilityRequest(
    request_body=operations.AdminTeamsSettingsSetDiscoverabilityApplicationJSON(
        discoverability='quae',
        team_id='ipsum',
    ),
    token='quidem',
)

res = s.admin.admin_teams_settings_set_discoverability(req, operations.AdminTeamsSettingsSetDiscoverabilitySecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_settings_set_icon

Sets the icon of a workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.settings.setIcon>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsSettingsSetIconRequestBody(
    image_url='molestias',
    team_id='excepturi',
    token='pariatur',
)

res = s.admin.admin_teams_settings_set_icon(req, operations.AdminTeamsSettingsSetIconSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_settings_set_name

Set the name of a given workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.settings.setName>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsSettingsSetNameRequest(
    request_body=operations.AdminTeamsSettingsSetNameApplicationJSON(
        name='Irma Ledner DVM',
        team_id='sint',
    ),
    token='veritatis',
)

res = s.admin.admin_teams_settings_set_name(req, operations.AdminTeamsSettingsSetNameSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_usergroups_add_channels

Add one or more default channels to an IDP group.

API method documentation
<https://api.slack.com/methods/admin.usergroups.addChannels>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsergroupsAddChannelsRequest(
    request_body=operations.AdminUsergroupsAddChannelsApplicationJSON(
        channel_ids='itaque',
        team_id='incidunt',
        usergroup_id='enim',
    ),
    token='consequatur',
)

res = s.admin.admin_usergroups_add_channels(req, operations.AdminUsergroupsAddChannelsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_usergroups_add_teams

Associate one or more default workspaces with an organization-wide IDP group.

API method documentation
<https://api.slack.com/methods/admin.usergroups.addTeams>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsergroupsAddTeamsRequest(
    request_body=operations.AdminUsergroupsAddTeamsApplicationJSON(
        auto_provision=False,
        team_ids='est',
        usergroup_id='quibusdam',
    ),
    token='explicabo',
)

res = s.admin.admin_usergroups_add_teams(req, operations.AdminUsergroupsAddTeamsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_usergroups_list_channels

List the channels linked to an org-level IDP group (user group).

API method documentation
<https://api.slack.com/methods/admin.usergroups.listChannels>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsergroupsListChannelsRequest(
    include_num_members=False,
    team_id='deserunt',
    token='distinctio',
    usergroup_id='quibusdam',
)

res = s.admin.admin_usergroups_list_channels(req, operations.AdminUsergroupsListChannelsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_usergroups_remove_channels

Remove one or more default channels from an org-level IDP group (user group).

API method documentation
<https://api.slack.com/methods/admin.usergroups.removeChannels>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminUsergroupsRemoveChannelsRequest(
    request_body=operations.AdminUsergroupsRemoveChannelsApplicationJSON(
        channel_ids='labore',
        usergroup_id='modi',
    ),
    token='qui',
)

res = s.admin.admin_usergroups_remove_channels(req, operations.AdminUsergroupsRemoveChannelsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

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
        channel_ids='aliquid',
        is_restricted=False,
        is_ultra_restricted=False,
        team_id='cupiditate',
        user_id='quos',
    ),
    token='perferendis',
)

res = s.admin.admin_users_assign(req, operations.AdminUsersAssignSecurity(
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
        channel_ids='magni',
        custom_message='assumenda',
        email='Abigale_Corkery27@yahoo.com',
        guest_expiration_ts='facilis',
        is_restricted=False,
        is_ultra_restricted=False,
        real_name='tempore',
        resend=False,
        team_id='labore',
    ),
    token='delectus',
)

res = s.admin.admin_users_invite(req, operations.AdminUsersInviteSecurity(
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
    cursor='eum',
    limit=248753,
    team_id='eligendi',
    token='sint',
)

res = s.admin.admin_users_list(req, operations.AdminUsersListSecurity(
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
        team_id='aliquid',
        user_id='provident',
    ),
    token='necessitatibus',
)

res = s.admin.admin_users_remove(req, operations.AdminUsersRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

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
        session_id=572252,
        team_id='officia',
    ),
    token='dolor',
)

res = s.admin.admin_users_session_invalidate(req, operations.AdminUsersSessionInvalidateSecurity(
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
        user_id='debitis',
        web_only=False,
    ),
    token='a',
)

res = s.admin.admin_users_session_reset(req, operations.AdminUsersSessionResetSecurity(
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
        team_id='dolorum',
        user_id='in',
    ),
    token='in',
)

res = s.admin.admin_users_set_admin(req, operations.AdminUsersSetAdminSecurity(
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
        expiration_ts=846409,
        team_id='maiores',
        user_id='rerum',
    ),
    token='dicta',
)

res = s.admin.admin_users_set_expiration(req, operations.AdminUsersSetExpirationSecurity(
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
        team_id='magnam',
        user_id='cumque',
    ),
    token='facere',
)

res = s.admin.admin_users_set_owner(req, operations.AdminUsersSetOwnerSecurity(
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
        team_id='ea',
        user_id='aliquid',
    ),
    token='laborum',
)

res = s.admin.admin_users_set_regular(req, operations.AdminUsersSetRegularSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
