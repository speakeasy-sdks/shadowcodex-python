# apps

### Available Operations

* [apps_event_authorizations_list](#apps_event_authorizations_list) - Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.
* [apps_permissions_info](#apps_permissions_info) - Returns list of permissions this app has on a team.
* [apps_permissions_request](#apps_permissions_request) - Allows an app to request additional scopes
* [apps_permissions_resources_list](#apps_permissions_resources_list) - Returns list of resource grants this app has on a team.
* [apps_permissions_scopes_list](#apps_permissions_scopes_list) - Returns list of scopes this app has on a team.
* [apps_uninstall](#apps_uninstall) - Uninstalls your app from a workspace.

## apps_event_authorizations_list

Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

API method documentation
<https://api.slack.com/methods/apps.event.authorizations.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsEventAuthorizationsListRequest(
    cursor='dolorem',
    event_context='sapiente',
    limit=518201,
    token='nihil',
)

res = s.apps.apps_event_authorizations_list(req, operations.AppsEventAuthorizationsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## apps_permissions_info

Returns list of permissions this app has on a team.

API method documentation
<https://api.slack.com/methods/apps.permissions.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsInfoRequest(
    token='sit',
)

res = s.apps.apps_permissions_info(req, operations.AppsPermissionsInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.apps_permissions_info_schema is not None:
    # handle response
```

## apps_permissions_request

Allows an app to request additional scopes

API method documentation
<https://api.slack.com/methods/apps.permissions.request>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsRequestRequest(
    scopes='expedita',
    token='neque',
    trigger_id='sed',
)

res = s.apps.apps_permissions_request(req, operations.AppsPermissionsRequestSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.apps_permissions_request_schema is not None:
    # handle response
```

## apps_permissions_resources_list

Returns list of resource grants this app has on a team.

API method documentation
<https://api.slack.com/methods/apps.permissions.resources.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsResourcesListRequest(
    cursor='vel',
    limit=730442,
    token='voluptas',
)

res = s.apps.apps_permissions_resources_list(req, operations.AppsPermissionsResourcesListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.apps_permissions_resources_list_success_schema is not None:
    # handle response
```

## apps_permissions_scopes_list

Returns list of scopes this app has on a team.

API method documentation
<https://api.slack.com/methods/apps.permissions.scopes.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsScopesListRequest(
    token='deserunt',
)

res = s.apps.apps_permissions_scopes_list(req, operations.AppsPermissionsScopesListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.api_permissions_scopes_list_success_schema is not None:
    # handle response
```

## apps_uninstall

Uninstalls your app from a workspace.

API method documentation
<https://api.slack.com/methods/apps.uninstall>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsUninstallRequest(
    client_id='quam',
    client_secret='ipsum',
    token='incidunt',
)

res = s.apps.apps_uninstall(req, operations.AppsUninstallSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.apps_uninstall_schema is not None:
    # handle response
```
