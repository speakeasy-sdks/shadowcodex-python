# admin_usergroups

### Available Operations

* [admin_usergroups_add_channels](#admin_usergroups_add_channels) - Add one or more default channels to an IDP group.
* [admin_usergroups_add_teams](#admin_usergroups_add_teams) - Associate one or more default workspaces with an organization-wide IDP group.
* [admin_usergroups_list_channels](#admin_usergroups_list_channels) - List the channels linked to an org-level IDP group (user group).
* [admin_usergroups_remove_channels](#admin_usergroups_remove_channels) - Remove one or more default channels from an org-level IDP group (user group).

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
        channel_ids='atque',
        team_id='sit',
        usergroup_id='fugiat',
    ),
    token='ab',
)

res = s.admin_usergroups.admin_usergroups_add_channels(req, operations.AdminUsergroupsAddChannelsSecurity(
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
        team_ids='soluta',
        usergroup_id='dolorum',
    ),
    token='iusto',
)

res = s.admin_usergroups.admin_usergroups_add_teams(req, operations.AdminUsergroupsAddTeamsSecurity(
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
    team_id='voluptate',
    token='dolorum',
    usergroup_id='deleniti',
)

res = s.admin_usergroups.admin_usergroups_list_channels(req, operations.AdminUsergroupsListChannelsSecurity(
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
        channel_ids='omnis',
        usergroup_id='necessitatibus',
    ),
    token='distinctio',
)

res = s.admin_usergroups.admin_usergroups_remove_channels(req, operations.AdminUsergroupsRemoveChannelsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
