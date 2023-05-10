# admin_teams_settings

### Available Operations

* [admin_teams_settings_info](#admin_teams_settings_info) - Fetch information about settings in a workspace
* [admin_teams_settings_set_default_channels](#admin_teams_settings_set_default_channels) - Set the default channels of a workspace.
* [admin_teams_settings_set_description](#admin_teams_settings_set_description) - Set the description of a given workspace.
* [admin_teams_settings_set_discoverability](#admin_teams_settings_set_discoverability) - An API method that allows admins to set the discoverability of a given workspace
* [admin_teams_settings_set_icon](#admin_teams_settings_set_icon) - Sets the icon of a workspace.
* [admin_teams_settings_set_name](#admin_teams_settings_set_name) - Set the name of a given workspace.

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
    team_id='hic',
    token='excepturi',
)

res = s.admin_teams_settings.admin_teams_settings_info(req, operations.AdminTeamsSettingsInfoSecurity(
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
    channel_ids='cum',
    team_id='voluptate',
    token='dignissimos',
)

res = s.admin_teams_settings.admin_teams_settings_set_default_channels(req, operations.AdminTeamsSettingsSetDefaultChannelsSecurity(
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
        description='reiciendis',
        team_id='amet',
    ),
    token='dolorum',
)

res = s.admin_teams_settings.admin_teams_settings_set_description(req, operations.AdminTeamsSettingsSetDescriptionSecurity(
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
        discoverability='numquam',
        team_id='veritatis',
    ),
    token='ipsa',
)

res = s.admin_teams_settings.admin_teams_settings_set_discoverability(req, operations.AdminTeamsSettingsSetDiscoverabilitySecurity(
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
    image_url='ipsa',
    team_id='iure',
    token='odio',
)

res = s.admin_teams_settings.admin_teams_settings_set_icon(req, operations.AdminTeamsSettingsSetIconSecurity(
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
        name='Sophia Predovic',
        team_id='natus',
    ),
    token='eos',
)

res = s.admin_teams_settings.admin_teams_settings_set_name(req, operations.AdminTeamsSettingsSetNameSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
