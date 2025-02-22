"""
This 'mocks' a discord.Member so we can use it for testing
"""
from unittest.mock import AsyncMock, Mock

from tests.mocks.mock_role import MockedRole


class MockedMember:
    def __init__(self, name=None, member_id=None, is_bot=False, mock_type="member"):
        self.name = name or "Mocked Member"
        # 0 is falsey
        if mock_type.lower() == "bot":
            self.id = int(member_id) if member_id or member_id == 0 else 98987
        else:
            self.id = int(member_id) if member_id or member_id == 0 else 12345
        self.mention = f"<@{self.id}>"
        self.is_bot = is_bot
        self.type = mock_type.lower()

    def to_mock(self):
        """Returns an AsyncMock matching the spec for this class"""
        # we still have to set stuff manually but changing values is nicer
        mock = AsyncMock(name="Member Mock")
        if self.type == "bot":
            # Mocks a bot
            mock.user.name = self.name
            mock.user.id = self.id
            mock.user.mention = f"<@{self.id}>"
            mock.user.bot = True

            mock.user.roles = [
                MockedRole().to_mock(),
                MockedRole(name="test role 2", role_id=252525).to_mock(),
            ]

            mock.get_channel = self.get_channel
            mock.fetch_channel = self.fetch_channel

            return mock
        elif self.type == "member":
            mock.roles = [
                MockedRole().to_mock(),
                MockedRole(name="test role 2", role_id=252525).to_mock(),
            ]
            mock.top_role.position = 5

        mock.name = self.name
        mock.display_name = self.name
        mock.id = self.id
        mock.bot = self.is_bot
        mock.mention = f"<@{self.id}>"

        return mock

    @staticmethod
    def get_channel(channel_id):
        from tests.mocks import MockedChannel

        return MockedChannel(channel_id=channel_id).to_mock()

    @staticmethod
    async def fetch_channel(channel_id):
        from tests.mocks import MockedChannel

        return MockedChannel(channel_id=channel_id).to_mock()
