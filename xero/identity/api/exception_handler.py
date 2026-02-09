from xero import exceptions


def translate_status_exception(error, api_instance, api_method):
    if error.status == 400:
        if error.http_resp.text == '{"error":"invalid_grant"}':
            return exceptions.OAuth2InvalidGrantError(http_resp=error.http_resp)
        return exceptions.BadRequestException(http_resp=error.http_resp)
    return exceptions.translate_status_exception(error, api_instance, api_method)
