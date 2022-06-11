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
            label -- Label of the action button in the notification
            url -- URL to which the HTTP request will be sent

        Keyword Arguments:
            method -- HTTP method to use for request (default: {'POST'})
            headers -- HTTP headers to pass in request (default: {[]})
            body -- HTTP body (default: {''})
            clear -- Clear notification after HTTP request succeeds. If
                     the request fails, the notification is not cleared. (default: {False})
        """
        super().__init__('http', label, clear)
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body

    def get_short_header(self) -> str:
        return ''

    def __str__(self) -> str:
        # TODO: Headers
        return f'action={self.action}, label="{self.label}", url={self.url}, method={self.method}, ' + \
               f'body="{self.body}", clear={str(self.clear).lower()}'
