import os

redirect_template = '''---
redirect_to: "http://erpnext.org/docs/{0}"
---
'''

for basepath, folders, files in os.walk('.'):
	for f in files:
		if f.endswith('.html'):
			fpath = os.path.join(basepath, f)
			print fpath
			with open(fpath, 'r') as _f:
				content = _f.read()
			fpath = fpath[:-5]
			if fpath.endswith('index'):
				fpath = fpath[:-5]
			fpath = fpath.strip('./')
			content = redirect_template.format(fpath) + content
			with open(os.path.join(basepath, f), 'w') as _f:
				_f.write(content)

