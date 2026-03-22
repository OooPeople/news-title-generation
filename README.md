# News Title Generation with mT5
# 使用 mT5 的新聞標題生成

This repository is a cleaned-up public version of an Applied Deep Learning homework project. It fine-tunes `google/mt5-small` to generate a Chinese news headline from the corresponding news article body.

<!-- bilingual split -->

這個 repository 是 `Applied Deep Learning` 作業的公開整理版，核心任務是微調 `google/mt5-small`，讓模型根據中文新聞內文生成對應標題。

## Overview / 專案概述

The original coursework focused on training, checkpoint-based prediction, and ROUGE evaluation. This public version keeps the runnable code, reorganizes the project structure, includes lightweight sample data, and documents the workflow in a cleaner portfolio format.

<!-- bilingual split -->

原始作業版本主要面向訓練、checkpoint 推論與 ROUGE 評估。公開版保留可執行的核心程式，重新整理專案結構，提供輕量 sample data，並以較適合公開展示的方式補齊說明文件。

## Task Example / 任務範例

Input schema:

```json
{
  "id": "21710",
  "date_publish": "2021-01-14 00:00:00",
  "source_domain": "udn.com",
  "maintext": "<news article body>",
  "title": "<news headline>"
}
```

The model reads `maintext` and generates `title`.

<!-- bilingual split -->

模型讀入 `maintext`，輸出對應的 `title`。

## Key Features / 主要特點

- Fine-tuning and inference pipeline for Chinese news title generation with `google/mt5-small`
- Custom `SummarizationTrainer` for generation-oriented evaluation and prediction output writing
- Built-in ROUGE evaluation using the bundled `tw_rouge` package
- Checkpoint download script for the released homework model weights
- Lightweight sample data for demonstrating the expected JSONL schema

<!-- bilingual split -->

- 使用 `google/mt5-small` 進行中文新聞標題生成的訓練與推論流程
- 針對生成式評估與輸出寫檔需求調整的 `SummarizationTrainer`
- 內含 `tw_rouge`，可直接進行 ROUGE 評估
- 提供已公開的作業 checkpoint 下載腳本
- 附上輕量 sample data，用來展示 JSONL 格式與使用方式

## Tech Stack / 技術棧

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- NLTK
- `tw_rouge`

## Repository Structure / 專案結構

```text
news-title-generation/
|-- src/
|   |-- eval.py
|   |-- run_mt5.py
|   `-- trainer_mt5.py
|-- scripts/
|   |-- download_checkpoint.sh
|   `-- run_inference.sh
|-- sample_data/
|   |-- README.md
|   |-- public_sample.jsonl
|   |-- sample_submission.jsonl
|   |-- sample_test.jsonl
|   `-- train_sample.jsonl
|-- tw_rouge/
|   |-- LICENSE
|   |-- README.md
|   |-- setup.py
|   `-- tw_rouge/
|       |-- __init__.py
|       `-- twrouge.py
|-- README.md
|-- THIRD_PARTY_NOTICES.md
|-- requirements.txt
`-- .gitignore
```

## Setup / 環境準備

### Prerequisites / 先備條件

- Python 3.8 or later
- A working PyTorch installation compatible with your hardware
- Git Bash, WSL, or another shell environment if you want to run the `.sh` scripts on Windows
- `wget` and `unzip` are required for the checkpoint download script

<!-- bilingual split -->

- Python 3.8 以上版本
- 與硬體相容的 PyTorch 環境
- 如果在 Windows 執行 `.sh` 腳本，建議使用 Git Bash、WSL 或其他 shell 環境
- `download_checkpoint.sh` 需要 `wget` 與 `unzip`

### Installation / 安裝方式

```bash
pip install -r requirements.txt
pip install -e tw_rouge
```

## Usage / 使用方式

### Download the Released Checkpoint / 下載公開的模型權重

```bash
bash scripts/download_checkpoint.sh
```

This downloads and extracts the released `mt5-small` checkpoint under the repository root.

<!-- bilingual split -->

這會將公開的 `mt5-small` checkpoint 下載並解壓縮到 repository 根目錄。

### Run Inference / 執行推論

```bash
bash scripts/run_inference.sh sample_data/sample_test.jsonl prediction.jsonl
```

The script expects a JSONL file with the same schema as the coursework data and writes a prediction JSONL file containing `id` and generated `title`.

For this public demo, `sample_test.jsonl` is aligned with `public_sample.jsonl`: they contain the same three article ids, while `sample_test.jsonl` simply omits the ground-truth `title` field.

