VALUE_CLAIM_EN = (
    "DSAINet turns complex EEG signals into reliable and interpretable brain-state "
    "assessments, offering a lightweight AI tool for scalable neurological and clinical evaluation."
)
VALUE_CLAIM_ZH = (
    "DSAINet 将复杂脑电信号转化为可靠、可解释的脑状态评估结果，"
    "为神经功能与临床筛查提供轻量化、可推广的人工智能工具。"
)

MODEL_SUMMARY_EN = [
    "Shared spatiotemporal tokenization converts raw EEG into compact token representations.",
    "Fine and coarse temporal branches capture complementary patterns at different receptive fields.",
    "Intra-branch attention refines each scale, while inter-branch attention exchanges cross-scale information.",
    "Adaptive token aggregation pools informative tokens before lightweight classification.",
]

MODEL_SUMMARY_ZH = [
    "共享时空 token 化模块将原始 EEG 转换为紧凑 token 表征。",
    "细粒度与粗粒度时间分支用不同感受野捕捉互补模式。",
    "分支内注意力精炼各自尺度，分支间注意力交换跨尺度信息。",
    "自适应 token 聚合在轻量分类前筛选更有信息量的 token。",
]

HOME_METRICS = [
    ("5", "EEG paradigms", "EEG 范式"),
    ("10", "Public datasets", "公开数据集"),
    ("13", "Baseline models", "基线模型"),
    ("76,989", "Parameters", "参数量"),
]

DATASETS = [
    {
        "Dataset": "BCIC-IV-2a", "Paradigm": "Motor Imagery", "Subjects": 9, "Channels": 22,
        "Trial Length (s)": 4, "Classes": 4, "Task Types": "left hand / right hand / feet / tongue",
        "Protocol": "LOSO", "Link": "https://www.bbci.de/competition/iv/#download",
    },
    {
        "Dataset": "BCIC-IV-2b", "Paradigm": "Motor Imagery", "Subjects": 9, "Channels": 3,
        "Trial Length (s)": 4, "Classes": 2, "Task Types": "left hand / right hand",
        "Protocol": "LOSO", "Link": "https://www.bbci.de/competition/iv/#download",
    },
    {
        "Dataset": "Zhou2016", "Paradigm": "Motor Imagery", "Subjects": 4, "Channels": 14,
        "Trial Length (s)": 5, "Classes": 3, "Task Types": "left hand / right hand / feet",
        "Protocol": "LOSO", "Link": "https://figshare.com/articles/dataset/data_zip/2061654?file=3662952",
    },
    {
        "Dataset": "OpenBMI", "Paradigm": "Motor Imagery", "Subjects": 54, "Channels": 20,
        "Trial Length (s)": 4, "Classes": 2, "Task Types": "left hand / right hand",
        "Protocol": "10-fold", "Link": "https://gigadb.org/dataset/100542",
    },
    {
        "Dataset": "PhysioNet-MI", "Paradigm": "Motor Imagery", "Subjects": 109, "Channels": 64,
        "Trial Length (s)": 4, "Classes": 4, "Task Types": "left fist / right fist / both fists / feet",
        "Protocol": "10-fold", "Link": "https://physionet.org/content/eegmmidb/1.0.0/",
    },
    {
        "Dataset": "Mumtaz2017", "Paradigm": "Mental Disorder", "Subjects": 63, "Channels": 19,
        "Trial Length (s)": 5, "Classes": 2, "Task Types": "healthy control / MDD",
        "Protocol": "10-fold", "Link": "https://figshare.com/articles/dataset/EEG_Data_New/4244171",
    },
    {
        "Dataset": "ADFTD", "Paradigm": "Neurodegenerative Disorder", "Subjects": 88, "Channels": 19,
        "Trial Length (s)": 4, "Classes": 3, "Task Types": "healthy control / AD / FTD",
        "Protocol": "10-fold", "Link": "https://openneuro.org/datasets/ds004504/versions/1.0.9",
    },
    {
        "Dataset": "Rockhill2021", "Paradigm": "Neurodegenerative Disorder", "Subjects": 31, "Channels": 32,
        "Trial Length (s)": 4, "Classes": 2, "Task Types": "healthy control / PD",
        "Protocol": "5-fold", "Link": "https://openneuro.org/datasets/ds002778/versions/1.0.5",
    },
    {
        "Dataset": "EEGMat", "Paradigm": "Mental Workload", "Subjects": 36, "Channels": 19,
        "Trial Length (s)": 2, "Classes": 2, "Task Types": "resting state / mental arithmetic",
        "Protocol": "10-fold", "Link": "https://physionet.org/content/eegmat/1.0.0/",
    },
    {
        "Dataset": "Shin2018", "Paradigm": "Cognitive Attention", "Subjects": 26, "Channels": 28,
        "Trial Length (s)": 4, "Classes": 2, "Task Types": "resting state / DSR",
        "Protocol": "10-fold", "Link": "https://doc.ml.tu-berlin.de/simultaneous_EEG_NIRS/",
    },
]

