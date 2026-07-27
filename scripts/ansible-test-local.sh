#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAMESPACE="${NAMESPACE:-cisco}"
COLLECTION_NAME="${COLLECTION_NAME:-fmcansible}"
WORK_ROOT="${ANSIBLE_TEST_WORK_ROOT:-$(mktemp -d /tmp/fmcansible-ansible-test.XXXXXX)}"
COLLECTION_DIR="${WORK_ROOT}/ansible_collections/${NAMESPACE}/${COLLECTION_NAME}"

cleanup() {
  if [[ "${KEEP_ANSIBLE_TEST_WORKDIR:-0}" != "1" ]]; then
    rm -rf "${WORK_ROOT}"
  else
    echo "Kept ansible-test workdir: ${WORK_ROOT}"
  fi
}
trap cleanup EXIT

mkdir -p "${COLLECTION_DIR}"
rsync -a --delete \
  --exclude '.git/' \
  --exclude '.ansible/' \
  --exclude '.cache/' \
  --exclude '.pytest_cache/' \
  --exclude 'ansible_collections/' \
  --exclude '__pycache__/' \
  --exclude '.DS_Store' \
  --exclude '*.bk' \
  --exclude 'inventory.ini' \
  --exclude 'logs' \
  --exclude 'unittest.sh' \
  "${ROOT_DIR}/" "${COLLECTION_DIR}/"

export ANSIBLE_LOCAL_TEMP="${ANSIBLE_LOCAL_TEMP:-/tmp/ansible-local}"
export ANSIBLE_REMOTE_TEMP="${ANSIBLE_REMOTE_TEMP:-/tmp/ansible-remote}"
export ANSIBLE_COLLECTIONS_PATH="${WORK_ROOT}:${ANSIBLE_COLLECTIONS_PATH:-}"

mkdir -p "${ANSIBLE_LOCAL_TEMP}" "${ANSIBLE_REMOTE_TEMP}"

cd "${COLLECTION_DIR}"
exec ansible-test "$@"
