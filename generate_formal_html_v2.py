import markdown
import re
import requests
import base64
import zlib
import os

md_path = "C:\\Users\\G Rohith Lakshman\\.gemini\\antigravity\\brain\\35458b52-1e37-4a24-9d6f-bfb3f0846978\\UrbanFlow_AI_Documentation.md"
html_path = "C:\\Users\\G Rohith Lakshman\\.gemini\\antigravity\\brain\\35458b52-1e37-4a24-9d6f-bfb3f0846978\\UrbanFlow_AI_Documentation.html"
download_dir = "C:\\Users\\G Rohith Lakshman\\Downloads"

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_hr = text.find('## 📑 Table of Contents')
if start_hr != -1:
    text = text[start_hr:] 

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

# Process Mermaid blocks
mermaid_blocks = re.findall(r'```mermaid\n(.*?)```', text, re.DOTALL)
for i, block in enumerate(mermaid_blocks):
    b64 = base64.urlsafe_b64encode(zlib.compress(block.encode('utf-8'), 9)).decode('utf-8')
    res = requests.get(f'https://kroki.io/mermaid/png/{b64}', headers={'User-Agent': 'Mozilla/5.0'})
    img_path = os.path.join(download_dir, f'diagram_{i}.png')
    with open(img_path, 'wb') as img_f:
        img_f.write(res.content)
    
    # Replace the mermaid block with an img tag with constrained height to prevent page breaks
    img_tag = f'<div style="text-align: center;"><img src="{img_path.replace("\\\\", "/")}" height="480"></div>'
    text = text.replace(f'```mermaid\n{block}```', img_tag)

html = markdown.markdown(text, extensions=['tables', 'fenced_code', 'md_in_html'])

css = """
<style>
@page {
    margin: 1cm;
}
body { 
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
    line-height: 1.5; 
    color: #000000; /* Pure black text */
    font-size: 11pt;
}
.team-info {
    text-align: center;
    font-size: 10pt;
    margin-bottom: 10px;
    color: #000000;
}
.thin-hr {
    border: 0;
    border-bottom: 1px solid #000000;
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
    color: #000000;
}
th { 
    background-color: #f7f9fc; 
    font-weight: bold; 
    color: #0b2e59;
}
img { 
    max-width: 100%; 
    margin: 15px 0; 
}
ul, ol {
    margin-top: 5px;
    margin-bottom: 10px;
}
li {
    margin-bottom: 5px;
}
</style>
"""

final_html = f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>UrbanFlow AI Documentation</title>\n{css}\n</head>\n<body>\n{html}\n</body>\n</html>'

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("HTML generated with rendered Mermaid diagrams and pure black font.")