TABLE_II = [
    ["BCIC-IV-2a", 32, "1e-3", 100, "LOSO"],
    ["BCIC-IV-2b", 32, "1e-3", 100, "LOSO"],
    ["Zhou2016", 32, "1e-3", 100, "LOSO"],
    ["OpenBMI", 128, "1e-3", 100, "10-fold"],
    ["PhysioNet-MI", 128, "1e-3", 100, "10-fold"],
    ["Mumtaz2017", 128, "1e-4", 30, "10-fold"],
    ["ADFTD", 128, "1e-4", 30, "10-fold"],
    ["Rockhill2021", 32, "1e-4", 30, "5-fold"],
    ["EEGMat", 32, "1e-3", 30, "10-fold"],
    ["Shin2018", 32, "1e-3", 100, "10-fold"],
]

TABLE_III_COLUMNS = [
    "Method", "BCIC-IV-2a ACC", "BCIC-IV-2a F1", "BCIC-IV-2b ACC", "BCIC-IV-2b F1",
    "Zhou2016 ACC", "Zhou2016 F1", "OpenBMI ACC", "OpenBMI F1", "PhysioNet-MI ACC", "PhysioNet-MI F1",
]

TABLE_III = [
    ["ShallowConvNet","55.43±1.27","52.96±1.36","75.12±0.61","74.58±0.71","74.41±1.18","73.91±1.17","79.16±0.19","79.06±0.20","58.66±0.20","58.69±0.28"],
    ["DeepConvNet","59.24±0.43","56.96±0.39","75.70±0.49","75.27±0.59","74.68±0.58","74.36±0.61","81.53±0.25","81.48±0.27","61.82±0.33","61.70±0.34"],
    ["EEGNet","58.68±0.72","56.41±0.98","75.91±0.51","75.33±0.61","75.41±1.58","74.94±1.64","80.67±0.40","80.63±0.40","60.43±0.14","60.48±0.12"],
    ["ADFCNN","59.95±0.81","57.45±0.93","76.22±0.32","75.65±0.33","76.65±1.33","76.14±1.56","81.32±0.51","81.26±0.53","61.54±0.15","61.60±0.13"],
    ["LMDA-Net","54.99±0.25","52.23±0.15","76.27±0.29","75.85±0.31","76.42±0.63","76.14±0.82","80.61±0.44","80.55±0.46","59.39±0.29","59.45±0.29"],
    ["MSVTNet","58.00±0.88","54.99±1.15","75.97±0.57","75.48±0.65","76.30±1.06","75.84±1.09","80.47±0.24","80.40±0.22","62.68±0.18","62.48±0.17"],
    ["CTNet","60.08±0.71","57.62±0.76","76.30±0.56","75.82±0.62","74.41±0.55","73.64±0.78","81.89±0.36","81.84±0.36","62.67±0.17","62.69±0.19"],
    ["TMSA-Net","58.06±0.93","55.46±1.16","75.89±0.44","75.38±0.55","75.68±1.10","75.03±1.22","78.95±0.23","78.87±0.24","59.23±0.28","59.14±0.33"],
    ["Deformer","59.39±0.53","56.80±0.66","76.05±0.40","75.56±0.42","76.01±1.12","75.48±1.19","81.99±0.17","81.94±0.16","63.38±0.15","63.37±0.13"],
    ["DBConformer","58.14±0.36","55.48±0.41","76.37±0.46","75.91±0.48","76.69±0.56","76.29±0.58","79.42±0.15","79.31±0.16","61.89±0.22","61.94±0.21"],
    ["MSCFormer","58.93±0.73","56.05±0.78","76.05±0.50","75.53±0.57","75.80±1.01","75.10±1.22","80.52±0.48","80.46±0.49","62.89±0.35","62.85±0.40"],
    ["DSAINet (Ours)","61.79±0.68","59.65±0.77","76.41±0.31","75.91±0.36","78.21±0.47","77.85±0.45","82.89±0.13","82.86±0.13","63.90±0.14","63.87±0.14"],
]

