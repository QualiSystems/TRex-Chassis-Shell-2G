"""
Tests for TrexChassisShell2GDriver.
"""
# pylint: disable=redefined-outer-name
from typing import Iterable

import pytest
import yaml
from _pytest.fixtures import SubRequest
from cloudshell.api.cloudshell_api import AttributeNameValue, CloudShellAPISession, ResourceInfo
from cloudshell.shell.core.driver_context import AutoLoadCommandContext
from cloudshell.traffic.tg import TGN_CHASSIS_FAMILY, TREX_CHASSIS_MODEL
from shellfoundry_traffic.test_helpers import TgTestHelpers, print_inventory, session, test_helpers  # noqa: F401

from trex_driver import TrexChassisShell2GDriver

TREX_USER = "trex"


@pytest.fixture(scope="session")
def sut(request: SubRequest) -> dict:
    """Yield the sut dictionary from the sut file."""
    with open(request.config.rootpath.joinpath(request.config.getoption("--tgn-sut")), "r") as yaml_file:
        return yaml.safe_load(yaml_file)


@pytest.fixture(params=["quali_sut.yaml"], ids=["linux"])
def address(request: SubRequest) -> str:
    """Yield TRex device under test parameters."""
    with open(request.param, "r") as yaml_file:
        trex_yaml = yaml.safe_load(yaml_file)
    return trex_yaml["server"]["ip"]


@pytest.fixture()
def autoload_context(test_helpers: TgTestHelpers, address: str) -> AutoLoadCommandContext:
    """Yield Ixia chassis shell command context for resource commands testing."""
    attributes = {f"{TREX_CHASSIS_MODEL}.User": TREX_USER}
    return test_helpers.autoload_command_context(TGN_CHASSIS_FAMILY, TREX_CHASSIS_MODEL, address, attributes)


@pytest.fixture()
def driver(test_helpers: TgTestHelpers, address: str) -> Iterable[TrexChassisShell2GDriver]:
    """Yield initialized TrexChassisShell2GDriver."""
    attributes = {f"{TREX_CHASSIS_MODEL}.User": TREX_USER}
    init_context = test_helpers.resource_init_command_context(
        TGN_CHASSIS_FAMILY, TREX_CHASSIS_MODEL, address, attributes, "test-trex"
    )
    driver = TrexChassisShell2GDriver()
    driver.initialize(init_context)
    yield driver
    driver.cleanup()


@pytest.fixture()
def autoload_resource(session: CloudShellAPISession, test_helpers: TgTestHelpers, address: str) -> Iterable[ResourceInfo]:
    """Yield Ixia chassis resource for shell autoload testing."""
    attributes = [AttributeNameValue(f"{TREX_CHASSIS_MODEL}.User", TREX_USER)]
    resource = test_helpers.create_autoload_resource(TREX_CHASSIS_MODEL, "tests/test-ixia", address, attributes)
    yield resource
    session.DeleteResource(resource.Name)


def test_autoload(driver: TrexChassisShell2GDriver, autoload_context: AutoLoadCommandContext) -> None:
    """Test direct (driver) auto load command."""
    inventory = driver.get_inventory(autoload_context)
    print_inventory(inventory)


def test_autoload_session(session: CloudShellAPISession, autoload_resource: ResourceInfo, address: str) -> None:
    """Test indirect (shell) autoload command."""
    session.AutoLoad(autoload_resource.Name)
    resource_details = session.GetResourceDetails(autoload_resource.Name)
    assert len(resource_details.ChildResources) == 1
    assert resource_details.ChildResources[0].FullAddress == f"{address}/M0"
