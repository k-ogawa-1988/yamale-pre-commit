import argparse
import os
from typing import List


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Run yamale on a set of files.'
    )
    parser.add_argument(
        '--schema', '-s', dest='schema', default='.yamale-validate-schema.yaml', help='File path of schema. Both absolute path and relative path can be accepted.'
    )
    parser.add_argument(
        '--parser', '-p', dest='parser', default='pyyaml', choices=['pyyaml', 'ruamel'], help='YAML library to load files. Choices are "ruamel" or "pyyaml" (default).'
    )
    parser.add_argument(
        '--no-strict', dest='no_strict', action='store_true', help='Disable strict mode, unexpected elements in the data will be accepted.',
    )
    parser.add_argument('--debug', dest='debug', action='store_true', help='Output debug logs.')
    parser.add_argument('path', nargs='+', help='Files to validate.')
    args = parser.parse_args(argv)

    if args.debug:
        print(f'[debug] args = {args}')

    path_to_check = []  # type: List[str]
    for path in args.path:  # type: str
        real_path = os.path.realpath(path or '.')
        if not os.path.exists(real_path) or not os.path.isfile(real_path):
            print(f'File "{real_path}" does not exists or not a file.')
            return 2

        path_to_check.append(real_path)

    if args.debug:
        print(f'[debug] path_to_check = {path_to_check}')

    if args.debug:
        print(f'[debug] path_to_check = {path_to_check}')

    if not path_to_check:
        print('No files to scan.')
        return 0

    ret = 0

    try:
        import yamale

        for file_path in path_to_check:
            data = yamale.make_data(path=file_path, parser=args.parser)

            schema_path = os.path.join(os.getcwd(), args.schema)

            if file_path == schema_path:
                continue

            try:
                schema = yamale.make_schema(path=schema_path, parser=args.parser)
            except FileNotFoundError:
                print(f'Validating: "{file_path}" with schema "{schema_path}"')
                print(f'  Skip: schema not found.')
                continue

            print(f'Validating: "{file_path}" with schema "{schema_path}"')
            yamale.validate(schema=schema, data=data, strict=not args.no_strict)
            print('  Okay!')

    except yamale.YamaleError as e:
        print('  Validation failed!')
        for result in e.results:
            for error in result.errors:
                print(f'    {error}')
        ret = 1

    except BaseException as e:
        print(e)
        ret = 3

    return ret


if __name__ == '__main__':
    exit(main())
