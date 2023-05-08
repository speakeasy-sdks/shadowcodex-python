# admin_conversations_ekm

### Available Operations

* [admin_conversations_ekm_list_original_connected_channel_info](#admin_conversations_ekm_list_original_connected_channel_info) - List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

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
    channel_ids='consequuntur',
    cursor='praesentium',
    limit=615560,
    team_ids='magni',
    token='sunt',
)

res = s.admin_conversations_ekm.admin_conversations_ekm_list_original_connected_channel_info(req, operations.AdminConversationsEkmListOriginalConnectedChannelInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
