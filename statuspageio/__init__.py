"""
StatusPage.io  API V1 library client for Python.
~~~~~~~~~~~~~~~~~~~~~
Usage::
  >>> import statuspageio
  >>> client = statuspageio.Client(api_key=os.environ.get('STATUSPAGE_API_KEY')
  >>> status = client.components.list()
  >>> print status
:copyright: (c) 2016 by GameSparks TechOps (techops@gamesparks.com).
:license: MIT, see LICENSE for more details.
"""

from statuspageio.client import Client
from statuspageio.configuration import Configuration
from statuspageio.errors import (
    BaseError,
    ConfigurationError,
    RateLimitError,
    RequestError,
    ResourceError,
    ServerError,
)
from statuspageio.http_client import HttpClient
from statuspageio.services import (
    ComponentsService,
    IncidentsService,
    MetricsService,
    PageService,
    SubscribersService,
    UsersService,
)
from statuspageio.version import VERSION


__all__ = [
    Client,
    Configuration,
    BaseError,
    ConfigurationError,
    RateLimitError,
    RequestError,
    ResourceError,
    ServerError,
    HttpClient,
    ComponentsService,
    IncidentsService,
    MetricsService,
    PageService,
    SubscribersService,
    UsersService,
    VERSION,
]
#
