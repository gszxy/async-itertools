from typing import TypeVar, AsyncIterable

_T = TypeVar("_T")


async def chain(*aiterables: AsyncIterable[_T]) -> AsyncIterable[_T]:
    for ait in aiterables:
        async for item in ait:
            yield item
