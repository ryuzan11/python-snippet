from lib.validate import validate
import lib.add_schema as aschema


SCHEMA = {
    **aschema.REQUIRED_ID,
    **aschema.OPTIONAL_NAME,
    **aschema.OPTIONAL_HOBBY
}


def main():
    params = {
        'id': '1',
        'name': 'ryu',
        'hobby': 'baseball'
    }

    errors = validate(SCHEMA, params)

    print(errors)


if __name__ == '__main__':
    main()
