import click
import yaml

from pydjinni.context import pass_logger, GenerateContext
from pydjinni.defs import DEFAULT_CONFIG_PATH
from pydjinni.parser.parser import IdlParser
from pydjinni.parser.resolver import Resolver
from pathlib import Path
from .java.command import java
from logging import Logger
from pydjinni.generator.java import java_target
from pydjinni.generator.objc import objc_target
from pydjinni.generator.cpp import cpp_target
from pydjinni.config.config_factory import ConfigFactory
from pydjinni.parser.type_factory import TypeFactory
from rich.pretty import pretty_repr

from pydjinni.defs import TYPES_DIR
from ...config.config import load_config


@click.group()
@click.option('--config', '-c', default=DEFAULT_CONFIG_PATH, type=Path,
              help="path to the config file.")
@click.option('--option', '-o', multiple=True, type=str,
              help="overwrite or extend options from the config file. Example: `-o java.out=java_out`")
@click.option('--interactive', '-i', is_flag=True,
              help="start generation in interactive mode. Will listen for any changes in the input files and update the output "
                   "on every change until terminated.")
@click.argument('idl', type=Path)
@pass_logger
@click.pass_context
def generate(ctx, logger: Logger, config: Path, option, interactive, idl: Path):
    """
    generate glue-code from the provided IDL file.

    COMMAND specifies the target languages.
    """

    if not idl.exists():
        click.echo("IDL file cannot be found")
    logger.info("generating language bindings")


    configuration = load_config(
        path=config,
        options=option,
        option_group="generate",
        logger=logger)
    resolver = Resolver(logger)
    resolver.load(TYPES_DIR / "int.yaml")
    ast = IdlParser(logger, resolver).parse(idl)


    ctx.obj = GenerateContext(
        config=configuration,
        ast=ast,
        interactive=interactive)


generate.add_command(java)