import hashlib


def get_sha_256_hash(input_value):
    return hashlib.sha256(input_value).hexdigest()


def block_hash_less_than_target(block_hash, given_target):
    return int(block_hash, 16) < int(given_target, 16)

# Initial block data (the transactions' merkle tree root, timestamp, client version, hash of the previous block)
blockData = '0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e20627266e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'.encode()

target = '0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

solution_found = False
block_data_hexadecimal_value = int(blockData, 16)
nonce = 0

while not solution_found:
    block_data_hexadecimal_value = block_data_hexadecimal_value + nonce
    first_hash = get_sha_256_hash(hex(block_data_hexadecimal_value).encode())
    second_hash = get_sha_256_hash(first_hash.encode())

    print('Nonce: ' + str(nonce))

    print('Block hash:')
    print(second_hash)

    print('Target:')
    print(target)

    print('Is the block hash less than the target?')
    solution_found = block_hash_less_than_target(second_hash, target)
    print(solution_found)

    if not solution_found:
        nonce += 1
