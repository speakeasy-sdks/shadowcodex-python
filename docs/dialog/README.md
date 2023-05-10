# dialog

### Available Operations

* [dialog_open](#dialog_open) - Open a dialog with a user

## dialog_open

Open a dialog with a user

API method documentation
<https://api.slack.com/methods/dialog.open>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.DialogOpenRequest(
    dialog='possimus',
    token='facilis',
    trigger_id='cum',
)

res = s.dialog.dialog_open(req, operations.DialogOpenSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.dialog_open_schema is not None:
    # handle response
```
