# Copyright 2025 DeepMind Technologies Limited
#
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
# ==============================================================================
"""Constants for Berkeley Humanoid."""

from etils import epath

from mujoco_playground._src import mjx_env
print(mjx_env.ROOT_PATH)
ROOT_PATH = mjx_env.ROOT_PATH / "locomotion" / "biped"
FLAT_TERRAIN_XML = (
    ROOT_PATH / "xmls" / "scene_mjx_feetonly_flat_terrain.xml"
)
ROUGH_TERRAIN_XML = (
    ROOT_PATH / "xmls" / "scene_mjx_feetonly_rough_terrain.xml"
)

def task_to_xml(task_name: str) -> epath.Path:
  return {
      "flat_terrain": FLAT_TERRAIN_XML,
      "rough_terrain": ROUGH_TERRAIN_XML,
  }[task_name]


FEET_SITES = [
    "l_foot",
    "r_foot",
]

LEFT_FEET_GEOMS = [
    "L_FOOT_GEOM",
]

RIGHT_FEET_GEOMS = [
    "R_FOOT_GEOM",
]

FEET_GEOMS = LEFT_FEET_GEOMS + RIGHT_FEET_GEOMS

FEET_POS_SENSOR = [f"{site}_pos" for site in FEET_SITES]

ROOT_BODY = "base_link"

GRAVITY_SENSOR = "upvector"
GLOBAL_LINVEL_SENSOR = "global_linvel"
GLOBAL_ANGVEL_SENSOR = "global_angvel"
LOCAL_LINVEL_SENSOR = "local_linvel"
ACCELEROMETER_SENSOR = "accelerometer"
GYRO_SENSOR = "gyro"
