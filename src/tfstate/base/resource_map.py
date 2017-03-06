# -*- coding: utf-8 -*-

# tfstate
from tfstate.provider import aws, openstack, template, other


class ResourceMap(object):
    """
    Class to map the resource names from a tfstate to the Resource classes
    """

    RESOURCE_MAP = {
        'archive_file': other.ArchiveFileResource,
        'aws_autoscaling_group': aws.AwsAutoScalingGroupResource,
        'aws_autoscaling_policy': aws.AwsAutoScalingPolicyResource,
        'aws_cloudwatch_metric_alarm': aws.AwsCloudWatchMetricAlarmResource,
        'aws_eip_association': aws.AwsEipAssociation,
        'aws_eip': aws.AwsEipResource,
        'aws_elasticache_replication_group': aws.AwsElasticCacheReplicationGroupResource,
        'aws_elasticache_subnet_group': aws.AwsElasticCacheSubnetGroupResource,
        'aws_elb': aws.AwsElbResource,
        'aws_iam_server_certificate': aws.AwsIamServerCertificateResource,
        'aws_instance': aws.AwsInstanceResource,
        'aws_internet_gateway': aws.AwsInternetGatewayResource,
        'aws_lambda_function': aws.AwsLambdaFunctionResource,
        'aws_lambda_permission': aws.AwsLambdaPermissionResource,
        'aws_launch_configuration': aws.AwsLaunchConfigurationResource,
        'aws_lb_ssl_negotiation_policy': aws.AwsLBSSLNegotiationPolicyResource,
        'aws_key_pair': aws.AwsKeyPairResource,
        'aws_nat_gateway': aws.AwsNatGatewayResource,
        'aws_proxy_protocol_policy': aws.AwsProxyProtocolPolicyResource,
        'aws_route53_record': aws.AwsRoute53RecordResource,
        'aws_route': aws.AwsRouteResource,
        'aws_route_table': aws.AwsRouteTableResource,
        'aws_route_table_association': aws.AwsRouteTableAssociationResource,
        'aws_security_group': aws.AwsSecurityGroupResource,
        'aws_security_group_rule': aws.AwsSecurityGroupRuleResource,
        'aws_sns_topic': aws.AwsSnsTopicResource,
        'aws_sns_topic_subscription': aws.AwsSnsTopicSubscriptionResource,
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
        'data_aws_ami': aws.DataAwsAmiResource,
        'data_aws_caller_identity': aws.DataAwsCallerIdentityResource,
        'data_template_file': template.DataTemplateFileResource,
        'null_resource': other.NullResource,
        'data_null_data_source': other.NullDataSource,
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
