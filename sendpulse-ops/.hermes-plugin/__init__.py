"""Auto-generated Hermes plugin for "sendpulse-ops".

Registers every bundled skill with Hermes' native skill loader via ctx.register_skill.
Docs: https://hermes-agent.nousresearch.com/docs/developer-guide/plugins
"""
import os
from pathlib import Path


def _skills_dir():
    """Locate the skills/ tree for either supported install layout.

    - git-clone install (`hermes plugins install <org>/<repo>`): the plugin dir is the
      repo root, so .hermes-plugin/ and skills/ are siblings here — resolves ../skills.
    - flattened install (this module's own directory copied to the plugin dir root):
      skills/ sits next to this module — resolves ./skills.

    Returns None when neither candidate exists (e.g. a plugin with no skills at all);
    callers must treat that as "nothing to register", not an error.
    """
    here = os.path.dirname(os.path.realpath(__file__))
    candidates = (
        os.path.realpath(os.path.join(here, "..", "skills")),
        os.path.realpath(os.path.join(here, "skills")),
    )
    for cand in candidates:
        if os.path.isdir(cand):
            return cand
    return None


def register(ctx):
    skills_dir = _skills_dir()
    if not skills_dir:
        return
    for name in sorted(os.listdir(skills_dir)):
        skill_md = os.path.join(skills_dir, name, "SKILL.md")
        if os.path.isfile(skill_md):
            # register_skill requires a pathlib.Path — a str raises AttributeError and
            # silently disables the whole plugin (verified against the ground truth
            # superpowers plugin's own __init__.py).
            ctx.register_skill(name, Path(skill_md))
