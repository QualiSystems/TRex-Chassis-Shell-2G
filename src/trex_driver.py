"""
TRex chassis shell driver.
"""
import logging

from cloudshell.logging.qs_logger import get_qs_logger
from cloudshell.shell.core.driver_context import AutoLoadDetails, InitCommandContext, ResourceCommandContext
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from pytrex.trex_app import TrexApp, TrexServer

from trex_data_model import GenericTrafficGeneratorModule, GenericTrafficGeneratorPort, TrexChassisShell2G


class TrexChassisShell2GDriver(ResourceDriverInterface):
    """TRex chassis shell driver."""

    def __init__(self) -> None:
        """Initialize object variables, actual initialization is performed in initialize method."""
        self.logger: logging.Logger = None
        self.resource: TrexChassisShell2G = None

    def initialize(self, context: InitCommandContext) -> None:
        """Initialize TRex chassis shell (from API)."""
        self.logger = get_qs_logger(log_group="traffic_shells", log_file_prefix=context.resource.name)
        self.logger.setLevel(logging.DEBUG)
        logging.getLogger("tgn.trex").parent = self.logger

    def cleanup(self) -> None:
        """Cleanup TRex chassis shell (from API)."""
        super().cleanup()

    def get_inventory(self, context: ResourceCommandContext) -> AutoLoadDetails:
        """Load TRex chassis inventory to CloudShell (from API)."""
        self.resource = TrexChassisShell2G.create_from_context(context)
        address = context.resource.address
        user = self.resource.user
        trex = TrexApp(user, address)
        trex.server.connect()

        self._load_chassis(trex.server)
        return self.resource.create_autoload_details()

    def _load_chassis(self, server: TrexServer) -> None:
        """Get chassis resource and attributes."""
        trex_info = server.get_system_info()
        self.resource.model_name = trex_info["core_type"]
        self.resource.vendor = "Cisco TRex"

        self._load_module(0, trex_info)

    def _load_module(self, module_id: int, trex_info: dict) -> None:
        """Get module resource and attributes."""
        gen_module = GenericTrafficGeneratorModule(f"Module{module_id}")
        self.resource.add_sub_resource(f"M{module_id}", gen_module)

        for port_id, port in enumerate(trex_info["ports"]):
            self._load_port(gen_module, port_id, port)

    @staticmethod
    def _load_port(gen_module: GenericTrafficGeneratorModule, port_id: int, port_info: dict) -> None:
        """Get port resource and attributes."""
        gen_port = GenericTrafficGeneratorPort(f"Port{port_id}")
        gen_module.add_sub_resource(f"P{port_id}", gen_port)

        gen_port.max_speed = max(port_info["supp_speeds"])
