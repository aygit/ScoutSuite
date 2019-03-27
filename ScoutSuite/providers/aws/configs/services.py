# -*- coding: utf-8 -*-

from ScoutSuite.providers.aws.resources.awslambda.service import Lambdas
from ScoutSuite.providers.aws.resources.cloudwatch.service import CloudWatch
from ScoutSuite.providers.aws.resources.cloudformation.service import CloudFormation
from ScoutSuite.providers.aws.resources.cloudtrail.service import CloudTrail
from ScoutSuite.providers.aws.resources.directconnect.service import DirectConnect
from ScoutSuite.providers.aws.resources.ec2.service import EC2
from ScoutSuite.providers.aws.resources.efs.service import EFS
from ScoutSuite.providers.aws.resources.elasticache.service import ElastiCache
from ScoutSuite.providers.aws.resources.elb.service import ELB
from ScoutSuite.providers.aws.resources.elbv2.service import ELBv2
from ScoutSuite.providers.aws.resources.iam.service import IAM
from ScoutSuite.providers.aws.resources.emr.service import EMR
from ScoutSuite.providers.aws.resources.route53.service import Route53
from ScoutSuite.providers.aws.resources.rds.service import RDS
from ScoutSuite.providers.aws.resources.redshift.service import Redshift
from ScoutSuite.providers.aws.resources.s3.service import S3
from ScoutSuite.providers.aws.resources.vpc.service import VPC
from ScoutSuite.providers.aws.resources.sqs.service import SQS
from ScoutSuite.providers.aws.resources.ses.service import SES
from ScoutSuite.providers.aws.resources.sns.service import SNS
from ScoutSuite.providers.base.configs.services import BaseServicesConfig

try:
    from ScoutSuite.providers.aws.resources.dynamodb.service_private import DynamoDB
    from ScoutSuite.providers.aws.resources.config.service_private import Config
    from ScoutSuite.providers.aws.resources.kms.service_private import KMS
except ImportError:
    DynamoDB = None
    Config = None
    KMS = None


class AWSServicesConfig(BaseServicesConfig):
    """
    Object that holds the necessary AWS configuration for all services in scope.

    :ivar cloudtrail:                   CloudTrail configuration
    :ivar cloudwatch:                   CloudWatch configuration:
    :ivar config:                       Config configuration
    :ivar dynamodb:                     DynomaDB configuration
    :ivar ec2:                          EC2 configuration
    :ivar iam:                          IAM configuration
    :ivar kms:                          KMS configuration
    :ivar rds:                          RDS configuration
    :ivar redshift:                     Redshift configuration
    :ivar s3:                           S3 configuration
    :ivar ses:                          SES configuration: TODO
    "ivar sns:                          SNS configuration
    :ivar sqs:                          SQS configuration
    """

    def __init__(self, credentials=None, thread_config=4, **kwargs):
        super(AWSServicesConfig, self).__init__(credentials, thread_config)

        super(AWSServicesConfig, self).__init__(metadata, thread_config)
        self.cloudwatch = CloudWatch()
        self.cloudformation = CloudFormation()
        self.cloudtrail = CloudTrail()
        self.directconnect = DirectConnect()
        self.ec2 = EC2()
        self.efs = EFS()
        self.elasticache = ElastiCache()
        self.iam = IAM()
        self.elb = ELB()
        self.elbv2 = ELBv2()
        self.emr = EMR()
        self.awslambda = Lambdas()
        self.route53 = Route53()
        self.redshift = Redshift()
        self.s3 = S3()
        self.rds = RDS()
        self.vpc = VPC()
        self.sqs = SQS()
        self.ses = SES()
        self.sns = SNS()

        try:
            self.dynamodb = DynamoDB()
            self.config = Config()
            self.kms = KMS()
        except (NameError, TypeError):
            pass

    def _is_provider(self, provider_name):
        return provider_name == 'aws'
