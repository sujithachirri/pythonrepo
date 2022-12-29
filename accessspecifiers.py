#public methods--can be accessed from any where ny defaut everything

class Public_sample_accessmodifier:
    def __init__(self,course,duration):
        self.course=course
        self.duration=duration
    def display_public_class_method(self):
        print("course: {} - Duration: {}".format(self.course, self.duration))
        publicobj=publ
        publicobj.display_public_class_method()