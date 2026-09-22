import markdown
import sys

md_path = "C:\\Users\\G Rohith Lakshman\\.gemini\\antigravity\\brain\\35458b52-1e37-4a24-9d6f-bfb3f0846978\\UrbanFlow_AI_Documentation.md"
html_path = "C:\\Users\\G Rohith Lakshman\\.gemini\\antigravity\\brain\\35458b52-1e37-4a24-9d6f-bfb3f0846978\\UrbanFlow_AI_Documentation.html"

# We will read the markdown and strip out the HTML cover page I added previously, replacing it with a clean markdown version that matches the formal look.
with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the old HTML cover page block
start_hr = text.find('## 📑 Table of Contents')
if start_hr != -1:
    text = text[start_hr:] # Keep everything from Table of contents onwards

# Add the formal header
formal_header = """
<table width="100%" cellpadding="15" cellspacing="0" border="0" style="background-color: #0b2e59; margin-bottom: 10px;">
    <tr>
        <td align="center" style="border: none; background-color: #0b2e59;">
            <div style="color: white; font-size: 28pt; font-weight: bold; margin-bottom: 5px;">URBANFLOW AI</div>
            <div style="color: white; font-size: 14pt;">Lane-Aware Adaptive Traffic Optimization System</div>
        </td>
    </tr>
</table>

<div class="team-info">
    <b>Team Name:</b> GOD-FATHER &nbsp;|&nbsp; <b>Category:</b> Computer Vision &nbsp;|&nbsp; <b>Event:</b> HACKZEN 2026 OPEN CHALLENGE<br>
    <b>Team Members:</b> G Rohith Lakshman | Jeyabharathi S | Madhavan S | Bavanraj M | Ramadharshini G
</div>
<hr class="thin-hr">

"""

text = formal_header + text

html = markdown.markdown(text, extensions=['tables', 'fenced_code', 'md_in_html'])

css = """
<style>
@page {
    margin: 1cm;
}
body { 
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
    line-height: 1.5; 
    color: #1a1a1a; 
    font-size: 11pt;
}
.header-banner {
    background-color: #0b2e59; /* Dark Navy Blue */
    color: white;
    text-align: center;
    padding: 20px;
    margin-bottom: 10px;
}
.header-banner h1 {
    color: white;
    margin: 0;
    font-size: 28pt;
    font-weight: bold;
    text-transform: uppercase;
}
.header-banner h2 {
    color: white;
    margin: 5px 0 0 0;
    font-size: 14pt;
    font-weight: normal;
}
.team-info {
    text-align: center;
    font-size: 10pt;
    margin-bottom: 10px;
    color: #333;
}
.thin-hr {
    border: 0;
    border-bottom: 1px solid #ccc;
    margin: 15px 0;
}
h1, h2, h3 { 
    color: #0b2e59; 
    font-weight: bold;
}
h2 {
    font-size: 16pt;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 5px;
    margin-top: 25px;
}
h3 {
    font-size: 13pt;
    margin-top: 15px;
}
table { 
    width: 100%; 
    border-collapse: collapse; 
    margin: 15px 0; 
}
th, td { 
    border: 1px solid #d0d0d0; 
    padding: 10px; 
    text-align: left; 
    font-size: 10pt;
}
th { 
    background-color: #f7f9fc; 
    font-weight: bold; 
    color: #0b2e59;
}
img { 
    max-width: 100%; 
    margin: 15px 0; 
    border: 1px solid #ccc;
}
ul, ol {
    margin-top: 5px;
    margin-bottom: 10px;
}
li {
    margin-bottom: 5px;
}
code {
    background: #f4f4f4;
    padding: 2px 4px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
}
pre {
    background: #f4f4f4;
    padding: 10px;
    border: 1px solid #ccc;
}
</style>
"""

final_html = f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>UrbanFlow AI Documentation</title>\n{css}\n</head>\n<body>\n{html}\n</body>\n</html>'

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Formal HTML generated successfully!")
