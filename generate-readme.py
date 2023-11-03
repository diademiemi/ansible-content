#!/usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML content
with open('content.yml', 'r') as file:
    content = yaml.safe_load(file)

# Set up Jinja2 environment and loader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('README.md.j2')  # Assume you have a Jinja2 template for markdown

# Render the template with YAML content
rendered = template.render(content=content)

# Write to README.md
with open('README.md', 'w') as readme:
    readme.write(rendered)
