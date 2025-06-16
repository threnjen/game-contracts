from abc import ABC, abstractmethod


class RunnerServerABC(ABC):
    @abstractmethod
    def poll_for_input(self) -> None: ...

    @abstractmethod
    def push_response(self) -> None: ...
