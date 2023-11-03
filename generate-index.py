#!/usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader

def generate_html_from_yaml(yaml_file, template_file, output_file):
    # Load the YAML data
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    roles = data['ansible_content']['roles']
    collections = data['ansible_content']['collections']

    # Set up the Jinja2 environment and template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file)

    # Render the template with the data
    html_content = template.render(roles=roles, collections=collections)

    # Save the rendered content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

if __name__ == '__main__':
    generate_html_from_yaml('content.yml', 'index.html.j2', 'index.html')
