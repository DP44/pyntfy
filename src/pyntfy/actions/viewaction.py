from pyntfy import action 

class ViewAction(action.Action):
    """
    View action implementation. (https://ntfy.sh/docs/publish/#open-websiteapp)
    """
    def __init__(self, label: str, url: str, clear: bool=False) -> None:
        """
        View action implementation. (https://ntfy.sh/docs/publish/#open-websiteapp)

        Arguments:
            label -- Label of the action button in the notification.
            url -- URL to open when the action is tapped.

        Keyword Arguments:
            clear -- Clear notification after action button is tapped (default: {False})
        """
        super().__init__('view', label, clear)
        self.url = url

    def get_short_header(self) -> str:
        return ''

    def __str__(self) -> str:
        return f'action={self.action}, label="{self.label}", url={self.url}, ' + \
               f'clear={str(self.clear).lower()}'
