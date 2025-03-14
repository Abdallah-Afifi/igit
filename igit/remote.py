import os

from . import data
from . import base

REMOTE_REFS_BASE = 'refs/heads'
LOCAL_REFS_BASE = 'refs/remotes'

def fetch(remote_path):
    # get refs from remote
    refs = _get_remote_refs(remote_path, REMOTE_REFS_BASE)

    # fetch missing objects
    for oid in base.iter_objects_in_commits(refs.values()):
        data.fetch_object_if_missing(oid, remote_path)

    # update local refs
    for remote_name, value in refs.items():
        refname = os.path.relpath(remote_name, REMOTE_REFS_BASE)
        data.update_ref(f'{LOCAL_REFS_BASE}/{refname}', data.RefValue(symbolic=False, value=value))

def _get_remote_refs(remote_path, prefix=''):
    with data.change_git_dir(remote_path):
        return {refname: ref.value for refname, ref in data.iter_refs(prefix)}
