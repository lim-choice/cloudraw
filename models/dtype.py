from enum import Enum


class Provider(Enum):
    Ncloud = "NCLOUD"
    AWS = "AWS"
    
class NcloudServiceList(Enum):
    VPC = "vpc"
    Subnet = "subnet"
    ACL = "acl"
    VM = "vm"
    ACG = "acg"
    LB = "lb"
    MySQL = "mysql"
    MSSQL = "mssql"
    PostgreSQL = "postgres"
    Redis = "redis"
    MongoDB = "mongo"
