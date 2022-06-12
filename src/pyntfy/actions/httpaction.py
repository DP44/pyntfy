from pyntfy import action 

class HTTPAction(action.Action):
    """
    HTTP action implementation. (https://ntfy.sh/docs/publish/#send-http-request)
    """
    def __init__(self, label: str, url: str, method: str='POST',
                 headers: list=[], body: str='', clear: bool=False) -> None:
        """
        HTTP action implementation. (https://ntfy.sh/docs/publish/#send-http-request)

        Arguments:
            label -- Label of the action button in the notification.
            url -- URL to which the HTTP request will be sent.

        Keyword Arguments:
            method -- HTTP method to use for request. (default: {'POST'})
            headers -- HTTP headers to pass in request. (default: {[]})
            body -- HTTP body. (default: {''})
            clear -- Clear notification after HTTP request succeeds. If
                     the request fails, the notification is not cleared. (default: {False})
        """
        super().__init__('http', label, clear)
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body

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
        str_rep = f'action={self.action}, label="{self.label}", url={self.url}, method={self.method}, '

        # Add headers to string.
        for header in self.headers.keys():
            str_rep += f'headers.{header}="{self.headers[header]}", '
        
        str_rep += f'body="{self.body}", clear={str(self.clear).lower()}'

        return str_rep