# DSAINet Demo 材料说明

这个目录存放本次比赛 DSAINet demo 所需的可视化材料，主要对应材料清单里的第 5 条和第 6 条：

- 第 5 条：Demo 用代表性样本，包括 EEG 波形、真实标签、预测概率、saliency/topomap
- 第 6 条：Forward pass 动画所需的模块名称、tensor shape 和简短解释

本次导出的 demo 样本遵循一个筛选规则：每个数据集的每一个 label，都至少要有预测正确的 trial。当前版本是每个 label 导出 3 个预测正确的 trial。

## 快速概览

材料根目录：

```bash
/home/mazhiyuan/QZH/competition_materials/dsainet_demo
```

生成脚本位置：

```bash
/home/mazhiyuan/QZH/archived_src/DSAINet_copy/scripts/export_competition_demo_materials.py
```

当前材料规模：

- 10 个数据集
- 78 个 demo trial
- 每个 label 3 个 trial
- 78 张 EEG 波形图
- 78 张预测概率柱状图
- 78 张 saliency/topomap 图
- 78 个 `.npz` 样本包
- 10 份 forward pass shape 文件

包含的数据集：

```text
BCIC_IV_2a, BCIC_IV_2b, OpenBMI, EEGMat, PhysioNet_MI,
ADFTD, Mumtaz2016, Rockhill2021, Shin2018, Zhou2016
```

## 目录结构

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

## 重要文件说明

### `manifest.json`

总览文件，记录本次导出了哪些数据集、多少 trial，以及主要子目录路径。

### `demo_trials_manifest.csv`

最重要的索引表。队友选 demo 样本时建议先看这个文件。每一行对应一个导出的 trial。

主要字段：

- `dataset`：数据集名称
- `class_name`：真实标签名称
- `predicted_name`：模型预测标签名称
- `is_correct`：预测是否正确；当前导出的样本全部是 `1`
- `confidence`：模型对预测类别的置信度
- `waveform_png`：EEG 波形图路径
- `probability_png`：预测概率柱状图路径
- `saliency_png`：saliency/topomap 图路径
- `npz`：该 trial 的原始样本包路径

### `label_coverage/*.csv`

每个数据集一份 label 覆盖检查表。

字段含义：

- `correct_available`：在候选样本池中，该 label 有多少个预测正确的 trial
- `exported_trials`：最终导出了多少个 trial；当前每个 label 都应为 3

这个文件用来证明 demo 不是只挑了某几个 label，而是每个 label 都有覆盖。

## 第 5 条材料怎么用

每个 demo trial 都对应三张图，建议一起使用：

1. `figures/waveforms/<dataset>/...png`
   - EEG 原始波形图
   - 为了可读性，一般只画前几个通道
   - 可以用来展示模型输入是什么样的脑电信号

2. `figures/probabilities/<dataset>/...png`
   - 模型输出的 softmax 概率柱状图
   - 绿色柱表示预测类别，而且当前样本预测正确
   - 如果以后重新导出并包含错误样本，橙色会表示真实类别，红色会表示预测类别

3. `figures/saliency/<dataset>/...png`
   - 基于梯度的通道 saliency
   - 如果该数据集有标准电极位置，会画成 topomap
   - 如果没有合适的电极位置，会退化成通道重要性柱状图

推荐展示顺序：

```text
EEG 波形 -> 预测概率 -> saliency/topomap
```

这样一页就能讲清楚：输入信号是什么、模型判断成什么、模型主要看了哪些脑区/通道。

## 第 6 条材料怎么用

Forward pass 相关文件在：

```bash
forward_pass/
```

每个数据集有两份文件：

- `<dataset>_forward_shapes.csv`
- `<dataset>_forward_steps.json`

CSV 更适合放 PPT 或手动整理表格；JSON 更适合做网页 demo 或动画。

主要 forward pass 流程：

```text
原始 EEG 输入
-> Patch Embedding
-> Projection
-> Positional Encoding
-> 粗尺度时间分支
-> 细尺度时间分支
-> 分支内 self-attention
-> 跨分支 cross-attention
-> token attention pooling
-> classifier
-> softmax 概率
```

以 BCIC_IV_2a 为例，输入 shape 大致是：

```text
(B, 1, 22, 1000)
```

输出类别 logits/probabilities 是：

```text
(B, 4)
```

注意：不同数据集的通道数和类别数不一样，所以做动画或表格时不要只用一个固定 shape，最好直接读取对应数据集的 CSV/JSON。

## `.npz` 样本包里有什么

每个文件位于：

```bash
samples_npz/<dataset>/
```

每个 `.npz` 对应一个 trial，里面包括：

- `eeg`：EEG 样本数组，通常形状为 `(channels, time)`
- `true_label`：真实标签编号
- `predicted_label`：预测标签编号
- `probabilities`：softmax 概率
- `saliency`：每个通道的 saliency 数值
- `channel_names`：通道名；如果该数据集有通道名就会保存

如果后续要做网页 demo、交互式展示，或者重新画图，可以直接用这些 `.npz`。

## 已完成的质量检查

最终导出后已经检查过：

- `manifest.json` 中包含 10 个数据集
- 每个 label 都有 3 个导出 trial
- 每个导出 trial 都是预测正确样本，也就是 `is_correct = 1`
- 每个 trial 都有波形图、预测概率图、saliency/topomap 图和 `.npz` 文件
- 每个数据集都有 forward pass shape 文件

最终数量：

```text
78 个 trial
= 78 张波形图
+ 78 张预测概率图
+ 78 张 saliency/topomap 图
+ 78 个 npz 样本包
```

## 给队友的使用建议

- 先打开 `demo_trials_manifest.csv`，不要手动猜图片文件名。
- 做 PPT 时，选 CSV 中任意一行，把对应的 `waveform_png`、`probability_png`、`saliency_png` 三张图放在同一页。
- 做网页 demo 时，可以直接读取 CSV，然后按路径渲染这三张图。
- 标签名已经整理在 `class_name` 和 `predicted_name`，不需要再查数字编号对应关系。
- 导出时有一些预处理 warning，但最终质量检查已经通过，不影响当前 demo 材料使用。

## 如何重新生成材料

只有在源码变化、权重变化、或者想改变每个 label 的 trial 数时才需要重新跑。

命令如下：

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

默认情况下，如果某个 label 找不到预测正确的 trial，脚本会直接报错并停止。这是故意设计的，因为我们的 demo 要求是：每个 label 至少要有预测正确的样本。