TABLE_IV_COLUMNS = [
    "Method", "Mumtaz2017 ACC", "Mumtaz2017 F1", "ADFTD ACC", "ADFTD F1",
    "Rockhill2021 ACC", "Rockhill2021 F1", "EEGMat ACC", "EEGMat F1", "Shin2018 ACC", "Shin2018 F1",
]

TABLE_IV = [
    ["ShallowConvNet","85.99±0.63","85.69±0.75","56.91±0.43","55.34±0.28","70.37±0.73","69.29±1.46","68.07±0.30","66.97±0.78","75.86±0.24","75.51±0.60"],
    ["DeepConvNet","85.70±0.60","85.16±0.90","56.00±0.91","53.86±1.42","68.59±0.74","66.51±1.72","67.50±0.26","66.64±0.77","79.95±0.45","79.64±0.50"],
    ["EEGNet","82.65±1.01","82.15±1.21","54.84±0.79","53.04±1.04","69.62±1.35","68.58±2.06","68.48±0.42","67.46±0.59","78.08±0.24","77.78±0.31"],
    ["ADFCNN","85.27±0.67","84.88±0.69","57.55±0.40","56.60±0.51","71.68±1.16","70.65±1.59","70.90±0.19","70.26±0.45","77.49±0.66","77.12±0.79"],
    ["Conformer","87.79±0.37","87.55±0.38","56.76±0.54","54.98±0.91","70.49±1.21","69.68±1.11","69.48±0.74","68.53±0.87","79.25±0.29","79.03±0.29"],
    ["LMDA-Net","85.12±0.80","84.76±0.84","57.19±0.64","54.66±0.31","71.32±1.62","70.28±1.35","71.12±0.32","70.47±0.52","78.27±0.69","78.05±0.70"],
    ["CTNet","86.27±0.63","85.76±0.84","57.69±0.71","55.95±0.60","74.19±1.15","73.57±1.37","72.13±0.44","71.38±0.61","79.02±0.39","78.67±0.49"],
    ["TMSA-Net","84.92±0.33","84.32±0.28","56.41±0.39","55.55±0.60","71.47±1.32","70.88±1.07","70.37±0.46","69.83±0.55","79.85±0.46","79.63±0.46"],
    ["MGFormer","86.31±0.70","86.09±0.68","55.66±0.34","53.36±0.57","72.85±0.87","72.00±0.80","70.85±0.25","70.08±0.11","78.25±0.71","77.90±0.75"],
    ["Deformer","85.91±0.62","85.36±0.85","57.74±0.57","54.20±0.57","70.83±1.52","69.90±1.96","72.53±1.48","71.59±1.63","82.35±0.39","82.04±0.42"],
    ["MSCFormer","86.52±0.39","86.11±0.36","57.33±0.93","56.16±1.27","73.59±1.11","73.07±1.22","71.62±0.47","71.11±0.53","80.24±0.61","79.97±0.64"],
    ["DSAINet (Ours)","89.33±0.72","89.22±0.78","59.65±0.55","58.40±0.92","75.85±1.27","75.52±1.18","72.83±0.28","72.03±0.53","84.81±0.52","84.67±0.51"],
]

