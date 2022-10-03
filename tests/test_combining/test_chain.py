from unittest import IsolatedAsyncioTestCase

import async_itertools


class TestAsAsync(IsolatedAsyncioTestCase):

    async def test_simple_case(self):
        self.assertListEqual(
            [1, 2, 3, 4, 5, 6],
            [item async for item in async_itertools.chain(
                async_itertools.as_async([1, 2, 3]),
                async_itertools.as_async([4, 5]),
                async_itertools.as_async([6])
            )]
        )

    async def test_empty_iterators(self):
        self.assertListEqual(
            [1, 2, 3, 4, 5, 6],
            [item async for item in async_itertools.chain(
                async_itertools.as_async([]),
                async_itertools.as_async([1, 2, 3]),
                async_itertools.as_async([]),
                async_itertools.as_async([4, 5, 6]),
                async_itertools.as_async([]),
            )]
        )
