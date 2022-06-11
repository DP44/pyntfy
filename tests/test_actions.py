import pyntfy
from pyntfy import actions

def test_actions():
    """
    Tests for using actions.
    """
    notif = pyntfy.Notification('test_actions', 'Hello, world!')
    notif.add_action(actions.ViewAction('Label', 'https://www.example.com/'))
    notif.add_action(actions.HTTPAction('Label', 'https://www.example.com/'))
    notif.send()