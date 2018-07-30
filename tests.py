"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        client = party.app.test_client()
        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        client = party.app.test_client()
        result = self.client.get("/")

        self.assertIn(b"Please RSVP", result.data)
        self.assertNotIn(b"123 Magic Unicorn Way",result.data)



    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        client = party.app.test_client()

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        self.assertNotIn(b"Please RSVP", result.data)
        self.assertIn(b"123 Magic Unicorn Way",result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself

        client = party.app.test_client()
        rsvp_info = {'name': "Mel", 'email': "jane@jane.com"}
        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        self.assertIn(b"Sorry, Mel. This is kind of awkward.", result.data)
        # self.assertNotIn(b"123 Magic Unicorn Way",result.data)
        


if __name__ == "__main__":
    unittest.main()
