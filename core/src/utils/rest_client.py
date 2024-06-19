# type: ignore
import asyncio
from functools import partial

import requests
from typing import Optional, Dict


class RestClient:
    """
    RestClient is a class needed to make async requests to an API using the
    requests library
    """

    def __init__(
        self,
        base_url: str,
        default_headers: Optional[Dict] = None,
    ) -> None:
        """
        Args:
            base_url (str): base url of the API
            default_headers (dict): default headers to be sent in all requests
        """
        self.base_url = base_url
        self.default_headers = default_headers or {}

    async def get(
        self,
        endpoint: str = "",
        query_params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
    ) -> requests.Response:
        """
        Makes a get request to the API

        Args:
            endpoint (str): endpoint of the base url to be called
            query_params (dict): query params to be sent in the request
            headers (dict): headers to be sent in the request

        Returns:
            requests.Response: response of the request
        """
        partial_get = partial(
            requests.get,
            f"{self.base_url}{endpoint}",
            params=query_params or {},
            headers={**self.default_headers, **(headers or {})},
        )
        return await asyncio.get_event_loop().run_in_executor(None, partial_get)