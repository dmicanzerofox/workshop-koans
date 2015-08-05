import urllib
from django.core.urlresolvers import reverse
from django.test import TestCase
from factories.views import get_network_api_factory, TwitterTweetAPI
from factories.views import FBPostAPI


class FactoriesTestCase(TestCase):
    """
    Use the factory design pattern to refactor the post_retriever view.
    Implement FBPostAPI and TwitterTweetAPI by subclassing NetworkAPIBase,
    and defining get_post in terms of the
     corresponding "api" method
     (ie. api_get_tweet_from_id, api_get_facebook_post_by_id)
    """
    def test_get_network_api_factory(self):
        """
        Test that the correct NetworkAPIBase subclass
         can be instantiated per network.
        :return:
        """
        retriever = get_network_api_factory('facebook')
        self.assertIsInstance(retriever, FBPostAPI)

        retriever = get_network_api_factory('twitter')
        self.assertIsInstance(retriever, TwitterTweetAPI)

    def test_fb_post_api_get_post(self):
        """
        :return:
        """
        fb_retreiver = FBPostAPI()
        post_id = 1
        self.assertEqual(
            fb_retreiver.get_post(post_id),
            {'post': post_id}
        )

    def test_twitter_tweet_api_get_post(self):
        """
        :return:
        """
        tw_retreiver = TwitterTweetAPI()
        post_id = 1
        self.assertEqual(
            tw_retreiver.get_post(post_id),
            {'post': post_id}
        )

    def test_post_retriever_get_post_facebook(self):
        """
        Tests that the post retriever can use FacebookPostAPI to
        get a post.  Modify post_retriever to use the factory function.
        This should act as a regression test.

        :return:
        """
        params = {
            'network': 'facebook',
            'post_id': '1'
        }
        response = self.client.get(
            reverse('factories:post_retriever') +
            '?' + urllib.urlencode(params)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get('Content-type'), 'application/javascript')
        expected = {'post': params['post_id']}
        self.assertJSONEqual(response.content, expected)

    def test_post_retriever_get_post_twitter(self):
        """
        Tests that the post retriever can use TwitterTweetAPI to
        get a post.
        This should act as a regression test, and provide feedback
        for the `post_retriever` refactor.

        :return:
        """
        params = {
            'network': 'twitter',
            'post_id': '1'
        }
        response = self.client.get(
            reverse('factories:post_retriever') +
            '?' + urllib.urlencode(params)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get('Content-type'), 'application/javascript')
        expected = {'post': params['post_id']}
        self.assertJSONEqual(response.content, expected)
