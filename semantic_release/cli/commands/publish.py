import logging
import shlex
import subprocess

import click
from rich import print as rprint
from twine.commands.upload import upload

from semantic_release.errors import InvalidConfiguration
from semantic_release.version import tags_and_versions

log = logging.getLogger(__name__)


@click.command()
@click.pass_context
def publish(ctx: click.Context) -> None:
    """
    This is the magic changelog function that writes out your beautiful changelog
    """
    runtime = ctx.obj
    repo = runtime.repo
    hvcs_client = runtime.hvcs_client
    translator = runtime.version_translator
    build_command = runtime.build_command
    dist_glob_patterns = runtime.dist_glob_patterns
    upload_to_repository = runtime.upload_to_repository
    upload_to_release = runtime.upload_to_release
    twine_settings = runtime.twine_settings

    if upload_to_repository and not twine_settings:
        ctx.fail(
            "Your configuration sets upload_to_repository = true, but your twine "
            "upload settings are invalid"
        )

    if runtime.global_cli_options.noop:
        rprint(
            "[bold cyan]:shield: 'noop' mode is enabled, semantic-release would "
            f"have run the build_command {build_command!r}"
        )
    else:
        try:
            subprocess.run(shlex.split(build_command), check=True)
        except subprocess.CalledProcessError as exc:
            ctx.fail(str(exc))

    if runtime.global_cli_options.noop and upload_to_repository:
        rprint(
            "[bold cyan]:shield: 'noop' mode is enabled, semantic-release would "
            "have uploaded files matching any of the globs "
            ", ".join(repr(g) for g in dist_glob_patterns) + " to your repository"
        )
    elif upload_to_repository:
        upload(upload_settings=twine_settings, dists=dist_glob_patterns)

    latest_tag = tags_and_versions(repo.tags, translator)[0][0]
    if upload_to_release and runtime.global_cli_options.noop:
        rprint(
            "[bold cyan]:shield: 'noop' mode is enabled, semantic-release would "
            "have uploaded files matching any of the globs "
            + ", ".join(repr(g) for g in dist_glob_patterns)
            + " to a remote VCS release, if supported"
        )
    elif upload_to_release:
        for pattern in dist_glob_patterns:
            hvcs_client.upload_dists(tag=latest_tag, dist_glob=pattern)

    rprint("[green]:sparkles: Done! :sparkles:")
