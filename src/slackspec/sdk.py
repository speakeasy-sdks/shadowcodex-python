"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .admin import Admin
from .admin_apps import AdminApps
from .admin_apps_approved import AdminAppsApproved
from .admin_apps_requests import AdminAppsRequests
from .admin_apps_restricted import AdminAppsRestricted
from .admin_conversations import AdminConversations
from .admin_conversations_ekm import AdminConversationsEkm
from .admin_conversations_restrictaccess import AdminConversationsRestrictAccess
from .admin_emoji import AdminEmoji
from .admin_inviterequests import AdminInviteRequests
from .admin_inviterequests_approved import AdminInviteRequestsApproved
from .admin_inviterequests_denied import AdminInviteRequestsDenied
from .admin_teams import AdminTeams
from .admin_teams_admins import AdminTeamsAdmins
from .admin_teams_owners import AdminTeamsOwners
from .admin_teams_settings import AdminTeamsSettings
from .admin_usergroups import AdminUsergroups
from .admin_users import AdminUsers
from .admin_users_session import AdminUsersSession
from .api import API
from .apps import Apps
from .apps_event_authorizations import AppsEventAuthorizations
from .apps_permissions import AppsPermissions
from .apps_permissions_resources import AppsPermissionsResources
from .apps_permissions_scopes import AppsPermissionsScopes
from .auth import Auth
from .bots import Bots
from .calls import Calls
from .calls_participants import CallsParticipants
from .chat import Chat
from .chat_scheduledmessages import ChatScheduledMessages
from .conversations import Conversations
from .dialog import Dialog
from .dnd import Dnd
from .emoji import Emoji
from .files import Files
from .files_comments import FilesComments
from .files_remote import FilesRemote
from .migration import Migration
from .oauth import Oauth
from .oauth_v2 import OauthV2
from .pins import Pins
from .reactions import Reactions
from .reminders import Reminders
from .rtm import Rtm
from .search import Search
from .stars import Stars
from .team import Team
from .team_profile import TeamProfile
from .usergroups import Usergroups
from .usergroups_users import UsergroupsUsers
from .users import Users
from .users_profile import UsersProfile
from .views import Views
from .workflows import Workflows

SERVERS = [
    "https://slack.com/api",
]
"""Contains the list of servers available to the SDK"""

class SlackSpec:
    r"""One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.
    https://api.slack.com/web - Learn more about the Slack Web API
    """
    admin: Admin
    admin_apps: AdminApps
    admin_apps_approved: AdminAppsApproved
    admin_apps_requests: AdminAppsRequests
    admin_apps_restricted: AdminAppsRestricted
    admin_conversations: AdminConversations
    admin_conversations_ekm: AdminConversationsEkm
    admin_conversations_restrict_access: AdminConversationsRestrictAccess
    admin_emoji: AdminEmoji
    admin_invite_requests: AdminInviteRequests
    admin_invite_requests_approved: AdminInviteRequestsApproved
    admin_invite_requests_denied: AdminInviteRequestsDenied
    admin_teams: AdminTeams
    admin_teams_admins: AdminTeamsAdmins
    admin_teams_owners: AdminTeamsOwners
    admin_teams_settings: AdminTeamsSettings
    admin_usergroups: AdminUsergroups
    admin_users: AdminUsers
    admin_users_session: AdminUsersSession
    api: API
    apps: Apps
    apps_event_authorizations: AppsEventAuthorizations
    apps_permissions: AppsPermissions
    apps_permissions_resources: AppsPermissionsResources
    apps_permissions_scopes: AppsPermissionsScopes
    auth: Auth
    bots: Bots
    calls: Calls
    calls_participants: CallsParticipants
    chat: Chat
    chat_scheduled_messages: ChatScheduledMessages
    conversations: Conversations
    dialog: Dialog
    dnd: Dnd
    emoji: Emoji
    files: Files
    files_comments: FilesComments
    files_remote: FilesRemote
    migration: Migration
    oauth: Oauth
    oauth_v2: OauthV2
    pins: Pins
    reactions: Reactions
    reminders: Reminders
    rtm: Rtm
    search: Search
    stars: Stars
    team: Team
    team_profile: TeamProfile
    usergroups: Usergroups
    usergroups_users: UsergroupsUsers
    users: Users
    users_profile: UsersProfile
    views: Views
    workflows: Workflows

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.0.0"
    _gen_version: str = "2.26.1"

    def __init__(self,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = self._client
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.admin = Admin(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_apps = AdminApps(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_apps_approved = AdminAppsApproved(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_apps_requests = AdminAppsRequests(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_apps_restricted = AdminAppsRestricted(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_conversations = AdminConversations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_conversations_ekm = AdminConversationsEkm(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_conversations_restrict_access = AdminConversationsRestrictAccess(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_emoji = AdminEmoji(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_invite_requests = AdminInviteRequests(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_invite_requests_approved = AdminInviteRequestsApproved(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_invite_requests_denied = AdminInviteRequestsDenied(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_teams = AdminTeams(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_teams_admins = AdminTeamsAdmins(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_teams_owners = AdminTeamsOwners(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_teams_settings = AdminTeamsSettings(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_usergroups = AdminUsergroups(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_users = AdminUsers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.admin_users_session = AdminUsersSession(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.api = API(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.apps = Apps(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.apps_event_authorizations = AppsEventAuthorizations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.apps_permissions = AppsPermissions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.apps_permissions_resources = AppsPermissionsResources(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.apps_permissions_scopes = AppsPermissionsScopes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.auth = Auth(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.bots = Bots(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.calls = Calls(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.calls_participants = CallsParticipants(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.chat = Chat(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.chat_scheduled_messages = ChatScheduledMessages(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.conversations = Conversations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.dialog = Dialog(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.dnd = Dnd(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.emoji = Emoji(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.files = Files(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.files_comments = FilesComments(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.files_remote = FilesRemote(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.migration = Migration(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.oauth = Oauth(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.oauth_v2 = OauthV2(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.pins = Pins(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.reactions = Reactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.reminders = Reminders(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.rtm = Rtm(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.search = Search(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.stars = Stars(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.team = Team(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.team_profile = TeamProfile(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.usergroups = Usergroups(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.usergroups_users = UsergroupsUsers(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.users = Users(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.users_profile = UsersProfile(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.views = Views(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.workflows = Workflows(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    