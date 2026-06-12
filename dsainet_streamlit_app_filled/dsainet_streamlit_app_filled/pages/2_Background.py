import streamlit as st
from pathlib import Path
import sys

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from utils import inject_css, init_lang_state, sidebar_language_switcher, tr, section_badge

st.set_page_config(page_title="Background | DSAINet", layout="wide")
inject_css()
init_lang_state()

asset_dir = Path(__file__).resolve().parents[1] / "assets"
what_is_eeg_img = asset_dir / "ChatGPT Image Jun 9, 2026, 03_11_57 PM (1).png"
why_eeg_matters_img = asset_dir / "ChatGPT Image Jun 9, 2026, 03_11_58 PM (3).png"
eeg_difficulty_img = asset_dir / "ChatGPT Image Jun 9, 2026, 03_11_58 PM (4).png"
cross_subject_img = asset_dir / "ChatGPT Image Jun 9, 2026, 03_11_59 PM (5).png"

with st.sidebar:
    sidebar_language_switcher()

section_badge("Why this matters", "为什么重要")
st.title(tr("Background: why general EEG decoding matters", "背景：为什么通用 EEG 解码值得关注"))

# What is EEG
st.markdown(f"## {tr('What is EEG?', '什么是 EEG？')}")
col1, col2 = st.columns([1, 1.2], gap="large")
with col1:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-body">
                {tr("Electroencephalography (EEG) records noninvasive electrical brain activity from scalp electrodes. Each electrode measures voltage changes caused by synchronized neural firing, typically sampled at 250–500 Hz.", "脑电图（EEG）通过头皮电极无创记录脑电活动。每个电极测量由同步神经放电引起的电压变化，通常以 250–500 Hz 的频率采样。")}
                <br/><br/>
                <b>{tr("Key features:", "关键特点：")}</b><br/>
                • {tr("Temporal resolution: milliseconds", "时间分辨率：毫秒级")}<br/>
                • {tr("Spatial resolution: tens of channels", "空间分辨率：数十个通道")}<br/>
                • {tr("Cost-effective and portable", "成本低、便携性好")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.image(str(what_is_eeg_img), use_container_width=True)
    st.caption(
        tr(
            "EEG records scalp electrode signals and converts multichannel waveforms into task-relevant features.",
            "EEG 从头皮电极记录多通道信号，并将波形转换为任务相关特征。",
        )
    )
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{tr("Project perspective", "项目视角")}</div>
            <div class="section-body">
                {tr("The paper defines <b>general EEG decoding</b> as using a unified model across multiple EEG tasks under subject-independent evaluation, with a shared architecture and consistent hyperparameters.", "论文把<b>通用 EEG 解码</b>定义为：在跨受试者评估下，用统一模型处理多个 EEG 任务，并保持共享结构与一致的超参数。")}
                <br/><br/>
                {tr("This is fundamentally different from building task-specific or subject-specific models.", "这与构建任务特定或受试者特定的模型本质上不同。")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Why EEG matters
st.write("")
st.markdown(f"## {tr('Why EEG Decoding Matters', '为什么 EEG 解码重要')}")
st.image(str(why_eeg_matters_img), use_container_width=True)
st.caption(
    tr(
        "EEG decoding connects brain activity with applications in BCI, clinical monitoring, and cognitive assessment.",
        "EEG 解码将脑活动与脑机接口、临床监测和认知评估等应用连接起来。",
    )
)
st.write("")

tab1, tab2, tab3 = st.tabs([
    tr("Brain–Computer Interfaces", "脑机接口"),
    tr("Clinical Diagnosis", "临床诊断"),
    tr("Cognitive Monitoring", "认知监测"),
])

with tab1:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{tr("Brain–Computer Interfaces (BCI)", "脑机接口 (BCI)")}</div>
            <div class="section-body">
                {tr("EEG-based BCIs enable direct communication between the brain and external devices without muscular involvement.", "基于 EEG 的脑机接口让大脑能直接与外部设备通信，无需肌肉参与。")}
                <br/><br/>
                <b>{tr("Applications:", "应用场景：")}</b><br/>
                • {tr("Assistive devices for paralyzed patients", "为瘫痪患者提供辅助设备")}<br/>
                • {tr("Cursor/robotic arm control", "光标 / 机械臂控制")}<br/>
                • {tr("Neurofeedback-based rehabilitation", "神经反馈康复")}<br/>
                • {tr("Real-time attention monitoring in safety-critical tasks", "关键任务中的实时注意力监测")}
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

with tab2:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{tr("Clinical Diagnosis & Screening", "临床诊断与筛查")}</div>
            <div class="section-body">
                {tr("EEG patterns are biomarkers for many neurological and psychiatric conditions.", "EEG 模式是许多神经精神疾病的生物标志物。")}
                <br/><br/>
                <b>{tr("Examples:", "例子：")}</b><br/>
                • {tr("Epilepsy: seizure detection and classification", "癫痫：发作检测和分类")}<br/>
                • {tr("Alzheimer's disease: background slowing and abnormal oscillations", "阿尔茨海默病：背景减速和异常振荡")}<br/>
                • {tr("Depression & anxiety: resting-state asymmetry, altered connectivity", "抑郁症与焦虑症：静息态不对称、连接性改变")}<br/>
                • {tr("Sleep disorders: abnormal sleep stages and arousals", "睡眠障碍：异常睡眠阶段和觉醒")}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tab3:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{tr("Cognitive Monitoring & Automation", "认知监测与自动化")}</div>
            <div class="section-body">
                {tr("EEG can detect mental states in real time, enabling proactive interventions.", "EEG 可实时检测心理状态，实现主动干预。")}
                <br/><br/>
                <b>{tr("Practical uses:", "实际应用：")}</b><br/>
                • {tr("Driver drowsiness detection for accident prevention", "驾驶员困倦检测防止事故")}<br/>
                • {tr("Student attention tracking in adaptive learning", "自适应学习中的学生注意力追踪")}<br/>
                • {tr("Operator fatigue monitoring in nuclear/aviation contexts", "核电 / 航空中操作员疲劳监测")}<br/>
                • {tr("Workload assessment during human–computer interaction", "人机交互中的工作量评估")}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Why it's difficult
st.write("")
st.markdown(f"## {tr('Why EEG Decoding is Difficult', '为什么 EEG 解码困难')}")
st.image(str(eeg_difficulty_img), use_container_width=True)
st.caption(
    tr(
        "Core challenges include low signal-to-noise ratio, inter-subject variability, and multi-scale temporal patterns.",
        "核心挑战包括低信噪比、跨受试者差异和多时间尺度模式。",
    )
)
st.write("")

col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{tr("Low Signal-to-Noise Ratio", "低信噪比")}</div>
            <div class="metric-text">
                {tr("EEG signals are contaminated by muscle artifacts, environmental noise, and eye movement. The signal of interest is often buried in noise.", "EEG 信号受肌肉伪迹、环境噪声和眼动污染。目标信号常被淹没在噪声中。")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{tr("Inter-Subject Variability", "跨受试者差异")}</div>
            <div class="metric-text">
                {tr("Different individuals have different brain anatomy, baseline activity, and responsiveness. A model trained on some subjects often fails on new ones.", "不同个体的脑解剖、基线活动和反应性都不同。在某些受试者上训练的模型常在新受试者上失效。")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{tr("Multi-Scale Temporal Patterns", "多时间尺度模式")}</div>
            <div class="metric-text">
                {tr("Task-relevant cues exist at different timescales: fast oscillations (20–40 Hz), slower components (0.5–2 Hz), and context-dependent dynamics.", "任务相关线索存在于不同时间尺度：快速振荡 (20–40 Hz)、慢成分 (0.5–2 Hz) 和上下文相关动态。")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Why cross-subject evaluation matters
st.write("")
st.markdown(f"## {tr('Why Cross-Subject Evaluation Matters', '为什么跨受试者评估重要')}")
st.image(str(cross_subject_img), use_container_width=True)
st.caption(
    tr(
        "Subject-independent evaluation better reflects whether an EEG decoder can generalize to unseen people.",
        "受试者无关评估更能反映 EEG 解码模型是否能泛化到未见过的新个体。",
    )
)
st.write("")

st.markdown(
    f"""
    <div class="section-card">
        <div class="section-body">
            <b>{tr("Subject-dependent vs. subject-independent:", "受试者相关 vs. 受试者无关：")}</b><br/>
            <br/>
            <b>{tr("Subject-dependent (within-subject):", "受试者相关（受试者内）：")}</b><br/>
            {tr("Train and test on the same subject. Usually reports high accuracy (>90%), but cannot tell you if the model will work on new people.", "在同一受试者上训练和测试。通常报告高精度（>90%），但无法告诉你模型是否能在新人身上工作。")}
            <br/>
            <br/>
            <b>{tr("Subject-independent (cross-subject):", "受试者无关（跨受试者）：")}</b><br/>
            {tr("Train on some subjects, test on completely unseen subjects. This is the real-world deployment scenario. Accuracy drops significantly but reflects true generalization.", "在某些受试者上训练，在全新受试者上测试。这是真实部署场景。精度下降明显，但反映了真正的泛化能力。")}
            <br/>
            <br/>
            {tr("Our work focuses exclusively on subject-independent evaluation because it is:", "我们的工作专注于跨受试者评估，因为它是：")}
            <br/>
            ✓ {tr("More challenging and informative", "更具挑战性和信息量")}<br/>
            ✓ {tr("More aligned with practical deployment", "更符合实际部署")}<br/>
            ✓ {tr("Not often addressed in the literature", "文献中较少涉及")}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Core message
st.write("")
st.markdown(
    f"""
    <div class="soft-note">
        <b>{tr("Core Message", "核心信息")}</b><br/>
        {tr("Our work is <b>not</b> just another high-accuracy deep learning model. Instead, it targets a harder and more realistic biomedical-engineering deployment scenario: building a single, unified, lightweight architecture that generalizes well to new subjects across multiple EEG paradigms and clinical contexts.", "我们的工作<b>不仅仅</b>是另一个高精度深度学习模型。我们的目标是一个更困难、更接近实际部署的生物医学工程场景：构建一个单一、统一、轻量的架构，能在多个 EEG 范式和临床背景下好地泛化到新受试者。")}
    </div>
    """,
    unsafe_allow_html=True,
)
