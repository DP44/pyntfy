import json
import requests

class Notify:
    """
    A class for easy interaction with ntfy.sh notifications.
    """
    def __init__(self, topic: str, url: str='https://ntfy.sh/') -> None:
        """
        A class for easy interaction with ntfy.sh notifications.

        Arguments:
            topic -- The topic name to send notifications to.

        Keyword Arguments:
            url -- The url to use for topics. This should be set when using a custom server. (default: {'https://ntfy.sh/'})
        """
        self.topic = topic
        self.url = url

    def trigger(self, priority: str='default', delay: str=''):
        """
        Triggers a notification event.

        Keyword Arguments:
            priority -- Message priority (default: {'default'})
            delay -- Timestamp or duration for delayed delivery (default: {''})

        Returns:
            A bool value representing if the operation was successful.
        """
        r = requests.post(f'{self.url}{self.topic}', data='', headers={
            'Priority': priority,
            'Delay': delay
        })

        return r.status_code == 200
    
    def send(self, message: str, title: str='', priority: str='default',
             tags: str='', actions: str='', click: str='', attach: str='',
             delay: str='', cache: bool=True, firebase: bool=True):
        """
        Sends a notification.

        Arguments:
            message -- Main body of the message as shown in the notification.

        Keyword Arguments:
            title -- Message title (default: {''})
            priority -- Message priority (default: {'default'})
            tags -- Tags and emojis (default: {''})
            actions -- User actions (default: {''})
            click -- URL to open when the notification is clicked (default: {''})
            attach -- URL to send as an attachment (default: {''})
            delay -- Timestamp or duration for delayed delivery (default: {''})
            cache -- If the notification should be stored server-side or not (default: {True})
            firebase -- If the notification should be sent to firebase or not (default: {True})
        
        Returns:
            A bool value representing if the operation was successful.
        """
        r = requests.post(f'{self.url}{self.topic}', data=message, headers={
            'Title': title,
            'Priority': priority,
            'Tags': tags,
            'Delay': delay,
            'Actions': actions,
            'Click': click,
            'Attach': attach,
            'Cache': '' if cache else 'no',
            'Firebase': '' if firebase else 'no'
        })

        return r.status_code == 200
    
    def send_json(self, json_data: dict):
        """
        Sends a notification using JSON data.

        Arguments:
            json_data -- A dict containing the parameters for the toast notification.

        Returns:
            A bool value representing if the operation was successful.
        """
        if len(json_data) == 0:
            return False
        
        r = requests.post(self.url, data=json.dumps({ 
            'topic': self.topic, **json_data
        }))

        return r.status_code == 200