# Sample Data
# 範例資料

This directory contains tiny JSONL examples derived from the coursework data format. The three evaluation-related files are intentionally aligned so the public demo workflow can run end to end.

<!-- bilingual split -->

這個資料夾收錄了依照作業資料格式整理出的精簡 JSONL 範例。為了讓公開版 demo 可以直接跑通，和評估有關的三個 sample 檔案已刻意對齊成同一組 id。

Included files:

- `train_sample.jsonl`: small sample with `maintext` and `title`
- `public_sample.jsonl`: small reference set with ground-truth titles for the three demo articles
- `sample_test.jsonl`: the same three demo articles with the `title` field removed for inference
- `sample_submission.jsonl`: example prediction output format aligned with `public_sample.jsonl`

<!-- bilingual split -->

包含檔案如下：

- `train_sample.jsonl`：包含 `maintext` 與 `title` 的小型訓練範例
- `public_sample.jsonl`：三筆 demo 文章的參考答案資料，可直接拿來做評估
- `sample_test.jsonl`：與 `public_sample.jsonl` 相同的三筆文章，但移除了 `title` 欄位，用於推論示範
- `sample_submission.jsonl`：與 `public_sample.jsonl` 對齊的預測輸出格式範例
