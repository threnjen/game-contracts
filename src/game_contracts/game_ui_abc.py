from abc import ABC, abstractmethod
import asyncio


class GameUI(ABC):

    def __init__(
        self, player_id: str, game_id: str, game_name: str, runner_client
    ) -> None:
        self.queue = asyncio.Queue()
        self.runner_client = runner_client
        self.player_id = player_id
        self.game_id = game_id
        self.game_name = game_name

    def _initialize_server(self) -> None:
        """
        Initializes the game state on the server.
        This method is called automatically during the init of the GameUI.
        """
        self.runner_client.initialize_server(
            params={
                "game_id": self.game_id,
                "player_id": self.player_id,
                "game_name": self.game_name,
            }
        )
        print(f"Game state initialized")

    async def start(self):
        """
        Starts the UI and begins the background polling loop.
        This method is called to kick off the UI and start listening for server messages.
        """
        asyncio.create_task(self._background_poll_loop())
        print("UI is running")

    def send_action_to_server(self, game_id: str, payload: dict) -> None:
        """
        This method is called by the UI to send actions to the server.
        Uses the runner client to post the payload to the server.
        """
        self.runner_client.post_to_server(game_id, payload)

    async def wait_for_server_response(self) -> dict:
        """
        This method is called by the UI to wait for a response from the server.
        It blocks until a message is received from the server.
        """
        return await self.queue.get()

    async def _background_poll_loop(self) -> None:
        """
        This method runs in the background to poll for server messages.
        It continuously checks for messages from the server and puts them in the queue.
        """
        while True:
            msg = await self.runner_client.poll_for_server_response()
            await self.queue.put(msg)

    @abstractmethod
    def _ui_game_cleanup(self) -> bool: ...

    """
    This method is called to clean up the UI game state.
    It should be implemented by subclasses to handle any necessary cleanup.
    Returns True if cleanup was successful, False otherwise.
    """

    @abstractmethod
    def handle_server_message(self, message) -> bool: ...

    """
    This method is called to handle messages received from the server.
    It should be implemented by subclasses to process the message.
    Returns True if the message was handled successfully, False otherwise.
    """
