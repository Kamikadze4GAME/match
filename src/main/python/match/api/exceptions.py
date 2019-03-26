import json


def bad_request(e):
    return (
        json.dumps(
            {"status": "fail", "error": ["bad request"], "method": "", "result": []}
        ),
        400,
    )


def page_not_found(e):
    return (
        json.dumps(
            {"status": "fail", "error": ["not found"], "method": "", "result": []}
        ),
        404,
    )


def method_not_allowed(e):
    return (
        json.dumps(
            {
                "status": "fail",
                "error": ["method not allowed"],
                "method": "",
                "result": [],
            }
        ),
        405,
    )


def server_error(e):
    return (
        json.dumps({"status": "fail", "error": [str(e)], "method": "", "result": []}),
        500,
    )
