# DSAINet Demo Materials Guide

This folder contains the prepared demo assets for the DSAINet competition submission, mainly covering item 5 and item 6 in the material checklist:

- item 5: representative demo trials with EEG waveforms, true labels, prediction probabilities, and saliency/topomap visualizations
- item 6: forward-pass module names, tensor shapes, and short explanations for animation or slide illustration

All exported demo trials were selected with one rule: every label in every dataset must have correctly predicted examples. The current export contains 3 correctly predicted trials per label.

## Quick Summary

Root folder:

```bash
/home/mazhiyuan/QZH/competition_materials/dsainet_demo
```

Source code used to generate these materials:

```bash
/home/mazhiyuan/QZH/archived_src/DSAINet_copy/scripts/export_competition_demo_materials.py
```

Current scale:

- 10 datasets
- 78 demo trials
- 3 trials per label
- 78 waveform figures
- 78 prediction probability figures
- 78 saliency/topomap figures
- 78 `.npz` sample packages
- 10 forward-pass shape files

Datasets included:

```text
BCIC_IV_2a, BCIC_IV_2b, OpenBMI, EEGMat, PhysioNet_MI,
ADFTD, Mumtaz2016, Rockhill2021, Shin2018, Zhou2016
```

## Folder Structure

```text
dsainet_demo/
  manifest.json
  demo_trials_manifest.csv
  figures/
    waveforms/<dataset>/*.png
    probabilities/<dataset>/*.png
    saliency/<dataset>/*.png
  samples_npz/<dataset>/*.npz
  forward_pass/*_forward_shapes.csv
  forward_pass/*_forward_steps.json
  label_coverage/*_label_coverage.csv
```

### Important Files

`manifest.json`

Overall summary of the export. It records the included datasets, trial count, and key subfolders.

`demo_trials_manifest.csv`

Main index table. Use this first when selecting demo examples. Each row is one exported trial.

Important columns:

- `dataset`: dataset name
- `class_name`: true label name
- `predicted_name`: predicted label name
- `is_correct`: whether prediction is correct; current export is all `1`
- `confidence`: model confidence for the predicted class
- `waveform_png`: EEG waveform figure path
- `probability_png`: prediction probability bar chart path
- `saliency_png`: saliency/topomap figure path
- `npz`: raw exported sample package path

`label_coverage/*.csv`

Per-dataset label coverage check. `correct_available` means how many correctly predicted candidate trials were available before choosing the final 3 examples. `exported_trials` should be 3 for every label.

## How To Use For Item 5

For each demo trial, use the three linked figures together:

1. `figures/waveforms/<dataset>/...png`
   - Shows the representative EEG waveform for the trial.
   - Usually only the first several channels are plotted to keep it readable.

2. `figures/probabilities/<dataset>/...png`
   - Shows softmax probabilities for all classes.
   - Green bar means the predicted class is also the true class.
   - If a future export includes mistakes, orange marks the true class and red marks the predicted class.

3. `figures/saliency/<dataset>/...png`
   - Shows gradient-based channel saliency.
   - If channel locations are known, it is drawn as a topomap.
   - If channel locations are unavailable, it falls back to a channel-importance bar chart.

Recommended presentation pattern:

```text
EEG waveform -> prediction probabilities -> saliency/topomap
```

This tells a complete story: input signal, model decision, and what channels influenced the decision.

## How To Use For Item 6

Use the files under:

```bash
forward_pass/
```

Each dataset has two files:

- `<dataset>_forward_shapes.csv`
- `<dataset>_forward_steps.json`

The CSV is easier for slides. The JSON is easier for making an animation or web demo.

Key forward-pass stages:

```text
raw EEG input
-> patch embedding
-> projection
-> positional encoding
-> coarse temporal branch
-> fine temporal branch
-> intra-branch self-attention
-> cross-branch attention
-> token attention pooling
-> classifier
-> softmax probabilities
```

For example, in BCIC_IV_2a the model uses input shape similar to:

```text
(B, 1, 22, 1000)
```

and outputs class logits/probabilities:

```text
(B, 4)
```

Use the exact per-dataset shapes from the CSV/JSON files rather than hardcoding one shape for all datasets, because channel count and class count differ by dataset.

## What Is Inside The `.npz` Files

Each file under `samples_npz/<dataset>/` contains one exported trial. It includes:

- `eeg`: EEG sample array, usually shaped `(channels, time)`
- `true_label`: integer true label
- `predicted_label`: integer predicted label
- `probabilities`: model softmax probabilities
- `saliency`: channel saliency vector
- `channel_names`: channel names when available

These are useful if someone wants to rebuild figures, make a web demo, or inspect raw values.

## Quality Check Already Done

The final export was checked with the following criteria:

- every dataset is present in `manifest.json`
- every label has 3 exported trials
- every exported trial has `is_correct = 1`
- every exported trial has a waveform figure, probability figure, saliency/topomap figure, and `.npz` package
- every dataset has forward-pass shape files

Final count:

```text
78 trials = 78 waveforms + 78 probability charts + 78 saliency/topomap figures + 78 npz files
```

## Notes For Teammates

- Use `demo_trials_manifest.csv` as the main entry point. Do not manually guess matching image filenames.
- For slides, choose one row from the CSV and place its three figures side by side.
- For the website/demo page, read the CSV and render the three paths in each row.
- The labels are already human-readable in `class_name` and `predicted_name`.
- Some preprocessing warnings appeared during export, but the final validation passed and all exported examples are correctly predicted.

## Regenerating Materials

Run this only if the source code or desired number of trials changes:

```bash
cd /home/mazhiyuan/QZH/archived_src/DSAINet_copy
PYTHONUNBUFFERED=1 /home/mazhiyuan/anaconda3/envs/mzy/bin/python3 \
  scripts/export_competition_demo_materials.py \
  --datasets all \
  --trials-per-class 3 \
  --output /home/mazhiyuan/QZH/competition_materials/dsainet_demo \
  --device 0 \
  --batch-size 256
```

By default, the script will fail if any label has no correctly predicted trial. This is intentional, because the demo requirement is that every label must have at least one correct example.
