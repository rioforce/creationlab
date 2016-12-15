import os

openHTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Creation Lab</title>
</head>

<body>
  <h1>Creation Lab Index</h1>
  <ul>
"""

closeHTML = """</ul>
</body>
</html>
"""


with open("index.html", "wt", encoding="utf-8") as f:
    f.write(openHTML)
    for dir in os.listdir():
        if os.path.isdir(dir):
            print(dir[10])
            fName = (dir[11:] if dir[10] == "-" else dir[10:])
            f.write('    <li><a href="{0}/{1}.html">{0}</a></li>\n'.format(dir, fName))
    f.write(closeHTML)
