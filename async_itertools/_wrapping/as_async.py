import asyncio
from typing import Iterable, TypeVar, AsyncIterable

_T = TypeVar("_T")


async def as_async(iterable: Iterable[_T], interval: float = 0) -> AsyncIterable[_T]:
    for item in iterable:
        await asyncio.sleep(interval)
        yield item
