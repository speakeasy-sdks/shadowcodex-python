# slack-spec

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/shadowcodex-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsApproveRequest(
    request_body=operations.AdminAppsApproveApplicationJSON(
        app_id='corrupti',
        request_id='provident',
        team_id='distinctio',
    ),
    token='quibusdam',
)

res = s.admin.admin_apps_approve(req, operations.AdminAppsApproveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [admin](docs/admin/README.md)

* [admin_apps_approve](docs/admin/README.md#admin_apps_approve) - Approve an app for installation on a workspace.
* [admin_apps_approved_list](docs/admin/README.md#admin_apps_approved_list) - List approved apps for an org or workspace.
* [admin_apps_requests_list](docs/admin/README.md#admin_apps_requests_list) - List app requests for a team/workspace.
* [admin_apps_restrict](docs/admin/README.md#admin_apps_restrict) - Restrict an app for installation on a workspace.
* [admin_apps_restricted_list](docs/admin/README.md#admin_apps_restricted_list) - List restricted apps for an org or workspace.
* [admin_conversations_archive](docs/admin/README.md#admin_conversations_archive) - Archive a public or private channel.
* [admin_conversations_convert_to_private](docs/admin/README.md#admin_conversations_convert_to_private) - Convert a public channel to a private channel.
* [admin_conversations_create](docs/admin/README.md#admin_conversations_create) - Create a public or private channel-based conversation.
* [admin_conversations_delete](docs/admin/README.md#admin_conversations_delete) - Delete a public or private channel.
* [admin_conversations_disconnect_shared](docs/admin/README.md#admin_conversations_disconnect_shared) - Disconnect a connected channel from one or more workspaces.
* [admin_conversations_ekm_list_original_connected_channel_info](docs/admin/README.md#admin_conversations_ekm_list_original_connected_channel_info) - List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.
* [admin_conversations_get_conversation_prefs](docs/admin/README.md#admin_conversations_get_conversation_prefs) - Get conversation preferences for a public or private channel.
* [admin_conversations_get_teams](docs/admin/README.md#admin_conversations_get_teams) - Get all the workspaces a given public or private channel is connected to within this Enterprise org.
* [admin_conversations_invite](docs/admin/README.md#admin_conversations_invite) - Invite a user to a public or private channel.
* [admin_conversations_rename](docs/admin/README.md#admin_conversations_rename) - Rename a public or private channel.
* [admin_conversations_restrict_access_add_group](docs/admin/README.md#admin_conversations_restrict_access_add_group) - Add an allowlist of IDP groups for accessing a channel
* [admin_conversations_restrict_access_list_groups](docs/admin/README.md#admin_conversations_restrict_access_list_groups) - List all IDP Groups linked to a channel
* [admin_conversations_restrict_access_remove_group](docs/admin/README.md#admin_conversations_restrict_access_remove_group) - Remove a linked IDP group linked from a private channel
* [admin_conversations_search](docs/admin/README.md#admin_conversations_search) - Search for public or private channels in an Enterprise organization.
* [admin_conversations_set_conversation_prefs](docs/admin/README.md#admin_conversations_set_conversation_prefs) - Set the posting permissions for a public or private channel.
* [admin_conversations_set_teams](docs/admin/README.md#admin_conversations_set_teams) - Set the workspaces in an Enterprise grid org that connect to a public or private channel.
* [admin_conversations_unarchive](docs/admin/README.md#admin_conversations_unarchive) - Unarchive a public or private channel.
* [admin_emoji_add](docs/admin/README.md#admin_emoji_add) - Add an emoji.
* [admin_emoji_add_alias](docs/admin/README.md#admin_emoji_add_alias) - Add an emoji alias.
* [admin_emoji_list](docs/admin/README.md#admin_emoji_list) - List emoji for an Enterprise Grid organization.
* [admin_emoji_remove](docs/admin/README.md#admin_emoji_remove) - Remove an emoji across an Enterprise Grid organization
* [admin_emoji_rename](docs/admin/README.md#admin_emoji_rename) - Rename an emoji.
* [admin_invite_requests_approve](docs/admin/README.md#admin_invite_requests_approve) - Approve a workspace invite request.
* [admin_invite_requests_approved_list](docs/admin/README.md#admin_invite_requests_approved_list) - List all approved workspace invite requests.
* [admin_invite_requests_denied_list](docs/admin/README.md#admin_invite_requests_denied_list) - List all denied workspace invite requests.
* [admin_invite_requests_deny](docs/admin/README.md#admin_invite_requests_deny) - Deny a workspace invite request.
* [admin_invite_requests_list](docs/admin/README.md#admin_invite_requests_list) - List all pending workspace invite requests.
* [admin_teams_admins_list](docs/admin/README.md#admin_teams_admins_list) - List all of the admins on a given workspace.
* [admin_teams_create](docs/admin/README.md#admin_teams_create) - Create an Enterprise team.
* [admin_teams_list](docs/admin/README.md#admin_teams_list) - List all teams on an Enterprise organization
* [admin_teams_owners_list](docs/admin/README.md#admin_teams_owners_list) - List all of the owners on a given workspace.
* [admin_teams_settings_info](docs/admin/README.md#admin_teams_settings_info) - Fetch information about settings in a workspace
* [admin_teams_settings_set_default_channels](docs/admin/README.md#admin_teams_settings_set_default_channels) - Set the default channels of a workspace.
* [admin_teams_settings_set_description](docs/admin/README.md#admin_teams_settings_set_description) - Set the description of a given workspace.
* [admin_teams_settings_set_discoverability](docs/admin/README.md#admin_teams_settings_set_discoverability) - An API method that allows admins to set the discoverability of a given workspace
* [admin_teams_settings_set_icon](docs/admin/README.md#admin_teams_settings_set_icon) - Sets the icon of a workspace.
* [admin_teams_settings_set_name](docs/admin/README.md#admin_teams_settings_set_name) - Set the name of a given workspace.
* [admin_usergroups_add_channels](docs/admin/README.md#admin_usergroups_add_channels) - Add one or more default channels to an IDP group.
* [admin_usergroups_add_teams](docs/admin/README.md#admin_usergroups_add_teams) - Associate one or more default workspaces with an organization-wide IDP group.
* [admin_usergroups_list_channels](docs/admin/README.md#admin_usergroups_list_channels) - List the channels linked to an org-level IDP group (user group).
* [admin_usergroups_remove_channels](docs/admin/README.md#admin_usergroups_remove_channels) - Remove one or more default channels from an org-level IDP group (user group).
* [admin_users_assign](docs/admin/README.md#admin_users_assign) - Add an Enterprise user to a workspace.
* [admin_users_invite](docs/admin/README.md#admin_users_invite) - Invite a user to a workspace.
* [admin_users_list](docs/admin/README.md#admin_users_list) - List users on a workspace
* [admin_users_remove](docs/admin/README.md#admin_users_remove) - Remove a user from a workspace.
* [admin_users_session_invalidate](docs/admin/README.md#admin_users_session_invalidate) - Invalidate a single session for a user by session_id
* [admin_users_session_reset](docs/admin/README.md#admin_users_session_reset) - Wipes all valid sessions on all devices for a given user
* [admin_users_set_admin](docs/admin/README.md#admin_users_set_admin) - Set an existing guest, regular user, or owner to be an admin user.
* [admin_users_set_expiration](docs/admin/README.md#admin_users_set_expiration) - Set an expiration for a guest user
* [admin_users_set_owner](docs/admin/README.md#admin_users_set_owner) - Set an existing guest, regular user, or admin user to be a workspace owner.
* [admin_users_set_regular](docs/admin/README.md#admin_users_set_regular) - Set an existing guest user, admin user, or owner to be a regular user.

### [admin_apps](docs/adminapps/README.md)

* [admin_apps_approve](docs/adminapps/README.md#admin_apps_approve) - Approve an app for installation on a workspace.
* [admin_apps_restrict](docs/adminapps/README.md#admin_apps_restrict) - Restrict an app for installation on a workspace.

### [admin_apps_approved](docs/adminappsapproved/README.md)

* [admin_apps_approved_list](docs/adminappsapproved/README.md#admin_apps_approved_list) - List approved apps for an org or workspace.

### [admin_apps_requests](docs/adminappsrequests/README.md)

* [admin_apps_requests_list](docs/adminappsrequests/README.md#admin_apps_requests_list) - List app requests for a team/workspace.

### [admin_apps_restricted](docs/adminappsrestricted/README.md)

* [admin_apps_restricted_list](docs/adminappsrestricted/README.md#admin_apps_restricted_list) - List restricted apps for an org or workspace.

### [admin_conversations](docs/adminconversations/README.md)

* [admin_conversations_archive](docs/adminconversations/README.md#admin_conversations_archive) - Archive a public or private channel.
* [admin_conversations_convert_to_private](docs/adminconversations/README.md#admin_conversations_convert_to_private) - Convert a public channel to a private channel.
* [admin_conversations_create](docs/adminconversations/README.md#admin_conversations_create) - Create a public or private channel-based conversation.
* [admin_conversations_delete](docs/adminconversations/README.md#admin_conversations_delete) - Delete a public or private channel.
* [admin_conversations_disconnect_shared](docs/adminconversations/README.md#admin_conversations_disconnect_shared) - Disconnect a connected channel from one or more workspaces.
* [admin_conversations_get_conversation_prefs](docs/adminconversations/README.md#admin_conversations_get_conversation_prefs) - Get conversation preferences for a public or private channel.
* [admin_conversations_get_teams](docs/adminconversations/README.md#admin_conversations_get_teams) - Get all the workspaces a given public or private channel is connected to within this Enterprise org.
* [admin_conversations_invite](docs/adminconversations/README.md#admin_conversations_invite) - Invite a user to a public or private channel.
* [admin_conversations_rename](docs/adminconversations/README.md#admin_conversations_rename) - Rename a public or private channel.
* [admin_conversations_search](docs/adminconversations/README.md#admin_conversations_search) - Search for public or private channels in an Enterprise organization.
* [admin_conversations_set_conversation_prefs](docs/adminconversations/README.md#admin_conversations_set_conversation_prefs) - Set the posting permissions for a public or private channel.
* [admin_conversations_set_teams](docs/adminconversations/README.md#admin_conversations_set_teams) - Set the workspaces in an Enterprise grid org that connect to a public or private channel.
* [admin_conversations_unarchive](docs/adminconversations/README.md#admin_conversations_unarchive) - Unarchive a public or private channel.

### [admin_conversations_ekm](docs/adminconversationsekm/README.md)

* [admin_conversations_ekm_list_original_connected_channel_info](docs/adminconversationsekm/README.md#admin_conversations_ekm_list_original_connected_channel_info) - List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

### [admin_conversations_restrict_access](docs/adminconversationsrestrictaccess/README.md)

* [admin_conversations_restrict_access_add_group](docs/adminconversationsrestrictaccess/README.md#admin_conversations_restrict_access_add_group) - Add an allowlist of IDP groups for accessing a channel
* [admin_conversations_restrict_access_list_groups](docs/adminconversationsrestrictaccess/README.md#admin_conversations_restrict_access_list_groups) - List all IDP Groups linked to a channel
* [admin_conversations_restrict_access_remove_group](docs/adminconversationsrestrictaccess/README.md#admin_conversations_restrict_access_remove_group) - Remove a linked IDP group linked from a private channel

### [admin_emoji](docs/adminemoji/README.md)

* [admin_emoji_add](docs/adminemoji/README.md#admin_emoji_add) - Add an emoji.
* [admin_emoji_add_alias](docs/adminemoji/README.md#admin_emoji_add_alias) - Add an emoji alias.
* [admin_emoji_list](docs/adminemoji/README.md#admin_emoji_list) - List emoji for an Enterprise Grid organization.
* [admin_emoji_remove](docs/adminemoji/README.md#admin_emoji_remove) - Remove an emoji across an Enterprise Grid organization
* [admin_emoji_rename](docs/adminemoji/README.md#admin_emoji_rename) - Rename an emoji.

### [admin_invite_requests](docs/admininviterequests/README.md)

* [admin_invite_requests_approve](docs/admininviterequests/README.md#admin_invite_requests_approve) - Approve a workspace invite request.
* [admin_invite_requests_deny](docs/admininviterequests/README.md#admin_invite_requests_deny) - Deny a workspace invite request.
* [admin_invite_requests_list](docs/admininviterequests/README.md#admin_invite_requests_list) - List all pending workspace invite requests.

### [admin_invite_requests_approved](docs/admininviterequestsapproved/README.md)

* [admin_invite_requests_approved_list](docs/admininviterequestsapproved/README.md#admin_invite_requests_approved_list) - List all approved workspace invite requests.

### [admin_invite_requests_denied](docs/admininviterequestsdenied/README.md)

* [admin_invite_requests_denied_list](docs/admininviterequestsdenied/README.md#admin_invite_requests_denied_list) - List all denied workspace invite requests.

### [admin_teams](docs/adminteams/README.md)

* [admin_teams_create](docs/adminteams/README.md#admin_teams_create) - Create an Enterprise team.
* [admin_teams_list](docs/adminteams/README.md#admin_teams_list) - List all teams on an Enterprise organization

### [admin_teams_admins](docs/adminteamsadmins/README.md)

* [admin_teams_admins_list](docs/adminteamsadmins/README.md#admin_teams_admins_list) - List all of the admins on a given workspace.

### [admin_teams_owners](docs/adminteamsowners/README.md)

* [admin_teams_owners_list](docs/adminteamsowners/README.md#admin_teams_owners_list) - List all of the owners on a given workspace.

### [admin_teams_settings](docs/adminteamssettings/README.md)

* [admin_teams_settings_info](docs/adminteamssettings/README.md#admin_teams_settings_info) - Fetch information about settings in a workspace
* [admin_teams_settings_set_default_channels](docs/adminteamssettings/README.md#admin_teams_settings_set_default_channels) - Set the default channels of a workspace.
* [admin_teams_settings_set_description](docs/adminteamssettings/README.md#admin_teams_settings_set_description) - Set the description of a given workspace.
* [admin_teams_settings_set_discoverability](docs/adminteamssettings/README.md#admin_teams_settings_set_discoverability) - An API method that allows admins to set the discoverability of a given workspace
* [admin_teams_settings_set_icon](docs/adminteamssettings/README.md#admin_teams_settings_set_icon) - Sets the icon of a workspace.
* [admin_teams_settings_set_name](docs/adminteamssettings/README.md#admin_teams_settings_set_name) - Set the name of a given workspace.

### [admin_usergroups](docs/adminusergroups/README.md)

* [admin_usergroups_add_channels](docs/adminusergroups/README.md#admin_usergroups_add_channels) - Add one or more default channels to an IDP group.
* [admin_usergroups_add_teams](docs/adminusergroups/README.md#admin_usergroups_add_teams) - Associate one or more default workspaces with an organization-wide IDP group.
* [admin_usergroups_list_channels](docs/adminusergroups/README.md#admin_usergroups_list_channels) - List the channels linked to an org-level IDP group (user group).
* [admin_usergroups_remove_channels](docs/adminusergroups/README.md#admin_usergroups_remove_channels) - Remove one or more default channels from an org-level IDP group (user group).

### [admin_users](docs/adminusers/README.md)

* [admin_users_assign](docs/adminusers/README.md#admin_users_assign) - Add an Enterprise user to a workspace.
* [admin_users_invite](docs/adminusers/README.md#admin_users_invite) - Invite a user to a workspace.
* [admin_users_list](docs/adminusers/README.md#admin_users_list) - List users on a workspace
* [admin_users_remove](docs/adminusers/README.md#admin_users_remove) - Remove a user from a workspace.
* [admin_users_set_admin](docs/adminusers/README.md#admin_users_set_admin) - Set an existing guest, regular user, or owner to be an admin user.
* [admin_users_set_expiration](docs/adminusers/README.md#admin_users_set_expiration) - Set an expiration for a guest user
* [admin_users_set_owner](docs/adminusers/README.md#admin_users_set_owner) - Set an existing guest, regular user, or admin user to be a workspace owner.
* [admin_users_set_regular](docs/adminusers/README.md#admin_users_set_regular) - Set an existing guest user, admin user, or owner to be a regular user.

### [admin_users_session](docs/adminuserssession/README.md)

* [admin_users_session_invalidate](docs/adminuserssession/README.md#admin_users_session_invalidate) - Invalidate a single session for a user by session_id
* [admin_users_session_reset](docs/adminuserssession/README.md#admin_users_session_reset) - Wipes all valid sessions on all devices for a given user

### [api](docs/api/README.md)

* [api_test](docs/api/README.md#api_test) - Checks API calling code.

### [apps](docs/apps/README.md)

* [apps_event_authorizations_list](docs/apps/README.md#apps_event_authorizations_list) - Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.
* [apps_permissions_info](docs/apps/README.md#apps_permissions_info) - Returns list of permissions this app has on a team.
* [apps_permissions_request](docs/apps/README.md#apps_permissions_request) - Allows an app to request additional scopes
* [apps_permissions_resources_list](docs/apps/README.md#apps_permissions_resources_list) - Returns list of resource grants this app has on a team.
* [apps_permissions_scopes_list](docs/apps/README.md#apps_permissions_scopes_list) - Returns list of scopes this app has on a team.
* [apps_uninstall](docs/apps/README.md#apps_uninstall) - Uninstalls your app from a workspace.

### [apps_event_authorizations](docs/appseventauthorizations/README.md)

* [apps_event_authorizations_list](docs/appseventauthorizations/README.md#apps_event_authorizations_list) - Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

### [apps_permissions](docs/appspermissions/README.md)

* [apps_permissions_info](docs/appspermissions/README.md#apps_permissions_info) - Returns list of permissions this app has on a team.
* [apps_permissions_request](docs/appspermissions/README.md#apps_permissions_request) - Allows an app to request additional scopes

### [apps_permissions_resources](docs/appspermissionsresources/README.md)

* [apps_permissions_resources_list](docs/appspermissionsresources/README.md#apps_permissions_resources_list) - Returns list of resource grants this app has on a team.

### [apps_permissions_scopes](docs/appspermissionsscopes/README.md)

* [apps_permissions_scopes_list](docs/appspermissionsscopes/README.md#apps_permissions_scopes_list) - Returns list of scopes this app has on a team.

### [auth](docs/auth/README.md)

* [auth_revoke](docs/auth/README.md#auth_revoke) - Revokes a token.
* [auth_test](docs/auth/README.md#auth_test) - Checks authentication & identity.

### [bots](docs/bots/README.md)

* [bots_info](docs/bots/README.md#bots_info) - Gets information about a bot user.

### [calls](docs/calls/README.md)

* [calls_add](docs/calls/README.md#calls_add) - Registers a new Call.
* [calls_end](docs/calls/README.md#calls_end) - Ends a Call.
* [calls_info](docs/calls/README.md#calls_info) - Returns information about a Call.
* [calls_participants_add](docs/calls/README.md#calls_participants_add) - Registers new participants added to a Call.
* [calls_participants_remove](docs/calls/README.md#calls_participants_remove) - Registers participants removed from a Call.
* [calls_update](docs/calls/README.md#calls_update) - Updates information about a Call.

### [calls_participants](docs/callsparticipants/README.md)

* [calls_participants_add](docs/callsparticipants/README.md#calls_participants_add) - Registers new participants added to a Call.
* [calls_participants_remove](docs/callsparticipants/README.md#calls_participants_remove) - Registers participants removed from a Call.

### [chat](docs/chat/README.md)

* [chat_delete](docs/chat/README.md#chat_delete) - Deletes a message.
* [chat_delete_scheduled_message](docs/chat/README.md#chat_delete_scheduled_message) - Deletes a pending scheduled message from the queue.
* [chat_get_permalink](docs/chat/README.md#chat_get_permalink) - Retrieve a permalink URL for a specific extant message
* [chat_me_message](docs/chat/README.md#chat_me_message) - Share a me message into a channel.
* [chat_post_ephemeral](docs/chat/README.md#chat_post_ephemeral) - Sends an ephemeral message to a user in a channel.
* [chat_post_message](docs/chat/README.md#chat_post_message) - Sends a message to a channel.
* [chat_schedule_message](docs/chat/README.md#chat_schedule_message) - Schedules a message to be sent to a channel.
* [chat_scheduled_messages_list](docs/chat/README.md#chat_scheduled_messages_list) - Returns a list of scheduled messages.
* [chat_unfurl](docs/chat/README.md#chat_unfurl) - Provide custom unfurl behavior for user-posted URLs
* [chat_update](docs/chat/README.md#chat_update) - Updates a message.

### [chat_scheduled_messages](docs/chatscheduledmessages/README.md)

* [chat_scheduled_messages_list](docs/chatscheduledmessages/README.md#chat_scheduled_messages_list) - Returns a list of scheduled messages.

### [conversations](docs/conversations/README.md)

* [conversations_archive](docs/conversations/README.md#conversations_archive) - Archives a conversation.
* [conversations_close](docs/conversations/README.md#conversations_close) - Closes a direct message or multi-person direct message.
* [conversations_create](docs/conversations/README.md#conversations_create) - Initiates a public or private channel-based conversation
* [conversations_history](docs/conversations/README.md#conversations_history) - Fetches a conversation's history of messages and events.
* [conversations_info](docs/conversations/README.md#conversations_info) - Retrieve information about a conversation.
* [conversations_invite](docs/conversations/README.md#conversations_invite) - Invites users to a channel.
* [conversations_join](docs/conversations/README.md#conversations_join) - Joins an existing conversation.
* [conversations_kick](docs/conversations/README.md#conversations_kick) - Removes a user from a conversation.
* [conversations_leave](docs/conversations/README.md#conversations_leave) - Leaves a conversation.
* [conversations_list](docs/conversations/README.md#conversations_list) - Lists all channels in a Slack team.
* [conversations_mark](docs/conversations/README.md#conversations_mark) - Sets the read cursor in a channel.
* [conversations_members](docs/conversations/README.md#conversations_members) - Retrieve members of a conversation.
* [conversations_open](docs/conversations/README.md#conversations_open) - Opens or resumes a direct message or multi-person direct message.
* [conversations_rename](docs/conversations/README.md#conversations_rename) - Renames a conversation.
* [conversations_replies](docs/conversations/README.md#conversations_replies) - Retrieve a thread of messages posted to a conversation
* [conversations_set_purpose](docs/conversations/README.md#conversations_set_purpose) - Sets the purpose for a conversation.
* [conversations_set_topic](docs/conversations/README.md#conversations_set_topic) - Sets the topic for a conversation.
* [conversations_unarchive](docs/conversations/README.md#conversations_unarchive) - Reverses conversation archival.

### [dialog](docs/dialog/README.md)

* [dialog_open](docs/dialog/README.md#dialog_open) - Open a dialog with a user

### [dnd](docs/dnd/README.md)

* [dnd_end_dnd](docs/dnd/README.md#dnd_end_dnd) - Ends the current user's Do Not Disturb session immediately.
* [dnd_end_snooze](docs/dnd/README.md#dnd_end_snooze) - Ends the current user's snooze mode immediately.
* [dnd_info](docs/dnd/README.md#dnd_info) - Retrieves a user's current Do Not Disturb status.
* [dnd_set_snooze](docs/dnd/README.md#dnd_set_snooze) - Turns on Do Not Disturb mode for the current user, or changes its duration.
* [dnd_team_info](docs/dnd/README.md#dnd_team_info) - Retrieves the Do Not Disturb status for up to 50 users on a team.

### [emoji](docs/emoji/README.md)

* [emoji_list](docs/emoji/README.md#emoji_list) - Lists custom emoji for a team.

### [files](docs/files/README.md)

* [files_comments_delete](docs/files/README.md#files_comments_delete) - Deletes an existing comment on a file.
* [files_delete](docs/files/README.md#files_delete) - Deletes a file.
* [files_info](docs/files/README.md#files_info) - Gets information about a file.
* [files_list](docs/files/README.md#files_list) - List for a team, in a channel, or from a user with applied filters.
* [files_remote_add](docs/files/README.md#files_remote_add) - Adds a file from a remote service
* [files_remote_info](docs/files/README.md#files_remote_info) - Retrieve information about a remote file added to Slack
* [files_remote_list](docs/files/README.md#files_remote_list) - Retrieve information about a remote file added to Slack
* [files_remote_remove](docs/files/README.md#files_remote_remove) - Remove a remote file.
* [files_remote_share](docs/files/README.md#files_remote_share) - Share a remote file into a channel.
* [files_remote_update](docs/files/README.md#files_remote_update) - Updates an existing remote file.
* [files_revoke_public_url](docs/files/README.md#files_revoke_public_url) - Revokes public/external sharing access for a file
* [files_shared_public_url](docs/files/README.md#files_shared_public_url) - Enables a file for public/external sharing.
* [files_upload](docs/files/README.md#files_upload) - Uploads or creates a file.

### [files_comments](docs/filescomments/README.md)

* [files_comments_delete](docs/filescomments/README.md#files_comments_delete) - Deletes an existing comment on a file.

### [files_remote](docs/filesremote/README.md)

* [files_remote_add](docs/filesremote/README.md#files_remote_add) - Adds a file from a remote service
* [files_remote_info](docs/filesremote/README.md#files_remote_info) - Retrieve information about a remote file added to Slack
* [files_remote_list](docs/filesremote/README.md#files_remote_list) - Retrieve information about a remote file added to Slack
* [files_remote_remove](docs/filesremote/README.md#files_remote_remove) - Remove a remote file.
* [files_remote_share](docs/filesremote/README.md#files_remote_share) - Share a remote file into a channel.
* [files_remote_update](docs/filesremote/README.md#files_remote_update) - Updates an existing remote file.

### [migration](docs/migration/README.md)

* [migration_exchange](docs/migration/README.md#migration_exchange) - For Enterprise Grid workspaces, map local user IDs to global user IDs

### [oauth](docs/oauth/README.md)

* [oauth_access](docs/oauth/README.md#oauth_access) - Exchanges a temporary OAuth verifier code for an access token.
* [oauth_token](docs/oauth/README.md#oauth_token) - Exchanges a temporary OAuth verifier code for a workspace token.
* [oauth_v2_access](docs/oauth/README.md#oauth_v2_access) - Exchanges a temporary OAuth verifier code for an access token.

### [oauth_v2](docs/oauthv2/README.md)

* [oauth_v2_access](docs/oauthv2/README.md#oauth_v2_access) - Exchanges a temporary OAuth verifier code for an access token.

### [pins](docs/pins/README.md)

* [pins_add](docs/pins/README.md#pins_add) - Pins an item to a channel.
* [pins_list](docs/pins/README.md#pins_list) - Lists items pinned to a channel.
* [pins_remove](docs/pins/README.md#pins_remove) - Un-pins an item from a channel.

### [reactions](docs/reactions/README.md)

* [reactions_add](docs/reactions/README.md#reactions_add) - Adds a reaction to an item.
* [reactions_get](docs/reactions/README.md#reactions_get) - Gets reactions for an item.
* [reactions_list](docs/reactions/README.md#reactions_list) - Lists reactions made by a user.
* [reactions_remove](docs/reactions/README.md#reactions_remove) - Removes a reaction from an item.

### [reminders](docs/reminders/README.md)

* [reminders_add](docs/reminders/README.md#reminders_add) - Creates a reminder.
* [reminders_complete](docs/reminders/README.md#reminders_complete) - Marks a reminder as complete.
* [reminders_delete](docs/reminders/README.md#reminders_delete) - Deletes a reminder.
* [reminders_info](docs/reminders/README.md#reminders_info) - Gets information about a reminder.
* [reminders_list](docs/reminders/README.md#reminders_list) - Lists all reminders created by or for a given user.

### [rtm](docs/rtm/README.md)

* [rtm_connect](docs/rtm/README.md#rtm_connect) - Starts a Real Time Messaging session.

### [search](docs/search/README.md)

* [search_messages](docs/search/README.md#search_messages) - Searches for messages matching a query.

### [stars](docs/stars/README.md)

* [stars_add](docs/stars/README.md#stars_add) - Adds a star to an item.
* [stars_list](docs/stars/README.md#stars_list) - Lists stars for a user.
* [stars_remove](docs/stars/README.md#stars_remove) - Removes a star from an item.

### [team](docs/team/README.md)

* [team_access_logs](docs/team/README.md#team_access_logs) - Gets the access logs for the current team.
* [team_billable_info](docs/team/README.md#team_billable_info) - Gets billable users information for the current team.
* [team_info](docs/team/README.md#team_info) - Gets information about the current team.
* [team_integration_logs](docs/team/README.md#team_integration_logs) - Gets the integration logs for the current team.
* [team_profile_get](docs/team/README.md#team_profile_get) - Retrieve a team's profile.

### [team_profile](docs/teamprofile/README.md)

* [team_profile_get](docs/teamprofile/README.md#team_profile_get) - Retrieve a team's profile.

### [usergroups](docs/usergroups/README.md)

* [usergroups_create](docs/usergroups/README.md#usergroups_create) - Create a User Group
* [usergroups_disable](docs/usergroups/README.md#usergroups_disable) - Disable an existing User Group
* [usergroups_enable](docs/usergroups/README.md#usergroups_enable) - Enable a User Group
* [usergroups_list](docs/usergroups/README.md#usergroups_list) - List all User Groups for a team
* [usergroups_update](docs/usergroups/README.md#usergroups_update) - Update an existing User Group
* [usergroups_users_list](docs/usergroups/README.md#usergroups_users_list) - List all users in a User Group
* [usergroups_users_update](docs/usergroups/README.md#usergroups_users_update) - Update the list of users for a User Group

### [usergroups_users](docs/usergroupsusers/README.md)

* [usergroups_users_list](docs/usergroupsusers/README.md#usergroups_users_list) - List all users in a User Group
* [usergroups_users_update](docs/usergroupsusers/README.md#usergroups_users_update) - Update the list of users for a User Group

### [users](docs/users/README.md)

* [users_conversations](docs/users/README.md#users_conversations) - List conversations the calling user may access.
* [users_delete_photo](docs/users/README.md#users_delete_photo) - Delete the user profile photo
* [users_get_presence](docs/users/README.md#users_get_presence) - Gets user presence information.
* [users_identity](docs/users/README.md#users_identity) - Get a user's identity.
* [users_info](docs/users/README.md#users_info) - Gets information about a user.
* [users_list](docs/users/README.md#users_list) - Lists all users in a Slack team.
* [users_lookup_by_email](docs/users/README.md#users_lookup_by_email) - Find a user with an email address.
* [users_profile_get](docs/users/README.md#users_profile_get) - Retrieves a user's profile information.
* [users_profile_set](docs/users/README.md#users_profile_set) - Set the profile information for a user.
* [users_set_active](docs/users/README.md#users_set_active) - Marked a user as active. Deprecated and non-functional.
* [users_set_photo](docs/users/README.md#users_set_photo) - Set the user profile photo
* [users_set_presence](docs/users/README.md#users_set_presence) - Manually sets user presence.

### [users_profile](docs/usersprofile/README.md)

* [users_profile_get](docs/usersprofile/README.md#users_profile_get) - Retrieves a user's profile information.
* [users_profile_set](docs/usersprofile/README.md#users_profile_set) - Set the profile information for a user.

### [views](docs/views/README.md)

* [views_open](docs/views/README.md#views_open) - Open a view for a user.
* [views_publish](docs/views/README.md#views_publish) - Publish a static view for a User.
* [views_push](docs/views/README.md#views_push) - Push a view onto the stack of a root view.
* [views_update](docs/views/README.md#views_update) - Update an existing view.

### [workflows](docs/workflows/README.md)

* [workflows_step_completed](docs/workflows/README.md#workflows_step_completed) - Indicate that an app's step in a workflow completed execution.
* [workflows_step_failed](docs/workflows/README.md#workflows_step_failed) - Indicate that an app's step in a workflow failed to execute.
* [workflows_update_step](docs/workflows/README.md#workflows_update_step) - Update the configuration for a workflow extension step.
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
