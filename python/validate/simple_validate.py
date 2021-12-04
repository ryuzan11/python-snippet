from cerberus import Validator
from cerberus.errors import BasicErrorHandler


def validate(schema, params, check_func=None):

    cerberus_vali = Validator(schema, error_handler=BasicErrorHandler())
    cerberus_res = cerberus_vali.validate(params)

    errors = []

    print(cerberus_res)

    # if not cerberus_res:
    #     errors.extend(cerberus_errors_to_json(cerberus_vali.errors, cerberus_vali))

    if check_func:
        additional_errors = check_func(params)

        if additional_errors:
            errors.extend(additional_errors)

    return errors
