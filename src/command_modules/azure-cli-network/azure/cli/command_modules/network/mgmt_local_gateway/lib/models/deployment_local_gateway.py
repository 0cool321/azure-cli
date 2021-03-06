# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
#pylint: skip-file

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentLocalGateway(Model):
    """Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateLocalGateway_2016-11-28/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :param asn: Autonomous System Number to use for the BGP settings.
    :type asn: str
    :param bgp_peering_address: IP address from the OnPremise VPN's subnet to
     use for BGP peering.
    :type bgp_peering_address: str
    :param gateway_ip_address: Gateway's Public IP address.  (e.g. 10.1.1.1)
    :type gateway_ip_address: str
    :param local_address_prefix: List of CIDR block prefixes representing the
     address space of the OnPremise VPN's subnet.
    :type local_address_prefix: list of object
    :param local_network_gateway_name: Gateway name.
    :type local_network_gateway_name: str
    :param peer_weight: Weight added to routes learned through BGP peering.
    :type peer_weight: str
    :param tags: Tags object.
    :type tags: object
    :param use_bgp_settings: Flag to enable BGP settings. Default value:
     False .
    :type use_bgp_settings: bool
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        'gateway_ip_address': {'required': True},
        'local_network_gateway_name': {'required': True},
        'use_bgp_settings': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        'asn': {'key': 'properties.parameters.asn.value', 'type': 'str'},
        'bgp_peering_address': {'key': 'properties.parameters.bgpPeeringAddress.value', 'type': 'str'},
        'gateway_ip_address': {'key': 'properties.parameters.gatewayIpAddress.value', 'type': 'str'},
        'local_address_prefix': {'key': 'properties.parameters.localAddressPrefix.value', 'type': '[object]'},
        'local_network_gateway_name': {'key': 'properties.parameters.localNetworkGatewayName.value', 'type': 'str'},
        'peer_weight': {'key': 'properties.parameters.peerWeight.value', 'type': 'str'},
        'tags': {'key': 'properties.parameters.tags.value', 'type': 'object'},
        'use_bgp_settings': {'key': 'properties.parameters.useBgpSettings.value', 'type': 'bool'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateLocalGateway_2016-11-28/azuredeploy.json"

    mode = "Incremental"

    def __init__(self, gateway_ip_address, local_network_gateway_name, content_version=None, asn=None, bgp_peering_address=None, local_address_prefix=None, peer_weight=None, tags=None, use_bgp_settings=False):
        self.content_version = content_version
        self.asn = asn
        self.bgp_peering_address = bgp_peering_address
        self.gateway_ip_address = gateway_ip_address
        self.local_address_prefix = local_address_prefix
        self.local_network_gateway_name = local_network_gateway_name
        self.peer_weight = peer_weight
        self.tags = tags
        self.use_bgp_settings = use_bgp_settings
