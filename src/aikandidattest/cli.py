"""Console script entry point – starts the dev server."""

from __future__ import annotations

import argparse


def main() -> None:
    """Run the AI Kandidattest web app."""
    parser = argparse.ArgumentParser(description="AI Kandidattest – prank app")
    parser.add_argument(
        "--host", default="127.0.0.1", help="Host to bind to (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port", type=int, default=5000, help="Port to listen on (default: 5000)"
    )
    parser.add_argument("--debug", action="store_true", help="Enable Flask debug mode")
    args = parser.parse_args()

    from aikandidattest.app import create_app

    app = create_app()
    print(f"\n🗳️  AI Kandidattest running at http://{args.host}:{args.port}\n")
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
