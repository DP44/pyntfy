import pyntfy

def test_actions():
    """
    Tests for using actions.
    """
    notif = pyntfy.Notification('test_actions', 'Hello, world!')
    notif.add_action(pyntfy.actions.ViewAction('Label', 'https://www.example.com/'))
    notif.add_action(pyntfy.actions.HTTPAction('Label', 'https://www.example.com/'))
    notif.send()