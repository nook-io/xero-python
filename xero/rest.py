import io
import json
import logging
import re
import ssl
from urllib.parse import urlencode
import aiohttp
from multidict import CIMultiDictProxy
from xero.exceptions import ApiException, ApiValueError

logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):
    def __init__(self, resp: aiohttp.ClientResponse, data: bytes) -> None:
        self.aiohttp_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = data

    def getheaders(self) -> CIMultiDictProxy[str]:
        return self.aiohttp_response.headers

    def getheader(self, name: str, default: str | None = None) -> str | None:
        return self.aiohttp_response.headers.get(name, default)


class RESTClientObject:
    def __init__(self, configuration, pools_size=4, maxsize=None) -> None:
        if maxsize is None:
            maxsize = configuration.connection_pool_maxsize
        ssl_context = ssl.create_default_context(cafile=configuration.ssl_ca_cert)
        if configuration.cert_file:
            ssl_context.load_cert_chain(
                configuration.cert_file, keyfile=configuration.key_file
            )
        if not configuration.verify_ssl:
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
        connector = aiohttp.TCPConnector(limit=maxsize, ssl=ssl_context)
        self.proxy = configuration.proxy
        self.proxy_headers = configuration.proxy_headers
        self.pool_manager = aiohttp.ClientSession(connector=connector, trust_env=True)

    async def close(self):
        await self.pool_manager.close()

    async def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        method = method.upper()
        assert method in ["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"]
        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )
        post_params = post_params or {}
        headers = headers or {}
        query_params = {}
        timeout = _request_timeout or 5 * 60
        if "Content-Type" not in headers:
            headers["Content-Type"] = "application/json"
        args = {"method": method, "url": url, "timeout": timeout, "headers": headers}
        if self.proxy:
            args["proxy"] = self.proxy
        if self.proxy_headers:
            args["proxy_headers"] = self.proxy_headers
        if query_params:
            args["url"] += "?" + urlencode(query_params)
        if method in ["POST", "PUT", "PATCH", "OPTIONS", "DELETE"]:
            if re.search("json", headers["Content-Type"], re.IGNORECASE):
                if body is not None:
                    body = json.dumps(body)
                args["data"] = body
            elif headers["Content-Type"] == "application/x-www-form-urlencoded":
                args["data"] = aiohttp.FormData(post_params)
            elif headers["Content-Type"] == "multipart/form-data":
                del headers["Content-Type"]
                data = aiohttp.FormData()
                for param in post_params:
                    k, v = param
                    if isinstance(v, tuple) and len(v) == 3:
                        data.add_field(k, value=v[1], filename=v[0], content_type=v[2])
                    else:
                        if isinstance(v, dict):
                            v = json.dumps(v)
                        elif isinstance(v, int):
                            v = str(v)
                        data.add_field(k, v)
                args["data"] = data
            elif isinstance(body, bytes):
                args["data"] = body
            else:
                msg = """Cannot prepare a request message for provided
                         arguments. Please check that your arguments match
                         declared content type."""
                raise ApiException(status=0, reason=msg)
        r = await self.pool_manager.request(**args)
        if _preload_content:
            data = await r.read()
            r = RESTResponse(r, data)
            logger.debug("response body: %s", r.data)
            if not 200 <= r.status <= 299:
                raise ApiException(http_resp=r)
        return r

    async def get_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "GET",
            url,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    async def head_request(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "HEAD",
            url,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    async def options_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "OPTIONS",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def delete_request(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "DELETE",
            url,
            headers=headers,
            query_params=query_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def post_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "POST",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def put_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "PUT",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def patch_request(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "PATCH",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )
