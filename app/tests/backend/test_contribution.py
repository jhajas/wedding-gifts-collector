from ferris.tests.lib import WithTestBed
from app.models.contribution import Contribution


class TestContribution(WithTestBed):

    def testQueries(self):
        # log in user one
        #self.loginUser('user1@example.com')

        # create tree contribution
	c1 = Contribution(gift="projektor",amount=2000)
        c1.put()

        c2 = Contribution(gift="projektor",amount=3250)
        c2.put()

        c3 = Contribution(gift="auto",amount=4000)
        c3.put()

        # Make sure we only get one for car contribution
        auto_donations = Contribution.collected('auto')

        assert auto_donations == 4000

        # Make sure we only get two for projektor contributions
        projektor_donations = Contribution.collected('projektor')

        assert projektor_donations == 5250

