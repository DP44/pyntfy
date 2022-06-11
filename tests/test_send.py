from pyntfy import notify

def test_send():
    """
    Tests for sending notifications.
    """
    notifications = notify.Notify('test_triggers')

    # TODO: Add send_json() tests.
    assert notifications.send('Hello, world!') == True, 'Failed to send notification.'
    assert notifications.send('Hello, world!', title='Notification Title') == True, 'Failed to send notification with title.'