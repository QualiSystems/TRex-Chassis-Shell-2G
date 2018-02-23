#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.autoload.autoload_builder import AutoloadDetailsBuilder

from traffic.trex.chassis.autoload import models
from traffic.trex.chassis.actions.trex_autoload_actions import TRexAutoloadActions


class TRexAutoloadFlow(object):
    def __init__(self, cli_handler, resource_config, logger):
        """  """

        self._resource_config = resource_config
        self._cli_handler = cli_handler
        self._logger = logger

    def autoload_details(self):
        """  """

        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            autoload_actions = TRexAutoloadActions(enable_session)

            resource = models.Chassis(shell_name=self._resource_config.shell_name,
                                      name=self._resource_config.name,
                                      unique_id=self._resource_config.fullname)

            ports = autoload_actions.get_trex_ports(self._resource_config.trex_server_path)

            for id, port in enumerate(ports):
                port_res = models.Port(shell_name=self._resource_config.shell_name,
                                       name="Port {id}".format(id=id),
                                       unique_id="{res_name}.{port_uid}".format(res_name=self._resource_config.name,
                                                                                port_uid=port))

                resource.add_sub_resource(id, port_res)

            return AutoloadDetailsBuilder(resource).autoload_details()
