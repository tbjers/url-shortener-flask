import spacy
from profanity_filter import ProfanityFilter

nlp = spacy.load("en_core_web_sm")
pf = ProfanityFilter(nlps={"en": nlp})
nlp.add_pipe(pf.spacy_component, last=True)


class TestProfanityFilter(object):
    def test_is_clean(self):
        doc = nlp("hello")
        assert doc._.is_profane == False

    def test_is_profane(self):
        doc = nlp("fuck")
        assert doc._.is_profane == True
