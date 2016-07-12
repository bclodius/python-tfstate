# -*- coding: utf-8 -*-

from tfstate.provider.aws.base import AwsResource
from tfstate.provider.aws.aws_eip import AwsEipResource
from tfstate.provider.aws.aws_elb import AwsElbResource
from tfstate.provider.aws.aws_iam_server_certificate import AwsIamServerCertificateResource
from tfstate.provider.aws.aws_internet_gateway import AwsInternetGatewayResource
from tfstate.provider.aws.aws_route_table import AwsRouteTableResource
from tfstate.provider.aws.aws_route_table_association import AwsRouteTableAssociationResource
from tfstate.provider.aws.aws_subnet import AwsSubnetResource
from tfstate.provider.aws.aws_vpc import AwsVpcResource, AwsVpcPeeringConnectionResource
from tfstate.provider.aws.aws_key_pair import AwsKeyPairResource
from tfstate.provider.aws.aws_instance import AwsInstanceResource
from tfstate.provider.aws.aws_security_group import AwsSecurityGroupResource, AwsSecurityGroupRuleResource
from tfstate.provider.aws.aws_nat_gateway import AwsNatGatewayResource
from tfstate.provider.aws.aws_route import AwsRouteResource
from tfstate.provider.aws.aws_eip_association import AwsEipAssociation
