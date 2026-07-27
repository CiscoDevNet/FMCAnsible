#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
MATRIX="${ANSIBLE_CORE_MATRIX:-2.17.14 2.18.18 2.19.11 2.20.7 2.21.2}"
WORK_ROOT="${DEPENDENCY_MATRIX_WORK_ROOT:-$(mktemp -d /tmp/fmcansible-deps.XXXXXX)}"
DIST_DIR="${WORK_ROOT}/dist"
COLLECTIONS_PATH="${WORK_ROOT}/collections"

cleanup() {
  if [[ "${KEEP_DEPENDENCY_MATRIX_WORKDIR:-0}" != "1" ]]; then
    rm -rf "${WORK_ROOT}"
  else
    echo "Kept dependency-matrix workdir: ${WORK_ROOT}"
  fi
}
trap cleanup EXIT

export ANSIBLE_LOCAL_TEMP="${ANSIBLE_LOCAL_TEMP:-/tmp/ansible-local}"
export ANSIBLE_REMOTE_TEMP="${ANSIBLE_REMOTE_TEMP:-/tmp/ansible-remote}"
export ANSIBLE_COLLECTIONS_PATH="${COLLECTIONS_PATH}"
export ANSIBLE_COLLECTIONS_PATHS="${COLLECTIONS_PATH}"
mkdir -p "${ANSIBLE_LOCAL_TEMP}" "${ANSIBLE_REMOTE_TEMP}" "${DIST_DIR}" "${COLLECTIONS_PATH}"

echo "Python under test:"
"${PYTHON_BIN}" --version

for version in ${MATRIX}; do
  venv="${WORK_ROOT}/venv-${version}"
  echo
  echo "==> Testing ansible-core ${version}"
  "${PYTHON_BIN}" -m venv "${venv}"
  # shellcheck disable=SC1091
  source "${venv}/bin/activate"
  python -m pip install --upgrade pip wheel
  constraint_file="${WORK_ROOT}/constraints-${version}.txt"
  printf 'ansible-core==%s\n' "${version}" > "${constraint_file}"
  python -m pip install "ansible-core==${version}"
  python -m pip install -r "${ROOT_DIR}/requirements.txt" -c "${constraint_file}"

  rm -f "${DIST_DIR}"/*.tar.gz
  ansible-galaxy collection build "${ROOT_DIR}" --output-path "${DIST_DIR}"
  ansible-galaxy collection install "${DIST_DIR}"/*.tar.gz --force
  ansible-galaxy collection install cisco.nxos --force

  ansible --version
  ansible-galaxy collection list cisco.fmcansible
  ansible-galaxy collection list cisco.nxos
  ansible-galaxy collection list ansible.netcommon
  ansible-galaxy collection list ansible.utils
  deactivate
done
