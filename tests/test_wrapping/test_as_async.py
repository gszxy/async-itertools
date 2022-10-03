import time
from unittest import IsolatedAsyncioTestCase

import async_itertools


class TestAsAsync(IsolatedAsyncioTestCase):

    async def test_without_interval(self):
        nums = list(range(10))
        self.assertEqual(nums, [item async for item in async_itertools.as_async(nums)])
        assert nums == [item async for item in async_itertools.as_async(set(nums))]
        assert nums == [item async for item in async_itertools.as_async(num for num in nums)]

    async def test_with_interval(self):
        nums = list(range(5))
        start = time.time()
        assert nums == [item async for item in async_itertools.as_async(nums, 0.01)]
        duration = time.time() - start
        self.assertAlmostEqual(duration, 0.05, delta=0.01)
