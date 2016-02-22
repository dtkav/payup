#!/usr/bin/env python

from jinja2 import Template
import json

with open("lambda.j2") as f:
    template = Template(f.read())

with open("config.json") as f:
    config = json.loads(f.read())
    print(config)
    aws_lambda = template.render(**config)

with open("lambda.py", "w") as f:
    f.write(aws_lambda)
