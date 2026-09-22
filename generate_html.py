import markdown
import sys

md_path = "C:\\Users\\G Rohith Lakshman\\.gemini\\antigravity\\brain\\35458b52-1e37-4a24-9d6f-bfb3f0846978\\UrbanFlow_AI_Documentation.md"
html_path = "C:\\Users\\G Rohith Lakshman\\.gemini\\antigravity\\brain\\35458b52-1e37-4a24-9d6f-bfb3f0846978\\UrbanFlow_AI_Documentation.html"

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

html = markdown.markdown(text, extensions=['tables', 'fenced_code', 'md_in_html'])

css = """
<style>
body { font-family: 'Segoe UI', Roboto, sans-serif; line-height: 1.6; max-width: 1000px; margin: auto; padding: 40px; color: #333; }
h1, h2, h3 { color: #06B6D4; font-family: 'Orbitron', sans-serif; }
table { width: 100%; border-collapse: collapse; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
th, td { border: 1px solid #e5e7eb; padding: 12px; text-align: left; }
th { background: #f3f4f6; color: #1f2937; }
img { max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); margin: 20px 0; }
hr { border: 0; height: 1px; background: #06B6D4; margin: 40px 0; }
code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; color: #ef4444; }
pre { background: #1e293b; color: #f8fafc; padding: 16px; border-radius: 8px; overflow-x: auto; }
pre code { background: transparent; color: inherit; padding: 0; }
a { color: #06B6D4; text-decoration: none; }
</style>
"""

final_html = f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>UrbanFlow AI Documentation</title>\n{css}\n</head>\n<body>\n{html}\n</body>\n</html>'

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("HTML generated successfully!")
