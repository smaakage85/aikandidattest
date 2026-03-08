"""Flask web application – AI Political Candidate Test (prank)."""

from __future__ import annotations

import random
from pathlib import Path

from flask import Flask, render_template

_HERE = Path(__file__).resolve().parent


def create_app() -> Flask:
    """Application factory."""
    app = Flask(
        __name__,
        template_folder=str(_HERE / "templates"),
        static_folder=str(_HERE / "static"),
    )
    app.secret_key = "this-is-a-prank-not-real-security"  # noqa: S105

    # ------------------------------------------------------------------
    # The fixed "match" result
    # ------------------------------------------------------------------
    candidate = {
        "name": "Sikandar Siddique",
        "party": "Frie Grønne",
        "photo": "candidate.png",
        "confidence": f"{random.uniform(94.0, 99.9):.1f}",
        "tagline": "Vi skal turde tage de svære kampe – for klimaet og for hinanden.",
        "policies": [
            "Ambitiøs klimahandling og grøn omstilling nu",
            "Styrket mental sundhed og trivsel for unge",
            "Et mere retfærdigt og rummeligt samfund for alle",
        ],
    }

    @app.route("/")
    def login():
        """Landing page with fake social login buttons."""
        return render_template("login.html")

    @app.route("/analyzing")
    def analyzing():
        """Fake progress / profiling screen."""
        return render_template("analyzing.html")

    @app.route("/result")
    def result():
        """Show the (fixed) candidate match."""
        return render_template("result.html", candidate=candidate)

    return app
