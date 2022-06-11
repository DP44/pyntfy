import requests

from pyntfy import action

class Notification:
    """
    A class representing a notification.
    """
    def __init__(self, topic: str, message: str, url: str='https://ntfy.sh/',
                 title: str='', priority: str='default', tags: str='',
                 click: str='', attach: str='', delay: str='',
                 cache: bool=True, firebase: bool=True) -> None:
        """
        A class representing a notification.

        Arguments:
            topic -- The topic name to send notifications to.
            message -- Main body of the message as shown in the notification.

        Keyword Arguments:
            url -- The url to use. This should be set when using a custom server. (default: {'https://ntfy.sh/'})
            title -- Message title. (default: {''})
            priority -- Message priority. (default: {'default'})
            tags -- Tags and emojis. (default: {''})
            click -- URL to open when the notification is clicked. (default: {''})
            attach -- URL to send as an attachment. (default: {''})
            delay -- Timestamp or duration for delayed delivery. (default: {''})
            cache -- If the notification should be stored server-side or not. (default: {True})
            firebase -- If the notification should be sent to firebase or not. (default: {True})
        """
        self.topic = topic
        self.message = message
        self.url = url
        self.title = title
        self.priority = priority
        self.tags = tags
        self.click = click
        self.attach = attach
        self.delay = delay
        self.cache = cache
        self.firebase = firebase

        self.actions = []
        
    def add_action(self, action: action.Action):
        """
        Adds an action to the notification.

        Arguments:
            action -- The action to add.
        """
        # Only 3 user actions are accepted.
        if len(self.actions) >= 3:
            return
        
        self.actions.append(action)
    
    def get_actions_string(self) -> str:
        """
        Constructs a string representation of the attached actions.

        Returns:
            A string representing all of the attached actions.
        """
        # We don't have any actions attached to this notification.
        if len(self.actions) == 0:
            return ''
        
        str_actions = ''

        for action in self.actions:
            str_actions += f'{str(action)}; '

        # Remove trailing semicolon.
        str_actions = str_actions[:len(str_actions) - 2]

        return str_actions
    
    def send(self) -> bool:
        """
        Sends the notification.

        Returns:
            A bool value representing if the operation was successful.
        """
        r = requests.post(f'{self.url}{self.topic}', data=self.message, headers={
            'Title': self.title,
            'Priority': self.priority,
            'Tags': self.tags,
            'Delay': self.delay,
            'Actions': self.get_actions_string(),
            'Click': self.click,
            'Attach': self.attach,
            'Cache': '' if self.cache else 'no',
            'Firebase': '' if self.firebase else 'no'
        })

        return r.status_code == 200
