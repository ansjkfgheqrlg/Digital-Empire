from dataclasses import dataclass


@dataclass(frozen=True)
class Greeting:
    message: str


def hello(name: str) -> Greeting:
    return Greeting(message=f"Hello, {name}")
