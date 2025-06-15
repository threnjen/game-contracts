from abc import ABC, abstractmethod


class RunnerClientABC(ABC):
    @abstractmethod
    def connect_to_server(self, server_address: str) -> None: ...

    @abstractmethod
    def disconnect_from_server(self) -> None: ...

    @abstractmethod
    def send_request(self, request: dict) -> dict: ...

    @abstractmethod
    def receive_response(self) -> dict: ...

    @abstractmethod
    def get_client_status(self) -> str: ...
