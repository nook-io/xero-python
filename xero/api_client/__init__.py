import datetime
import json
import mimetypes
import os
import re
import tempfile
from decimal import Decimal
from enum import Enum
from functools import cached_property
from urllib.parse import quote
from dateutil.parser import parse
from pydantic import SecretStr
from xero import rest
from xero.api_client.api_response import ApiResponse
from xero.api_client.configuration import Configuration
from xero.api_client.deserializer import deserialize
from xero.exceptions import (
    AccessTokenExpiredError,
    ApiException,
    ApiValueError,
    OAuth2TokenGetterError,
    OAuth2TokenSaverError,
)
from xero.models import BaseModel


class ModelFinder:
    def __init__(self, models_module):
        self.models = models_module

    def find_model(self, name):
        return getattr(self.models, name)


class ApiClient:
    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
        "date": datetime.date,
        "datetime": datetime.datetime,
        "object": object,
    }

    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None,
        oauth2_token_saver=None,
        oauth2_token_getter=None,
    ) -> None:
        if configuration is None:
            configuration = Configuration()
        self.configuration = configuration
        self._rest_client = None
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        self.user_agent = "OpenAPI-Generator/1.0.0/python"
        self.client_side_validation = configuration.client_side_validation
        self._oauth2_token_saver = oauth2_token_saver
        self._oauth2_token_getter = oauth2_token_getter

    @property
    def rest_client(self) -> rest.RESTClientObject:
        if self._rest_client is None:
            self._rest_client = rest.RESTClientObject(self.configuration)
        return self._rest_client

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def close(self):
        if self._rest_client:
            await self._rest_client.close()

    @property
    def user_agent(self):
        return self.default_headers["User-Agent"]

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers["User-Agent"] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    _default = None

    @classmethod
    def get_default(cls):
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        cls._default = default

    async def __call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_types_map=None,
        response_model_finder=None,
        auth_settings=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
        _request_auth=None,
    ):
        config = self.configuration
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params["Cookie"] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params, collection_formats)
            )
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace(
                    "{%s}" % k, quote(str(v), safe=config.safe_chars_for_path_param)
                )
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params, collection_formats)
            post_params.extend(self.files_parameters(files))
        await self.update_params_for_auth(
            header_params,
            query_params,
            auth_settings,
            resource_path,
            method,
            body,
            request_auth=_request_auth,
        )
        if body:
            body = self.sanitize_for_serialization(body)
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            url = _host + resource_path
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(query_params, collection_formats)
            url += "?" + url_query
        response_data = await self.request(
            method,
            url,
            query_params=query_params,
            headers=header_params,
            post_params=post_params,
            body=body,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
        )
        self.last_response = response_data
        return_data = None
        if not _preload_content:
            return response_data
        response_type = None
        if response_types_map:
            response_type = response_types_map.get(str(response_data.status), None)
            if (
                not response_type
                and isinstance(response_data.status, int)
                and 100 <= response_data.status <= 599
            ):
                response_type = response_types_map.get(
                    str(response_data.status)[0] + "XX", None
                )
        if response_type != "bytearray":
            match = None
            content_type = response_data.getheader("content-type")
            if content_type is not None:
                match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
            encoding = match.group(1) if match else "utf-8"
            response_data.data = response_data.data.decode(encoding)
        if response_type == "bytearray":
            return_data = response_data.data
        elif response_type:
            return_data = self.deserialize(
                response_data, response_type, response_model_finder
            )
        else:
            return_data = None
        if _return_http_data_only:
            return return_data
        else:
            return ApiResponse(
                status_code=response_data.status,
                data=return_data,
                headers=response_data.getheaders(),
                raw_data=response_data.data,
            )

    def sanitize_for_serialization(self, obj):
        if isinstance(obj, BaseModel):
            serialized = {}
            for attr_name, attr_type in obj.openapi_types.items():
                attr_value = getattr(obj, attr_name)
                if attr_value is not None:
                    key = obj.attribute_map[attr_name]
                    attr_value = self.sanitize_for_serialization(attr_value)
                    serialized[key] = attr_value
            return serialized
        elif obj is None:
            return None
        elif isinstance(obj, SecretStr):
            return obj.get_secret_value()
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        if isinstance(obj, dict):
            obj_dict = obj
        else:
            if hasattr(obj, "to_dict") and callable(getattr(obj, "to_dict")):
                obj_dict = obj.to_dict()
            else:
                obj_dict = obj.__dict__
        return {
            key: self.sanitize_for_serialization(val) for key, val in obj_dict.items()
        }

    def deserialize(self, response, response_type, response_model_finder):
        if response_type == "file":
            return self.__deserialize_file(response)
        try:
            data = json.loads(response.data, parse_float=Decimal)
        except ValueError:
            data = response.data
        return deserialize(response_type, data, response_model_finder)

    async def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_types_map=None,
        response_model_finder=None,
        auth_settings=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
        _request_auth=None,
    ):
        args = (
            resource_path,
            method,
            path_params,
            query_params,
            header_params,
            body,
            post_params,
            files,
            response_types_map,
            response_model_finder,
            auth_settings,
            _return_http_data_only,
            collection_formats,
            _preload_content,
            _request_timeout,
            _host,
            _request_auth,
        )
        return await self.__call_api(*args)

    async def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        if method == "GET":
            return await self.rest_client.get_request(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "HEAD":
            return await self.rest_client.head_request(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "OPTIONS":
            return await self.rest_client.options_request(
                url,
                query_params=query_params,
                headers=headers,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
            )
        elif method == "POST":
            return await self.rest_client.post_request(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PUT":
            return await self.rest_client.put_request(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PATCH":
            return await self.rest_client.patch_request(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "DELETE":
            return await self.rest_client.delete_request(
                url,
                query_params=query_params,
                headers=headers,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == "multi":
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == "ssv":
                        delimiter = " "
                    elif collection_format == "tsv":
                        delimiter = "\t"
                    elif collection_format == "pipes":
                        delimiter = "|"
                    else:
                        delimiter = ","
                    new_params.append((k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = json.dumps(v)
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == "multi":
                    new_params.extend((k, str(value)) for value in v)
                else:
                    if collection_format == "ssv":
                        delimiter = " "
                    elif collection_format == "tsv":
                        delimiter = "\t"
                    elif collection_format == "pipes":
                        delimiter = "|"
                    else:
                        delimiter = ","
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v))
                    )
            else:
                new_params.append((k, quote(str(v))))
        return "&".join(["=".join(map(str, item)) for item in new_params])

    def files_parameters(self, files=None):
        params = []
        if files:
            for k, v in files.items():
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, "rb") as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (
                            mimetypes.guess_type(filename)[0]
                            or "application/octet-stream"
                        )
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))
        return params

    def select_header_accept(self, accepts):
        if not accepts:
            return
        for accept in accepts:
            if re.search("json", accept, re.IGNORECASE):
                return accept
        return accepts[0]

    def select_header_content_type(self, content_types):
        if not content_types:
            return None
        for content_type in content_types:
            if re.search("json", content_type, re.IGNORECASE):
                return content_type
        return content_types[0]

    async def update_params_for_auth(
        self,
        headers,
        queries,
        auth_settings,
        resource_path,
        method,
        body,
        request_auth=None,
    ):
        if not auth_settings:
            return
        if request_auth:
            self._apply_auth_params(
                headers, queries, resource_path, method, body, request_auth
            )
            return
        for auth in auth_settings:
            auth_setting = await self.configuration.auth_settings()
            if auth_setting:
                auth_setting = auth_setting.get(auth)
                if callable(auth_setting):
                    auth_setting = await auth_setting(self)
                self._apply_auth_params(
                    headers, queries, resource_path, method, body, auth_setting
                )

    def _apply_auth_params(
        self, headers, queries, resource_path, method, body, auth_setting
    ):
        if auth_setting["in"] == "cookie":
            headers["Cookie"] = auth_setting["value"]
        elif auth_setting["in"] == "header":
            if auth_setting["type"] != "http-signature":
                headers[auth_setting["key"]] = auth_setting["value"]
        elif auth_setting["in"] == "query":
            queries.append((auth_setting["key"], auth_setting["value"]))
        else:
            raise ApiValueError("Authentication token must be in `query` or `header`")

    def __deserialize_file(self, response):
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)
        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(
                r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition
            ).group(1)
            path = os.path.join(os.path.dirname(path), filename)
        with open(path, "wb") as f:
            f.write(response.data)
        return path

    def get_oauth2_token(self):
        if not self._oauth2_token_getter:
            raise OAuth2TokenGetterError(
                "Invalid oauth2_token_getter={!r} function".format(
                    self._oauth2_token_getter
                )
            )
        return self._oauth2_token_getter()

    def set_oauth2_token(self, token):
        if not self._oauth2_token_saver:
            raise OAuth2TokenSaverError(
                "Invalid oauth2_token_saver={!r} function".format(
                    self._oauth2_token_saver
                )
            )
        self._oauth2_token_saver(token)

    async def refresh_oauth2_token(self):
        oauth2_token = self.configuration.oauth2_token
        oauth2_token.update_token(**self.get_oauth2_token())
        if await oauth2_token.refresh_access_token(self):
            return self.get_oauth2_token()

    async def revoke_oauth2_token(self):
        oauth2_token = self.configuration.oauth2_token
        oauth2_token.update_token(**self.get_oauth2_token())
        if await oauth2_token.revoke_access_token(self):
            return self.get_oauth2_token()

    async def get_client_credentials_token(self, app_store_billing=False):
        oauth2_token = self.configuration.oauth2_token
        if await oauth2_token.get_client_credentials_access_token(
            self, app_store_billing
        ):
            return self.get_oauth2_token()

    def oauth2_token_getter(self, token_getter):
        self._oauth2_token_getter = token_getter
        return token_getter

    def oauth2_token_saver(self, token_saver):
        self._oauth2_token_saver = token_saver
        return token_saver
