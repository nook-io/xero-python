import copy
import http.client as httplib
import logging
import sys
from .oauth2 import OAuth2Token

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    "multipleOf",
    "maximum",
    "exclusiveMaximum",
    "minimum",
    "exclusiveMinimum",
    "maxLength",
    "minLength",
    "pattern",
    "maxItems",
    "minItems",
}


class Configuration:
    _default = None

    def __init__(
        self,
        host=None,
        api_key=None,
        api_key_prefix=None,
        username=None,
        password=None,
        access_token=None,
        server_index=None,
        server_variables=None,
        server_operation_index=None,
        server_operation_variables=None,
        ssl_ca_cert=None,
        oauth2_token=None,
    ) -> None:
        self._base_path = "https://api.xero.com/api.xro/2.0" if host is None else host
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        self.temp_folder_path = None
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        self.username = username
        self.password = password
        self.access_token = access_token
        self.oauth2_token: OAuth2Token | None = oauth2_token
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("xero.accounting")
        self.logger_format = "%(asctime)s %(levelname)s %(message)s"
        self.logger_stream_handler = None
        self.logger_file_handler = None
        self.logger_file = None
        self.debug = False
        self.verify_ssl = True
        self.ssl_ca_cert = ssl_ca_cert
        self.cert_file = None
        self.key_file = None
        self.assert_hostname = None
        self.tls_server_name = None
        self.connection_pool_maxsize = 100
        self.proxy = None
        self.proxy_headers = None
        self.safe_chars_for_path_param = ""
        self.retries = None
        self.client_side_validation = True
        self.socket_options = None
        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        self.date_format = "%Y-%m-%d"

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ("logger", "logger_file_handler"):
                setattr(result, k, copy.deepcopy(v, memo))
        result.logger = copy.copy(self.logger)
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        cls._default = default

    @classmethod
    def get_default_copy(cls):
        return cls.get_default()

    @classmethod
    def get_default(cls):
        if cls._default is None:
            cls._default = Configuration()
        return cls._default

    @property
    def logger_file(self):
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        self.__logger_file = value
        if self.__logger_file:
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value
        if self.__debug:
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            httplib.HTTPConnection.debuglevel = 1
        else:
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(
            identifier, self.api_key.get(alias) if alias is not None else None
        )
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    async def auth_settings(self):
        auth = {}
        if self.access_token is not None:
            return {
                "OAuth2": {
                    "type": "oauth2",
                    "in": "header",
                    "key": "Authorization",
                    "value": "Bearer " + self.access_token,
                }
            }
        elif self.oauth2_token is not None:
            return {"OAuth2": self.oauth2_token.get_auth_settings()}
        return auth

    def to_debug_report(self):
        return (
            "Python SDK Debug Report:\n"
            "OS: {env}\n"
            "Python Version: {pyversion}\n"
            "Version of the API: 6.3.0\n"
            "SDK Package Version: 1.0.0".format(env=sys.platform, pyversion=sys.version)
        )

    def get_host_settings(self):
        return [
            {
                "url": "https://api.xero.com/api.xro/2.0",
                "description": "The Xero Accounting API exposes accounting and related functions of the main Xero application and can be used for a variety of purposes such as creating transactions like invoices and credit notes, right through to extracting accounting data via our reports endpoint.",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        if index is None:
            return self._base_path
        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers
        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers))
            )
        url = server["url"]
        for variable_name, variable in server.get("variables", {}).items():
            used_value = variables.get(variable_name, variable["default_value"])
            if "enum_values" in variable and used_value not in variable["enum_values"]:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name], variable["enum_values"]
                    )
                )
            url = url.replace("{" + variable_name + "}", used_value)
        return url

    @property
    def host(self):
        return self.get_host_from_settings(
            self.server_index, variables=self.server_variables
        )

    @host.setter
    def host(self, value):
        self._base_path = value
        self.server_index = None
