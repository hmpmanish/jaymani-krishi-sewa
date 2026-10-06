import base64

with open('jaymani_krishi_sewa_logo.jpg', 'rb') as f:
    b64_main = base64.b64encode(f.read()).decode('utf-8')
    main_src = 'data:image/jpeg;base64,' + b64_main

with open('sharda-university-logo-png_.png', 'rb') as f:
    b64_sharda = base64.b64encode(f.read()).decode('utf-8')
    sharda_src = 'data:image/png;base64,' + b64_sharda

with open('Project_Proposal_Report.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src=\"jaymani_krishi_sewa_logo.jpg\"', f'src=\"{main_src}\"')
html = html.replace('src=\"sharda-university-logo-png_.png\"', f'src=\"{sharda_src}\"')

with open('Project_Proposal_Report.html', 'w', encoding='utf-8') as f:
    f.write(html)
