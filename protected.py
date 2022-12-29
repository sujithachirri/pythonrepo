class protected_sample_class:
    _tutor= None
    _place=None
    _experiance=None
    def __init__(self,tutor,place,experiance):
        self._tutor=tutor
        self._place=place
        self._experiance=experiance
    def _displaytutordetails(self):
        print("tutor:{} -place:{} -experiance:{}".format(self._tutor,self._place,self._experiance))
class derived_protected_class(protected_sample_class):
    def display_protected_method_variables(self):
        self._displaytutordetails()
class non_derived_class(derived_protected_class):
    def trytodisplayprotectedmethod(self):
        self._displaytutordetails()
derivedclassobj=derived_protected_class("sujitha","nellore",0)
derivedclassobj.display_protected_method_variables()

nonderivedobj=non_derived_class("rohi","tanuku",0)
nonderivedobj.trytodisplayprotectedmethod()
