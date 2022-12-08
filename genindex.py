import os;

indextemplate = '''
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
		<title>{path}</title>
	</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col">
					<h1>Index of {path}</h1>
					<hr>
				</div>
			</div>
			<div class="row">
				<div class="col">
					<table>
						{table}
					</table>
				</div>
			</div>
		</div>
	</body>
</html>
'''

for (root, dirs, files) in os.walk("maven"):
	dirs.sort()
	files.sort()
	if "index.html" in files:
		files.remove("index.html")
	table = ""
	for d in dirs:
		table += '<tr><td><a href="{linkto}/">{linkto}/</a></td></tr>\n'.format(linkto = d)
	for f in files:
		table += '<tr><td><a href="{linkto}">{linkto}</a></td></tr>\n'.format(linkto = f)
	html = indextemplate.format(path = root, table = table)
	indexfile = open(root + "/index.html", "w")
	indexfile.write(html)
	indexfile.close()

	