#!/usr/bin/env python3
# Copyright 2023 Linkall Inc.
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

import argparse

import json
import yaml
from vanus.connect.customsource import run_http_source

from .labeling import HttpLabelMaker


def main():
    parser = argparse.ArgumentParser(
        prog="labeling-source", description="vanus connect source labeling", epilog="Linkall Inc."
    )
    parser.add_argument("--config", help="the label source config")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    labels = json.loads(config["label"])
    label_maker = HttpLabelMaker(config["source_path"], config["target_path"], config=labels)

    run_http_source(config["port"], config["target"], label_maker.label, name=config.get("name", __name__))


if __name__ == "__main__":
    main()
