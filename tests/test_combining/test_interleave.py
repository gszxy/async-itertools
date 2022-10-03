import asyncio
import unittest

import async_itertools


class TestInterleave(unittest.IsolatedAsyncioTestCase):

    async def test_combine_async_iterators(self):
        first = async_itertools.as_async([1, 3, 5])
        second = async_itertools.as_async([2, 4, 6, 7])
        third = async_itertools.as_async([8])
        fourth = async_itertools.as_async([])
        self.assertSetEqual(
            {item async for item in async_itertools.interleave(first, second, third, fourth)},
            {1, 2, 3, 4, 5, 6, 7, 8}
        )

    async def test_time_order(self):
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
