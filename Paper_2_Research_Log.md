# Paper 2 — Research Development Log

## Selected Research Title

**Lightweight Explainable TinyML Framework for Real-Time Intrusion Detection in Resource-Constrained AIoT Edge Networks**

---

# Research Direction

This project focuses on:

- TinyML-based Intrusion Detection Systems (IDS)
- AIoT edge security
- Explainable AI (XAI)
- Lightweight deployment feasibility
- TensorFlow Lite optimization
- Runtime-aware edge inference

---

# Experimental Pipeline

## 1. Dataset Selection

Dataset:
- CICIoT2023

Original dataset statistics:
- Samples: 5,491,971
- Features: 47

---

## 2. Binary IDS Formulation

The original multi-class intrusion labels were converted into:

- Benign → 0
- Attack → 1

Reasoning:
- Simplifies TinyML deployment
- Reduces computational complexity
- Supports lightweight edge inference

---

## 3. Balanced Dataset Construction

Balanced subset:
- 50,000 benign samples
- 50,000 attack samples

Final balanced dataset:
- 100,000 samples

Motivation:
- Reduce computational overhead
- Mitigate severe class imbalance
- Improve TinyML experimentation feasibility

---

# Feature Engineering

## 4. Zero / Near-Zero Variance Removal

Removed features:

- ece_flag_number
- cwr_flag_number
- SMTP
- Telnet
- IRC
- DHCP
- Drate
- SSH
- ARP
- IPv
- LLC
- DNS

Reason:
- Statistical redundancy
- Minimal contribution to learning

---

## 5. Correlation Analysis

Highly correlated features were removed to:
- Reduce redundancy
- Improve lightweight deployment
- Lower memory overhead

---

## 6. Final Selected Features

Final TinyML feature space (20 features):

- rst_count
- urg_count
- AVG
- Variance
- Tot size
- flow_duration
- Std
- Covariance
- Header_Length
- IAT
- Max
- Tot sum
- Duration
- Protocol Type
- HTTPS
- Number
- ack_flag_number
- Min
- Rate
- UDP

---

# Baseline IDS

## Random Forest Baseline

Results:

| Metric | Score |
|---|---|
| Accuracy | 0.9969 |
| Precision | 0.9993 |
| Recall | 0.9944 |
| F1-score | 0.9968 |

---

# TinyML IDS Architecture

Architecture:

20 Features
→ Dense(32, ReLU)
→ Dropout(0.2)
→ Dense(16, ReLU)
→ Dropout(0.2)
→ Sigmoid Output

Total Parameters:
- 1,217

---

# TinyML Training Results

| Metric | Score |
|---|---|
| Accuracy | 0.9922 |
| Precision | 0.9984 |
| Recall | 0.9860 |
| F1-score | 0.9922 |

Observations:
- Stable convergence
- Minimal overfitting
- High detection capability despite lightweight design

---

# Quantization and Compression

TensorFlow Lite conversion was performed using post-training quantization.

## Model Sizes

| Model | Size |
|---|---|
| Original Model | 43.41 KB |
| Quantized TFLite | 6.77 KB |

Compression Ratio:
- 6.41×

---

# Explainable TinyML (SHAP)

SHAP analysis was integrated to:
- Interpret intrusion decisions
- Validate feature reduction
- Improve transparency

Important SHAP features:
- Variance
- rst_count
- Number
- IAT
- ack_flag_number

Key observation:
- Strong consistency between SHAP explanations and Random Forest feature importance.

---

# Runtime Profiling

TensorFlow Lite runtime profiling was performed.

## Runtime Result

| Metric | Value |
|---|---|
| Average Inference Latency | 0.0093 ms |

Interpretation:
- Extremely lightweight inference
- Strong real-time suitability
- Edge-oriented deployment feasibility

---

# Edge Feasibility Discussion

The proposed TinyML IDS demonstrated:

- Lightweight execution
- Compact architecture
- Quantized inference capability
- Explainable security behavior
- Resource-aware deployment feasibility

Target edge assumptions:
- ESP32-class AIoT constraints

---

# Scientific Figures Generated

## Figures

1. Baseline vs TinyML Performance
2. Model Compression Comparison
3. Training Convergence Curve
4. TinyML Architecture Diagram
5. Final SHAP Summary Plot

---

# Scientific Tables Generated

## Tables

1. Dataset Description
2. Removed Features
3. Selected Features
4. Experimental Results
5. Runtime & Resource Evaluation

---

# Academic Writing Rules Adopted

Writing strategy includes:

- Researcher-natural academic style
- Controlled under-optimization
- Mechanism-oriented writing
- Avoidance of AI-suspicious patterns
- Evidence-based interpretation
- TinyML claim discipline
- Q1/Q2 publication-oriented structure

---

# Final Experimental Status

Completed:
- Dataset preparation
- Feature engineering
- TinyML training
- Quantization
- Explainability
- Runtime profiling
- Edge feasibility analysis
- Figures and tables package

Next phase:
- Abstract writing
- Introduction
- Related Work
- Methodology
- Results
- Discussion
- Conclusion

