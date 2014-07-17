import os


for f in os.listdir("./docs"):
    header = "../partials/header-" + f
    f = os.path.join("docs", f)
    print f
    page = open(f).read()
    page = page.split('\n') 
    try:
        idx = page.index('        <h2>Examples</h2>')
        page = page[:idx-1] + ["{{ EXAMPLES }}"] + page[-1:]
        with open(header, 'w') as newpage:
            newpage.write("\n".join(page))
    except:
        print "could not do %s" % f

