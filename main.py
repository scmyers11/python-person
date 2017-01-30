import webapp2
import person

class Index(webapp2.RequestHandler):
    def get(self):
        me = person.Person("Stephen Myers", ["scmyers11@gmail.com", "stephen@impresscareer.com"], "(636) 368-5639")
        self.response.write(str(me))

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
