from abc import ABC, abstractmethod
import asyncio


class GameUI(ABC):

    def __init__(self, player_id, game_id, game_name, runner_client) -> None:
        self.queue = asyncio.Queue()
        self.runner_client = runner_client
        self.player_id = player_id
        self.game_id = game_id
        self.game_name = game_name

    def initialize_server(self) -> None:
        self.runner_client.initialize_server(
            params={
                "game_id": self.game_id,
                "player_id": self.player_id,
                "game_name": self.game_name,
            }
        )
        print(f"Game state initialized")

    async def start(self):
        asyncio.create_task(self.background_poll_loop())
        print("UI is running")

    def send_action_to_server(self, payload) -> None:
        self.runner_client.post_to_server(payload)

    async def wait_for_server_response(self) -> dict:
        return await self.queue.get()

    async def background_poll_loop(self) -> None:
        while True:
            msg = await self.runner_client.poll_for_server_response()
            await self.queue.put(msg)

    @abstractmethod
    def ui_game_cleanup(self) -> bool: ...

    @abstractmethod
    def handle_server_message(self, message) -> bool: ...
