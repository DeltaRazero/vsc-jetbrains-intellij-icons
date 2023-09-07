
class __:

    import string
    import secrets

# *****************************************************************************

_generated_uids: dict[int, list[str]] = {}

def generate_uid(n: int) -> str:
    """Helper function to make short random font IDs."""

    uid = ''.join(
        __.secrets.choice(
            __.string.ascii_letters + __.string.digits
        )
        for _ in range(n)
    )

    if (n not in _generated_uids):
        _generated_uids[n] = []

    if (uid in _generated_uids[n]):
        uid = generate_uid(n)
    _generated_uids[n].append(uid)

    return uid
