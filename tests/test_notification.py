import pyntfy

def test_notification():
    """
    Tests for sending notifications.
    """

    notif = pyntfy.Notification('test_notification', 'Hello, world!', title='Notification Title')
    assert notif.send() == True, 'Failed to send notification'

    timed_notif = pyntfy.Notification('test_notification', 'Hello, world!', delay='1m')
    assert timed_notif.send() == True, 'Failed to send timed notification!'
    # TODO: Add more tests.
