from xero import exceptions


def translate_status_exception(error, api_instance, api_method):
    if error.status == 400:
        return exceptions.PayrollUkBadRequestException(http_resp=error.http_resp)
    return exceptions.translate_status_exception(error, api_instance, api_method)
