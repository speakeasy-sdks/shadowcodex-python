# migration

### Available Operations

* [migration_exchange](#migration_exchange) - For Enterprise Grid workspaces, map local user IDs to global user IDs

## migration_exchange

For Enterprise Grid workspaces, map local user IDs to global user IDs

API method documentation
<https://api.slack.com/methods/migration.exchange>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.MigrationExchangeRequest(
    team_id='voluptatem',
    to_old=False,
    token='culpa',
    users='expedita',
)

res = s.migration.migration_exchange(req, operations.MigrationExchangeSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.migration_exchange_success_schema is not None:
    # handle response
```
