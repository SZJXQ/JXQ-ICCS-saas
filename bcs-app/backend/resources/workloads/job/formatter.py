# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from typing import Dict

from backend.resources.utils.common import calculate_duration
from backend.resources.workloads.common.formatter import WorkloadFormatter


class JobFormatter(WorkloadFormatter):
    """ Deployment 格式化 """

    def format_dict(self, resource_dict: Dict) -> Dict:
        res = self.format_common_dict(resource_dict)
        status = resource_dict['status']

        res.update(
            {
                'duration': calculate_duration(status.get('startTime'), status.get('completionTime')),
            }
        )
        return res
