Wrapping
=========================

.. py:function:: as_async(iterable: Iterable[_T], interval: float = 0) -> AsyncIterable[_T]
   :async:

   Warp an ``Iterable`` into an ``AsyncIterable``, with an optional interval(``asyncio.sleep``)
   between each element.

   When `interval` is 0, ``asyncio.sleep(0)`` is called to trigger coroutine schedule of the eventloop.