<!-- bilingual split -->

此腳本預期輸入為與作業資料格式相容的 JSONL 檔案，並輸出包含 `id` 與模型生成 `title` 的 prediction JSONL 檔。

在這份公開版 demo 中，`sample_test.jsonl` 與 `public_sample.jsonl` 使用相同的三筆文章 id；差別只在於 `sample_test.jsonl` 移除了標準答案 `title` 欄位，方便直接接上推論與評估流程。

### Evaluate Predictions / 評估預測結果

```bash
python src/eval.py -r sample_data/public_sample.jsonl -s prediction.jsonl
```

### Training Entry Point / 訓練入口

```bash
python src/run_mt5.py --help
```

An example training configuration from the coursework setup used:

```bash
python src/run_mt5.py \
  --do_train \
  --do_eval \
  --model_name_or_path google/mt5-small \
  --train_file data/train.jsonl \
  --validation_file data/public.jsonl \
  --output_dir mt5-small \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 4 \
  --per_device_eval_batch_size 4 \
  --eval_accumulation_steps 4 \
  --predict_with_generate \
  --text_column maintext \
  --summary_column title \
  --adafactor \
  --learning_rate 1e-3 \
  --warmup_ratio 0.1
```

The full training dataset is not included in this public repository; the command above is documented for reproducibility and reference only.

<!-- bilingual split -->

完整訓練資料不包含在此公開版本中；以上指令主要作為流程說明與重現參考。

## Method / 方法說明

The project uses a sequence-to-sequence formulation:

1. Tokenize the news article body from `maintext`
2. Fine-tune `google/mt5-small` on paired `maintext -> title` examples
3. Generate headlines with beam search during inference
4. Evaluate generated titles with ROUGE on held-out data

<!-- bilingual split -->

本專案採用 sequence-to-sequence 設定：

1. 將新聞內文 `maintext` tokenization
2. 使用成對的 `maintext -> title` 資料微調 `google/mt5-small`
3. 推論時以 beam search 生成標題
4. 在驗證資料上以 ROUGE 評估生成品質

## Results / 實驗結果

Observed coursework results from the preserved experiment outputs:

- Training samples: `21710`
- Validation samples: `5494`
- Training epochs: `3`
- Validation ROUGE-1/2/L F1: `0.2467 / 0.0915 / 0.2224`
- Beam-5 prediction ROUGE-1/2/L F1: `0.2618 / 0.1061 / 0.2360`

<!-- bilingual split -->

保留下來的作業實驗結果如下：

- 訓練樣本數：`21710`
- 驗證樣本數：`5494`
- 訓練 epoch：`3`
- 驗證 ROUGE-1/2/L F1：`0.2467 / 0.0915 / 0.2224`
- Beam-5 推論 ROUGE-1/2/L F1：`0.2618 / 0.1061 / 0.2360`

## Dataset / 資料集說明

- The original coursework dataset consists of Chinese news articles with associated headlines
- This public repository includes only tiny schema examples under `sample_data/`
- The full training and validation files are intentionally not bundled here
- Expected columns include `id`, `date_publish`, `source_domain`, `maintext`, and optionally `title`

<!-- bilingual split -->

- 原始作業資料為中文新聞內文與對應標題
- 此公開版本只在 `sample_data/` 中保留極小量格式範例
- 完整訓練與驗證資料不隨 repo 提供
- 預期欄位包含 `id`、`date_publish`、`source_domain`、`maintext`，以及可選的 `title`

## Limitations / 限制說明

- The exact coursework environment was not fully pinned
- Full datasets are not included in this public repository
- The released checkpoint is downloaded separately rather than committed directly
- Core training code is adapted from official examples and extended for coursework use

<!-- bilingual split -->

- 原始作業環境並未完整鎖定版本
- 完整資料集不包含在公開版本中
- 公開的 checkpoint 透過外部下載，不直接放入 repo
- 核心訓練程式是基於官方範例修改並延伸，而非完全從零實作

## Course Context / 課程背景

This repository was adapted from a homework submission for the course `Applied Deep Learning`. The public version keeps the runnable implementation, removes coursework-only artifacts, and reorganizes the codebase for easier public review.

<!-- bilingual split -->

本 repository 改寫自 `Applied Deep Learning` 課程作業繳交版本。公開版保留可執行的核心實作，移除僅供交作業使用的中間產物，並重新整理結構，使其更適合公開展示與檢閱。

## Author / 作者

Student coursework adapted into a public project repository by the original project author.

<!-- bilingual split -->

由原作者將課程作業整理為公開展示版本。
