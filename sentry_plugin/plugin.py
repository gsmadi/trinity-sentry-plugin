from argparse import ArgumentParser, _SubParsersAction

import sentry_sdk

from trinity.extensibility import BaseIsolatedPlugin

class SentryPlugin(BaseIsolatedPlugin):

    @property
    def name(self) -> str:
        return "Sentry Error Tracking Plugin"

    def configure_parser(self,
                         arg_parser: ArgumentParser,
                         subparser: _SubParsersAction) -> None:
        arg_parser.add_argument(
            "--sentry-host",
            action="store_true",
            help="Snetry host to report errors",
        )

        arg_parser.add_argument(
            "--sentry-project-id",
            action="store_true",
            help="Sentry Project ID",
        )

        arg_parser.add_argument(
            "--sentry-pub-key",
            action="store_true",
            help="Sentry public key",
        )

        arg_parser.add_argument(
            "--sentry-insecure",
            action="store_true",
            help="Enable insecure error reporting over HTTP",
        )

    def on_ready(self, manager_eventbus: TrinityEventBusEndpoint) -> None:
        sentry_sdk.init("https://4e71390f88824d0081226a6a83194ed7@sentry.io/1417193")

    def do_start(self) -> None:
        pass
