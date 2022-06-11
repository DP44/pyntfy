
# pyntfy

A module for interacting with [ntfy.sh](https://ntfy.sh/) notifications.

------------------------------------------------------------------  
### Installation
You can install pyntfy via pip.
```
$ pip install pyntfy
```

------------------------------------------------------------------  
### Examples
```py
from pyntfy import notify

notifier = notify.Notify('sample_topic')

# Send a sample notification.
notifier.send('Hello, world!', title='Notification Title')

# Wait one minute before triggering a notification.
notifier.trigger(delay='1m')
```

------------------------------------------------------------------  



<!-- TODO: Finish this -->
