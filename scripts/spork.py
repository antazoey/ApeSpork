import click
from ape.cli import ConnectedProviderCommand, ape_cli_context
from ape.types import AddressType

from ._lib import get_spork_contract


@click.group()
def cli():
    """
    Commands for SPORK.
    """


@cli.command(cls=ConnectedProviderCommand)
@ape_cli_context()
@click.argument("account")
def balance(cli_ctx, account):
    """
    Check your SPORK balance.
    """
    contract = get_spork_contract()

    if account.endswith(".eth"):
        account = cli_ctx.conversion_manager.convert(account, AddressType)
    elif not account.startswith("0x"):
        # Is an account alias.
        account = cli_ctx.account_manager.load(account).AddressType
    # else: is an address

    balance = contract.balanceOf(account)
    click.echo(balance)
