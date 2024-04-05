from enum import Enum

__all__ = [
    "EncryptionMode",
    "EncryptionDirection",
]


class EncryptionMode(str, Enum):
    ECB = "ECB"
    CBC = "CBC"


class EncryptionDirection(str, Enum):
    ENCRYPT = "Encrypt"
    DECRYPT = "Decrypt"
