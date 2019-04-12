from argparse import ArgumentParser, _SubParsersAction

import sentry_sdk
from sentry_sdk import capture_exception


from trinity import __version__
from trinity.extensibility import BaseIsolatedPlugin

class SentryPlugin(BaseIsolatedPlugin):
    sentry_host: str
    project_id: str
    public_key: str
    protocol: str

    @property
    def name(self) -> str:
        return "Sentry Error Reporting Plugin"

    def configure_parser(self,
                         arg_parser: ArgumentParser,
                         subparser: _SubParsersAction) -> None:
        sentry_parser = arg_parser.add_argument_group('sentry')

        sentry_parser.add_argument(
            "--sentry-host",
            help="Sentry host to report errors",
        )

        sentry_parser.add_argument(
            "--sentry-project-id",
            help="Sentry project ID",
        )

        sentry_parser.add_argument(
            "--sentry-pub-key",
            help="Sentry public key",
        )

        sentry_parser.add_argument(
            "--sentry-insecure",
            action="store_true",
            help="Enable insecure error reporting over HTTP",
        )

    def on_ready(self, manager_eventbus) -> None:
        args = self.context.args

        self.sentry_host = args.sentry_host or 'sentry.io'
        self.project_id = args.sentry_project_id
        self.public_key = args.sentry_pub_key
        self.protocol = 'https'

        if args.sentry_insecure:
            self.protocol = 'http'

        init_url = f'{self.protocol}://{self.public_key}@{self.sentry_host}/{self.project_id}'
        sentry_sdk.init(init_url, release=f'trinity@{__version__}')

        try:
            self.start()
        except:
            capture_exception()

    def do_start(self) -> None:
        pass
