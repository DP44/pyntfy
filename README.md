
# pyntfy

A module for interacting with [ntfy.sh](https://ntfy.sh/) notifications.

------------------------------------------------------------------  
### Installation
You can install pyntfy via pip.
```
$ pip install pyntfy
```

------------------------------------------------------------------  
### Usage
```py
import pyntfy

# Send a sample notification.
notif = pyntfy.Notification('test_notification', 'Hello, world!', title='Notification Title')
notif.send()

# Send a timed notification.
timed_notif = pyntfy.Notification('test_notification', 'Hello, world!', title='Notification Title', delay='1m')
timed_notif.send()
```

#### Actions
```py
import pyntfy

notif = pyntfy.Notification('test_actions', 'Hello, world!')
notif.add_action(pyntfy.actions.ViewAction('Label', 'https://www.example.com/'))
notif.send()
```

------------------------------------------------------------------  
### Planned Features
- Webhook support.
- Allow for JSON data as input.
- Proper tests.

<!-- TODO: README -->
