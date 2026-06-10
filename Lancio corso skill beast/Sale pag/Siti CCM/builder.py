import json
import os
from jinja2 import Environment, FileSystemLoader

def build():
    # Load data
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Initialize Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Render
    output = template.render(data=data)

    # Save to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output)

    print("Successfully built index.html from data.json and template.html")

if __name__ == "__main__":
    build()
