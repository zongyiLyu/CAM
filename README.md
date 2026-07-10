## CAM: A Causality-Based Analysis Framework For Multi-Agent Code Generation Systems

**This Repo is modified based on source code of [MetaGPT](https://github.com/FoundationAgents/MetaGPT).**

### Prerequisites

Run` pip install -r ./Code/requirement.txt `  to prepare the environment for MetaGPT.

### Source code

Source code and experiment result for our causal analysis can be found in `./Code`

The source code of running the original dataset is in ` ./Code/metagpt/software_causal_basedataset.py`

The source code for intervention is in ` ./Code/metagpt/intervene_internal_output.py`

The source code of causal analysis is in ` ./Code/metagpt/software_causal_modified.py`

The script of running these code is in `./Code/scripts`

### Reproduction

For reproduction, first run `bash ./Code/scripts/{Dataset}/{Model}/test_cause_basedataset.sh` to generate original result for different settings.


After generating the result for original dataset, run `python ./Code/metagpt/intervene_internal_output.py` to generate intervention for the internal output.

Run `bash ./Code/scripts/{Dataset}/{Model}/test_cause_len_all_new_modified.sh` for causal analysis.

### More Experiment Result

The full results of LLM analysis (Sec. 3) can be found in `./Supplementary_results/LLM-results`

The full results of pilot study (Sec. 6) can be found in `./Supplementary_results/Pilot_study`

Detail explanation for all features can be found in  `./Supplementary_results/Features`

The full results of failure repair (Sec. 8) can be found in `./Supplementary_results/Failure_repair`

The full results of Self-Collaboration Code Generation (Sec. 9) can be found in `./Supplementary_results/Self-Collab-results`



