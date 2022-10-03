import asyncio
from typing import TypeVar, AsyncIterable, AsyncIterator, Tuple, Union

_T = TypeVar("_T")


async def _next(itr: AsyncIterator[_T]) -> Tuple[AsyncIterator[_T], Union[_T, StopAsyncIteration]]:
    try:
        result = await itr.__anext__()
    except StopAsyncIteration as err:
        return itr, err
    return itr, result


async def interleave(*aiterables: AsyncIterable[_T]) -> AsyncIterable[_T]:
    iterators = [item.__aiter__() for item in aiterables]
    pending = {asyncio.create_task(_next(item)) for item in iterators}
    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            itr, result = task.result()
            if not isinstance(result, StopAsyncIteration):
                pending.add(asyncio.create_task(_next(itr)))
                yield result
