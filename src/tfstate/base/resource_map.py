# -*- coding: utf-8 -*-

# tfstate
from tfstate.provider import aws, openstack, template, other


class ResourceMap(object):
    """
    Class to map the resource names from a tfstate to the Resource classes
    """

    RESOURCE_MAP = {
        'aws_eip_association': aws.AwsEipAssociation,
        'aws_eip': aws.AwsEipResource,
        'aws_elb': aws.AwsElbResource,
        'aws_iam_server_certificate': aws.AwsIamServerCertificateResource,
        'aws_instance': aws.AwsInstanceResource,
        'aws_internet_gateway': aws.AwsInternetGatewayResource,
        'aws_key_pair': aws.AwsKeyPairResource,
        'aws_nat_gateway': aws.AwsNatGatewayResource,
        'aws_route': aws.AwsRouteResource,
        'aws_route_table': aws.AwsRouteTableResource,
        'aws_route_table_association': aws.AwsRouteTableAssociationResource,
        'aws_security_group': aws.AwsSecurityGroupResource,
        'aws_security_group_rule': aws.AwsSecurityGroupRuleResource,
        'aws_subnet': aws.AwsSubnetResource,
        'aws_vpc': aws.AwsVpcResource,
        'aws_vpc_peering_connection': aws.AwsVpcPeeringConnectionResource,
        'openstack_blockstorage_volume_v2': openstack.OSBlockstorageVolumeV2,
        'openstack_compute_floatingip_v2': openstack.OSComputeFloatingIPV2,
        'openstack_compute_instance_v2': openstack.OSComputeInstanceV2,
        'openstack_compute_keypair_v2': openstack.OSComputeKeypairV2,
        'openstack_networking_network_v2': openstack.OSNetworkingNetworkV2,
        'openstack_networking_router_interface_v2': openstack.OSNetworkingRouterInterfaceV2,
        'openstack_networking_secgroup_v2': openstack.OSNetworkingSecgroupV2,
        'openstack_networking_secgroup_rule_v2': openstack.OSNetworkingSecgroupRuleV2,
        'openstack_networking_subnet_v2': openstack.OSNetworkingSubnetV2,
        'data_template_file': template.DataTemplateFileResource,
        'null_resource': other.NullResource,
    }

    @staticmethod
    def get(resource_name):
        """
        Retrieve a class given its tfstate resource name

        :param str resource_name: Resource name to look up
        :raises NotImplementedError: If a resource is not implemented yet
        """
        splitted_name = resource_name.split('.')
        if len(splitted_name) > 0:
            resource_type = splitted_name[0]
            if resource_type == 'data':
                resource_type = '_'.join(splitted_name[:-1])

        resource_class = ResourceMap.RESOURCE_MAP.get(resource_type, None)
        if resource_class is None:
            raise NotImplementedError('Resource {} not implemented yet'.format(resource_name))

        return resource_class
