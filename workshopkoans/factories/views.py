import json
from django.http import HttpResponse
from django.shortcuts import render



def post_retriever(request):
    """
    Given a network and a post_id retrieves data using that networks
    API for the post_id

    :param request:
    :return:
    """
    network = request.GET['network']
    post_id = request.GET['post_id']
    if network == 'twitter':
        tweet_dict = api_get_tweet_from_id(post_id)
        post = {'post': tweet_dict['tweet']}
    elif network == 'facebook':
        post = api_get_facebook_post_by_id(post_id)

    response = HttpResponse(
        json.dumps(post), content_type='application/javascript')
    return response

def api_get_tweet_from_id(id):
    """
    Do not change

    :param id:
    :return:
    """
    # make network call
    return {'tweet': id}

def api_get_facebook_post_by_id(id):
    """
    Do not change

    :param id:
    :return:
    """
    # make network call
    return {'post': id}


def get_network_api_factory(network):
    pass

class FBPostAPI(object):
    pass

class TwitterTweetAPI(object):
    pass
