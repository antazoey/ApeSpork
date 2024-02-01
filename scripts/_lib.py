from ape import Contract, accounts, chain, project
from ape.contracts import ContractInstance

SPORK_ETHEREUM_MAINNET = "0xb624FdE1a972B1C89eC1dAD691442d5E8E891469"
SPORK_POLYGON_MUMBAI = "0x9CA6a77C8B38159fd2dA9Bd25bc3E259C33F5E39"
SPORK_DATA = {
    "ethereum": {"mainnet": {"address": SPORK_ETHEREUM_MAINNET}},
    "polygon": {"mainnet": {"address": SPORK_POLYGON_MUMBAI}},
}


def get_spork_contract() -> ContractInstance:
    ecosystem = chain.provider.network.ecosystem
    network = chain.provider.network
    network_name = network.name.replace("-fork", "")
    data = SPORK_DATA.get(ecosystem.name, {}).get(network_name, {})

    if network.is_local:
        account = accounts.test_accounts[0]
        return account.deploy(project.Spork, "Spork", "SPORK", account)

    address = data.get("address", SPORK_ETHEREUM_MAINNET)
    return Contract(address)
