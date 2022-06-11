class Action:
    """
    An abstract class representing an action.
    """
    def __init__(self, action: str, label: str, clear: bool) -> None:
        """
        An abstract class representing an action.

        Arguments:
            action -- Action type.
            label -- Label of the action button in the notification.
            clear -- Clear notification after action button is tapped.
        """
        self.action = action
        self.label = label
        self.clear = clear
    
    def get_short_header(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()