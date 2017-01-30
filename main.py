import webapp2
import person

page_layout = """
<!DOCTYPE html>
<html>
<head>
    <title>Who I Am</title>
</head>
<body>
    <h1>
        <a href="/">Who Am I?</a>
    </h1>
    <div class="content">
        %(content)s
    </div>
</body>
</html>
"""

class Handler(webapp2.RequestHandler):
    def renderContent(self, content=""):
        self.response.write(page_layout % { "content" : content })

class Index(Handler):
    def get(self):
        me = person.Person("Stephen Myers", ["scmyers11@gmail.com", "stephen@impresscareer.com"], "(636) 368-5639")
        self.renderContent(str(me))

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
