# -*- coding: utf-8 -*-
#
# Supplemental class to handle concurrent logins by using the same tokens stored in HashiCorp Vault
#

import hvac
import os
import time

class KsatVault:

    def __init__(self):
        # Authentication
        self.client = hvac.Client(
            url=os.environ['VAULT_ADDR'],
            token=os.environ['VAULT_TOKEN'],
        )

    def get_tokens(self):
        # Reading a secret
        read_response = self.client.secrets.kv.v2.read_secret(
            path='automation_fmc_tokens',
            mount_point='network',
            raise_on_deleted_version=False,
        )

        secrets = read_response['data']['data']
        if not self._is_token_valid(secrets):
            return None

        return secrets

    def update_tokens(self, access_token, refresh_tokens):
        self.client.secrets.kv.v2.patch(
            path='automation_fmc_tokens',
            mount_point='network',
            secret={
                'access_token': access_token,
                'refresh_token': refresh_tokens,
                'token_timestamp': round(time.time() * 1000),
            },
        )

    def _is_token_valid(self, secrets):
        try:
            current_ms = round(time.time() * 1000)
            token_ms = int(secrets.get('token_timestamp', ''))
        except:
            return False

        if (current_ms-token_ms) < (60000 * 30):
            return True
        return False
