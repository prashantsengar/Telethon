from dataclasses import dataclass
from hashlib import sha1
from typing import Self


@dataclass
class AuthKey:
    data: bytes
    aux_hash: bytes
    key_id: bytes

    @classmethod
    def from_bytes(cls, data: bytes) -> Self:
        sha = sha1(data).digest()
        aux_hash = sha[:8]
        key_id = sha[12:]
        return cls(data=data, aux_hash=aux_hash, key_id=key_id)

    def __bytes__(self) -> bytes:
        return self.data

    def calc_new_nonce_hash(self, new_nonce: bytes, number: int) -> bytes:
        return sha1(new_nonce + bytes((number,)) + self.aux_hash).digest()[4:]