import webapp2

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write("This is the index!")

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
