# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from absl.testing import absltest

import jax
import jax._src.lib.xla_bridge as xla_bridge
from jax.config import config
import jax._src.test_util as jtu


config.parse_flags_with_absl()


class HeapProfilerTest(unittest.TestCase):
  # These tests simply test that the heap profiler API does not crash; they do
  # not check functional correctness.

  def testBasics(self):
    client = xla_bridge.get_backend()
    _ = client.heap_profile()

    a = jax.device_put(1)
    _ = client.heap_profile()

    # Heap profiler doesn't crash with deleted buffer
    a.delete()
    _ = client.heap_profile()

if __name__ == "__main__":
  absltest.main(testLoader=jtu.JaxTestLoader())
