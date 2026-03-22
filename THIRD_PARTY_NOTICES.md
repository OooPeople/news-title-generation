# Third-Party Notices

This repository includes files adapted from Hugging Face example training scripts and a bundled third-party ROUGE package.

Affected files include:

- `src/run_mt5.py`
- `src/trainer_mt5.py`
- `src/eval.py`
- `tw_rouge/setup.py`
- `tw_rouge/tw_rouge/__init__.py`
- `tw_rouge/tw_rouge/twrouge.py`

Notes:

- `src/run_mt5.py` is adapted from Hugging Face official sequence-to-sequence example workflows.
- `src/trainer_mt5.py` extends the Hugging Face `Trainer` pattern for coursework-specific generation and post-processing behavior.
- The custom trainer modifications follow practical community-style `Trainer` extension patterns and were not built fully from scratch.
- `tw_rouge/` is included as a third-party dependency. Review the original files under that directory for its license and package notice.
- Original license headers preserved in adapted source files should be reviewed directly for the applicable notice terms.
