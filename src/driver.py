#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.core.context.error_handling_context import ErrorHandlingContext
from cloudshell.devices.driver_helper import get_logger_with_thread_id, get_cli, get_api
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface

from traffic.trex.chassis.configuration_attributes_structure import TrafficGeneratorChassisResource
from traffic.trex.chassis.runners.autoload_runner import TRexAutoloadRunner


class TRexChassisDriver(ResourceDriverInterface):
    SHELL_NAME = "Traffic TRex 2G"

    def initialize(self, context):
        """

        :type context: cloudshell.shell.core.driver_context.InitCommandContext
        """
        pass

    def cleanup(self):
        pass

    def get_inventory(self, context):
        """ Return device structure with all standard attributes

        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        :rtype: cloudshell.shell.core.driver_context.AutoLoadDetails
        """

        logger = get_logger_with_thread_id(context)
        logger.info("Autoload started")

        with ErrorHandlingContext(logger):
            resource_config = TrafficGeneratorChassisResource.from_context(context=context,
                                                                           shell_name=self.SHELL_NAME)

            session_pool_size = int(resource_config.sessions_concurrency_limit)
            self._cli = get_cli(session_pool_size)
            api = get_api(context)

            autoload_runner = TRexAutoloadRunner(api=api,
                                                 cli=self._cli,
                                                 resource_config=resource_config,
                                                 logger=logger)

            response = autoload_runner.discover()
            logger.info("Autoload completed")

            return response
