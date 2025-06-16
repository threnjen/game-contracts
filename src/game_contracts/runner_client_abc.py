from abc import ABC, abstractmethod


class RunnerClientABC(ABC):
    @abstractmethod
    def poll_for_input(self) -> None: ...

    @abstractmethod
    def poll_for_server_response(self) -> str: ...

    @abstractmethod
    def send_action_to_server(self, action) -> None: ...
