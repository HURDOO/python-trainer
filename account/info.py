from typing import Optional

from .models import Account

USER_ID_KEY = 'account_user_id'
USER_SCORE_KEY = 'account_score'


def get_data(session: dict) -> dict:
    user_id = get_user_id(session)
    if user_id is not None:
        return {
            USER_ID_KEY: user_id,
            USER_SCORE_KEY: Account.objects.get(id=user_id).score
        }
    else:
        return {}


def get_user_id(session: dict) -> Optional[int]:
    if USER_ID_KEY in session:
        return session[USER_ID_KEY]
    else:
        return None


def has_permission(user_id: int, perms: list[str]) -> bool:
    account = Account.objects.get(id=user_id)
    return all((perm in account.permissions) for perm in perms)
