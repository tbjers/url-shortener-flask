from profanity_filter import ProfanityFilter

class TestProfanityFilter(object):
    @classmethod
    def setup_class(cls):
        cls.pf = ProfanityFilter()

    def test_is_clean(self):
        assert self.pf.is_clean('hello') == True

    def test_is_profane(self):
        assert self.pf.is_profane('fuck') == True