TABLE_V = [
    ["w/o Positional Embedding","59.76±1.26","75.71±0.97","57.06±0.87"],
    ["Single Fine-Scale Branch","59.82±0.58","75.94±0.57","58.57±0.46"],
    ["Single Coarse-Scale Branch","60.19±1.02","75.74±0.80","57.84±1.41"],
    ["w/o Attentive Interaction","59.36±0.61","75.90±0.54","57.62±1.19"],
    ["w/o Intra-Branch Attn.","60.07±0.63","75.49±0.51","58.97±1.40"],
    ["w/o Inter-Branch Attn.","60.14±0.49","75.56±0.69","57.65±1.51"],
    ["w/o Adaptive Token Aggregation","59.82±0.74","75.58±0.45","56.92±1.20"],
    ["DSAINet (Full Model)","61.79±0.68","76.41±0.31","59.65±0.55"],
]

TEAM = [
    (
        "李泽元",
        "Zeyuan Li",
        "队长、实验与可视化",
        "Group leader, Experiment & Visualization",
        [
            ("专业", "Major", "生物医学工程", "Biomedical Engineering"),
            ("兴趣", "Hobbies", "语言学习、网球、游泳", "Language Learning, Tennis, Swimming"),
            (
                "科研志趣",
                "Research Interests",
                "海马计算、脑启发神经网络、神经语言学",
                "Hippocampus computation, Brain-inspired neural networks, Neurolinguistics",
            ),
        ],
    ),
    (
        "邱子浩",
        "Zihao Qiu",
        "画图与数据处理、报告修改",
        "Drawing and data processing, report editing",
        [
            ("专业", "Major", "生物医学工程", "Biomedical Engineering"),
            (
                "兴趣爱好",
                "Hobbies",
                "热爱运动、兴趣广泛，喜欢打羽毛球、高尔夫球。",
                "Passionate about sports with broad interests; enjoys badminton and golf.",
            ),
        ],
    ),
    (
        "张琬梅",
        "Wanmei Zhang",
        "网页制作与美化、报告校对",
        "Web page creation and enhancement, report proofreading",
        [
            ("专业", "Major", "生物医学工程", "Biomedical Engineering"),
            ("兴趣爱好", "Hobbies", "音乐、电影、文学", "Music, movies, and literature"),
        ],
    ),
    (
        "王榕",
        "Rong Wang",
        "网页、演示文稿校对美化",
        "Webpage and presentation proofreading and enhancement",
        [
            ("专业", "Major", "生物医学工程", "Biomedical Engineering"),
            ("兴趣爱好", "Hobbies", "摄影和戏剧", "Photography and drama"),
        ],
    ),
    (
        "杜又郎",
        "Youlang Du",
        "报告修改、校对",
        "Report editing and proofreading",
        [
            (
                "专业",
                "Major",
                "生物医学工程",
                "Biomedical Engineering",
            ),
            (
                "研究方向",
                "Research interests",
                "Devoted to AI for Neuroscience, Neuroengineering, Neuro-Manifold",
                "Devoted to AI for Neuroscience, Neuroengineering, Neuro-Manifold",
            ),
        ],
    ),
]

KEY_REF_ROWS = [
    ["Tangermann et al., 2012", "BCI Competition IV datasets", "Standard motor imagery benchmark for cross-subject EEG decoding."],
    ["Lee et al., 2019", "OpenBMI dataset and toolbox", "Large-scale motor imagery dataset with many subjects."],
    ["Schalk et al., 2004", "PhysioNet EEG Motor Movement/Imagery", "Public EEG motor imagery resource with high channel coverage."],
    ["Mumtaz et al., 2017", "EEG-based MDD diagnosis dataset", "Clinical downstream task for depression-related EEG decoding."],
    ["Miltiadous et al., 2023", "ADFTD scalp EEG dataset", "Neurodegenerative disorder benchmark for AD/FTD/HC classification."],
    ["Zyma et al., 2019", "EEGMat mental arithmetic dataset", "Mental workload task that broadens evaluation beyond motor imagery."],
]

FIGURE_TITLES = [
    ("Fig. 1", "Overview of the general EEG decoding setting."),
    ("Fig. 2", "Overall architecture of DSAINet."),
    ("Fig. 3", "Hyperparameter sensitivity analysis."),
    ("Fig. 4", "Segment length analysis."),
    ("Fig. 5", "Accuracy-efficiency trade-off comparison."),
    ("Fig. 6", "Mean saliency maps across datasets."),
    ("Fig. 7", "Learned attention patterns."),
]
