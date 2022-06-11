from pyntfy import notify

def test_trigger():
    """
    Tests for notification triggers.
    """
    notifications = notify.Notify('test_triggers')
    
    assert notifications.trigger() == True, 'Failed to send default trigger!'
    assert notifications.trigger(priority='high') == True, 'Failed to send trigger with high priority!'
    assert notifications.trigger(delay='1m') == True, 'Failed to send scheduled trigger!'
    