# Copyright (c) KAITO authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" # Force CPU-only execution for testing
os.environ["OMP_NUM_THREADS"] = "1" # Force single-threaded for testing to prevent segfault while loading embedding model
os.environ["MKL_NUM_THREADS"] = "1"  # Force MKL to use a single thread
