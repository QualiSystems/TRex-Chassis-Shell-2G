#!/usr/bin/python
# -*- coding: utf-8 -*-

from traffic.trex.chassis.flows.autoload_flow import TRexAutoloadFlow
from cloudshell.traffic.trex.cli.trex_cli_handler import TRexCliHandler


class TRexAutoloadRunner(object):
    def __init__(self, api, cli, resource_config, logger):
        self._cli = cli
        self.resource_config = resource_config
        self.resource_address = resource_config.address
        self.username = resource_config.user
        self.password = api.DecryptPassword(resource_config.password).Value
        self.logger = logger

    @property
    def cli_handler(self):
        """ CLI Handler property """

        return TRexCliHandler(self._cli, self.resource_address, self.username, self.password)

    @property
    def autoload_flow(self):
        return TRexAutoloadFlow(cli_handler=self.cli_handler,
                                resource_config=self.resource_config,
                                logger=self.logger)

    def discover(self):
        return self.autoload_flow.autoload_details()

