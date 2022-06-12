from pyntfy import action 

# TODO: This needs testing.

class BroadcastAction(action.Action):
    """
    Broadcast action implementation. (https://ntfy.sh/docs/publish/#send-android-broadcast)
    """
    def __init__(self, label: str, intent: str='io.heckel.ntfy.USER_ACTION',
                 extras: list=[], clear: bool=False) -> None:
        """
        Broadcast action implementation. (https://ntfy.sh/docs/publish/#send-android-broadcast)

        Arguments:
            label -- Label of the action button in the notification.

        Keyword Arguments:
            intent -- Android intent name. (default: {'io.heckel.ntfy.USER_ACTION'})
            extras -- Android intent extras. (default: {[]})
            clear -- Clear notification after action button is tapped. (default: {False})
        """
        super().__init__('broadcast', label, clear)
        self.intent = intent
        self.extras = extras

    def get_short_header(self) -> str:
        """
        Constructs a string representation of the action in the short header format.

        Returns:
            The constructed string.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        """
        Constructs a string representation of the action.

        Returns:
            The constructed string.
        """
        str_rep = f'action={self.action}, label="{self.label}", intent={self.intent}, '

        # Add extras to string.
        for extra in self.extras.keys():
            str_rep += f'extras.{extra}={self.extras[extra]}, '

        str_rep += f'clear={str(self.clear).lower()}'

        return str_rep
