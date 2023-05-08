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