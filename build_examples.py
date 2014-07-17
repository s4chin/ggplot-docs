import os
from bs4 import BeautifulSoup, NavigableString 
from ggplot import *

dirname = "examples"

for f in os.listdir(dirname):
    print f
    example_file = open(os.path.join(dirname, f)).read()
    soup = BeautifulSoup(example_file)
    all_examples = []
    # run the examples
    for i, example in enumerate(soup.find_all("example")):
        code = example.text
        code = code.strip().strip("#")
        template = """
        <div class="row">
            <div class="col-sm-6">
                <pre class="prettyprint">{code}</pre>
            </div>
            <div class="col-sm-6">
                <img src="{STATIC_URL}/img/newdocs/{f}_example_{i}.png">
            </div>
        </div>
        """
        template = template.format(code=code, f=f, i=i, STATIC_URL="{{ STATIC_URL }}")
        plotcode = code[code.find("ggplot("):]
        code += "\np = " + plotcode
        code += "\nggsave('static/img/newdocs/%s_example_%d.png', p)" % (f, i)
        exec(code)
        all_examples.append(template)

    # make the new page
    headerfile = os.path.join("partials", "header-" + f.replace('.py', '.html'))
    header = open(headerfile).read()
    header = header.replace("{{ EXAMPLES }}", "\n".join(all_examples))
    docfile = os.path.join("pages/docs", f.replace('.py', '.html'))
    with open(docfile, 'w') as doc:
        doc.write(header)
