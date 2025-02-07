# -*- coding: utf-8 -*-
# Copyright 2018 The Blueoil Authors. All Rights Reserved.
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
# =============================================================================
from easydict import EasyDict
import tensorflow as tf

from lmnet.common import Tasks
from lmnet.networks.object_detection.yolo_v2 import YoloV2
from lmnet.datasets.open_images_v4 import OpenImagesV4BoundingBox
from lmnet.data_processor import Sequence
from lmnet.pre_processor import (
    ResizeWithGtBoxes,
    DivideBy255,
)
from lmnet.post_processor import (
    FormatYoloV2,
    ExcludeLowScoreBox,
    NMS,
)
from lmnet.data_augmentor import (
    Brightness,
    Color,
    Contrast,
    FlipLeftRight,
    Hue,
    SSDRandomCrop,
)

IS_DEBUG = False
# distributed training
IS_DISTRIBUTION = False

NETWORK_CLASS = YoloV2
DATASET_CLASS = OpenImagesV4BoundingBox

IMAGE_SIZE = [416, 416]
BATCH_SIZE = 8
DATA_FORMAT = "NHWC"
TASK = Tasks.OBJECT_DETECTION
CLASSES = DATASET_CLASS(subset="train", batch_size=1).classes
MAX_STEPS = 1000000
SAVE_STEPS = 50000
TEST_STEPS = 10000
SUMMARISE_STEPS = 1000

PRE_PROCESSOR = Sequence([
    ResizeWithGtBoxes(size=IMAGE_SIZE),
    DivideBy255(),
])
anchors = [
    (1.3221, 1.73145), (3.19275, 4.00944), (5.05587, 8.09892), (9.47112, 4.84053), (11.2364, 10.0071)
]
score_threshold = 0.05
nms_iou_threshold = 0.5
nms_max_output_size = 100
POST_PROCESSOR = Sequence([
    FormatYoloV2(
        image_size=IMAGE_SIZE,
        classes=CLASSES,
        anchors=anchors,
        data_format=DATA_FORMAT,
    ),
    ExcludeLowScoreBox(threshold=score_threshold),
    NMS(iou_threshold=nms_iou_threshold, max_output_size=nms_max_output_size, classes=CLASSES,),
])

# for debug
# IS_DEBUG = True
# SUMMARISE_STEPS = 1


