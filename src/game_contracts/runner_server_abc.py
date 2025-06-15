from abc import ABC, abstractmethod


class RunnerServerABC(ABC):
    @abstractmethod
    def start_server(self) -> None: ...

    @abstractmethod
    def stop_server(self) -> None: ...

    @abstractmethod
    def restart_server(self) -> None: ...

    @abstractmethod
    def get_server_status(self) -> str: ...

    @abstractmethod
    def handle_client_request(self, request: dict) -> dict: ...
