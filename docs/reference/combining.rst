Combining
=========================

.. py:function:: chain(*aiterables: AsyncIterable[_T]) -> AsyncIterable[_T]
   :async:

   Chain multiple async iterables, behaves like ``itertools.chain`` but is asynchronous.


.. py:function:: interleave(*aiterables: AsyncIterable[_T]) -> AsyncIterable[_T]
   :async:

   Combine multiple async iterables. Unlike ``chain``, which doesn't iterate the second iterator until
   the first is exhausted, this one yields once any of the given iterable is available.

   Stops when all given iterators are exhausted.

   Usage example:

   .. code-block:: python

        async def first():
            yield 1
            await asyncio.sleep(0.02)
            yield 2

        async def second():
            await asyncio.sleep(0.01)
            yield 3
            await asyncio.sleep(0.02)
            yield 4

        assert [
            item
            async for item in async_itertools.interleave(first(), second())
        ] == [1, 3, 2, 4]
