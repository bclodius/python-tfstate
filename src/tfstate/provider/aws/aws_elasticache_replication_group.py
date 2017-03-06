# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsElasticCacheReplicationGroupResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsElasticCacheReplicationGroupResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_elasticache_replication_group":
            raise InvalidResource("AwsElasticCacheReplicationGroupResource must be of 'aws_elasticache_replication_group' type")
        attributes = self.primary_data['attributes']
        self.auto_minor_version_upgrade = attributes.get('auto_minor_version_upgrade', None)
        self.automatic_failover_enabled = attributes.get('automatic_failover_enabled', None)
        self.engine = attributes.get('engine', None)
        self.engine_version = attributes.get('engine_version', None)
        self.id = attributes.get('id', None)
        self.maintenance_window = attributes.get('maintenance_window', None)
        self.node_type = attributes.get('node_type', None)
        self.number_cache_clusters = attributes.get('number_cache_clusters', None)
        self.parameter_group_name = attributes.get('parameter_group_name', None)
        self.port = attributes.get('port', None)
        self.primary_endpoint_address = attributes.get('primary_endpoint_address', None)
        self.replication_group_description = attributes.get('replication_group_description', None)
        self.replication_group_id = attributes.get('replication_group_id', None)
        self.security_group_ids = self.compound_attributes.get('security_group_ids', {})
        self.snapshot_retention_limit = attributes.get('snapshot_retention_limit', None)
        self.snapshot_window = attributes.get('snapshot_window', None)
        self.tags = self.compound_attributes.get('tags', {})