# pretrain
IS_PRETRAIN = False
PRETRAIN_VARS = [
    'block_1/conv/kernel:0',
    'block_1/bn/beta:0',
    'block_1/bn/gamma:0',
    'block_1/bn/moving_mean:0',
    'block_1/bn/moving_variance:0',
    'block_2/conv/kernel:0',
    'block_2/bn/beta:0',
    'block_2/bn/gamma:0',
    'block_2/bn/moving_mean:0',
    'block_2/bn/moving_variance:0',
    'block_3/conv/kernel:0',
    'block_3/bn/beta:0',
    'block_3/bn/gamma:0',
    'block_3/bn/moving_mean:0',
    'block_3/bn/moving_variance:0',
    'block_4/conv/kernel:0',
    'block_4/bn/beta:0',
    'block_4/bn/gamma:0',
    'block_4/bn/moving_mean:0',
    'block_4/bn/moving_variance:0',
    'block_5/conv/kernel:0',
    'block_5/bn/beta:0',
    'block_5/bn/gamma:0',
    'block_5/bn/moving_mean:0',
    'block_5/bn/moving_variance:0',
    'block_6/conv/kernel:0',
    'block_6/bn/beta:0',
    'block_6/bn/gamma:0',
    'block_6/bn/moving_mean:0',
    'block_6/bn/moving_variance:0',
    'block_7/conv/kernel:0',
    'block_7/bn/beta:0',
    'block_7/bn/gamma:0',
    'block_7/bn/moving_mean:0',
    'block_7/bn/moving_variance:0',
    'block_8/conv/kernel:0',
    'block_8/bn/beta:0',
    'block_8/bn/gamma:0',
    'block_8/bn/moving_mean:0',
    'block_8/bn/moving_variance:0',
    'block_9/conv/kernel:0',
    'block_9/bn/beta:0',
    'block_9/bn/gamma:0',
    'block_9/bn/moving_mean:0',
    'block_9/bn/moving_variance:0',
    'block_10/conv/kernel:0',
    'block_10/bn/beta:0',
    'block_10/bn/gamma:0',
    'block_10/bn/moving_mean:0',
    'block_10/bn/moving_variance:0',
    'block_11/conv/kernel:0',
    'block_11/bn/beta:0',
    'block_11/bn/gamma:0',
    'block_11/bn/moving_mean:0',
    'block_11/bn/moving_variance:0',
    'block_12/conv/kernel:0',
    'block_12/bn/beta:0',
    'block_12/bn/gamma:0',
    'block_12/bn/moving_mean:0',
    'block_12/bn/moving_variance:0',
    'block_13/conv/kernel:0',
    'block_13/bn/beta:0',
    'block_13/bn/gamma:0',
    'block_13/bn/moving_mean:0',
    'block_13/bn/moving_variance:0',
    'block_14/conv/kernel:0',
    'block_14/bn/beta:0',
    'block_14/bn/gamma:0',
    'block_14/bn/moving_mean:0',
    'block_14/bn/moving_variance:0',
    'block_15/conv/kernel:0',
    'block_15/bn/beta:0',
    'block_15/bn/gamma:0',
    'block_15/bn/moving_mean:0',
    'block_15/bn/moving_variance:0',
    'block_16/conv/kernel:0',
    'block_16/bn/beta:0',
    'block_16/bn/gamma:0',
    'block_16/bn/moving_mean:0',
    'block_16/bn/moving_variance:0',
    'block_17/conv/kernel:0',
    'block_17/bn/beta:0',
    'block_17/bn/gamma:0',
    'block_17/bn/moving_mean:0',
    'block_17/bn/moving_variance:0',
    'block_18/conv/kernel:0',
    'block_18/bn/beta:0',
    'block_18/bn/gamma:0',
    'block_18/bn/moving_mean:0',
    'block_18/bn/moving_variance:0',
    'block_19/conv/kernel:0',
    'block_19/bn/beta:0',
    'block_19/bn/gamma:0',
    'block_19/bn/moving_mean:0',
    'block_19/bn/moving_variance:0',
    'block_20/conv/kernel:0',
    'block_20/bn/beta:0',
    'block_20/bn/gamma:0',
    'block_20/bn/moving_mean:0',
    'block_20/bn/moving_variance:0',
    'block_21/conv/kernel:0',
    'block_21/bn/beta:0',
    'block_21/bn/gamma:0',
    'block_21/bn/moving_mean:0',
    'block_21/bn/moving_variance:0',
    'block_22/conv/kernel:0',
    'block_22/bn/beta:0',
    'block_22/bn/gamma:0',
    'block_22/bn/moving_mean:0',
    'block_22/bn/moving_variance:0',

    # 'conv_23/kernel:0',
    # 'conv_23/bias:0',

]
PRETRAIN_DIR = "saved/convert_weight_from_darknet/yolo_v2/checkpoints"
PRETRAIN_FILE = "save.ckpt"

NETWORK = EasyDict()
NETWORK.OPTIMIZER_CLASS = tf.train.MomentumOptimizer
NETWORK.OPTIMIZER_KWARGS = {"momentum": 0.9, "learning_rate": 1e-5}
# NETWORK.LEARNING_RATE_FUNC = tf.train.piecewise_constant
# In the origianl yolov2 Paper, with a starting learning rate of 10−3, dividing it by 10 at 60 and 90 epochs.
# Train data num per epoch is 16551
# NETWORK.LEARNING_RATE_KWARGS = {
#     "values": [1e-4, 1e-4],
#     "boundaries": [10000],
# }
NETWORK.IMAGE_SIZE = IMAGE_SIZE
NETWORK.BATCH_SIZE = BATCH_SIZE
NETWORK.DATA_FORMAT = DATA_FORMAT
NETWORK.ANCHORS = anchors
NETWORK.OBJECT_SCALE = 5.0
NETWORK.NO_OBJECT_SCALE = 1.0
NETWORK.CLASS_SCALE = 1.0
NETWORK.COORDINATE_SCALE = 1.0
NETWORK.LOSS_IOU_THRESHOLD = 0.6
NETWORK.WEIGHT_DECAY_RATE = 0.0005
NETWORK.SCORE_THRESHOLD = score_threshold
NETWORK.NMS_IOU_THRESHOLD = nms_iou_threshold
NETWORK.NMS_MAX_OUTPUT_SIZE = nms_max_output_size
NETWORK.LOSS_WARMUP_STEPS = int(12800 / BATCH_SIZE)

# dataset
DATASET = EasyDict()
DATASET.BATCH_SIZE = BATCH_SIZE
DATASET.DATA_FORMAT = DATA_FORMAT
DATASET.PRE_PROCESSOR = PRE_PROCESSOR
DATASET.AUGMENTOR = Sequence([
    FlipLeftRight(),
    Brightness((0.75, 1.25)),
    Color((0.75, 1.25)),
    Contrast((0.75, 1.25)),
    Hue((-10, 10)),
    SSDRandomCrop(min_crop_ratio=0.7),
])
