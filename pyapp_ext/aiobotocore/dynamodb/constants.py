from enum import Enum

__all__ = ("NoDefault", "DataType", "IndexDataTypes", "KeyType", "BillingMode")


class NoDefaultType:
    def __repr__(self):
        return "<NoDefault>"


NoDefault = NoDefaultType()


class DataType(Enum):
    """
    Data types supported by DynamoDB
    """

    Number = "N"
    String = "S"
    Binary = "B"
    Bool = "BOOL"
    List = "L"
    Map = "M"
    NumberSet = "NS"
    StringSet = "SS"
    BinarySet = "BS"


IndexDataTypes = (DataType.Number, DataType.String, DataType.Binary)


class KeyType(Enum):
    """
    Key types supported by DynamoDB
    """

    Hash = "HASH"
    Range = "RANGE"


class BillingMode(Enum):
    """
    Billing mode
    """

    Provisioned = "PROVISIONED"
    PayPerRequest = "PAY_PER_REQUEST"