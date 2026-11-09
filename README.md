# Parameter-Efficient Adaptation of Protein Language Models via Low-Rank Experts

Official implementation for the paper "Parameter-Efficient Adaptation of
Protein Language Models via Low-Rank Experts", accepted at EACL 2026.

## Overview

The repository implements a mixture of low-rank experts that adapts a frozen
protein language model to new assay families.  Both the expert-routing layer
and the lightweight training pipeline are included.

## Repository Structure

```
├── src/
│   ├── model.py        # Backbone wrapper with expert routing
│   ├── lora.py         # Low-rank expert layers
│   ├── train.py        # Training and evaluation entry point
│   └── utils.py        # Assay data helpers
├── data/
│   └── README.md       # Assay splits description
├── experiments/
│   └── eacl_config.yaml
├── results/
│   └── README.md
├── tests/
│   └── test_lora.py
├── requirements.txt
└── .gitignore
```

## Quick Start

```bash
git clone https://github.com/wholetherapi/emails_github_1643_m2v7c1_protein-lora-experts.git
cd protein-lora-experts
pip install -r requirements.txt
python src/train.py --config experiments/eacl_config.yaml
```

## Citation

```bibtex
@inproceedings{carter2026protein,
  title={Parameter-Efficient Adaptation of Protein Language Models via Low-Rank Experts},
  author={Carter, Patrick and others},
  booktitle={Proceedings of EACL 2026},
  year={2026}
}
```
