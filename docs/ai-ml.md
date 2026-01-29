# :material-robot: AI & Machine Learning

Open source AI and machine learning tools, frameworks, and platforms for research and scientific computing.

## :material-brain: Open Source Large Language Models (LLMs)

### General Purpose LLMs

[Meta LLaMA](https://ai.meta.com/llama/){target=_blank} - Meta's open foundation models including Llama 3 and Llama 4 (Scout/Maverick variants) with 128k context, Apache 2.0 license

[Mistral AI](https://mistral.ai/){target=_blank} - French AI company providing open-weight models including Mistral Small 3 (24B parameters), Mistral Large 2 (123B parameters), and Mixtral MoE

[Mixtral 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1){target=_blank} - powerful Mixture-of-Experts model using 8 expert networks, Apache 2.0 license

[EleutherAI GPT-NeoX-20B](https://github.com/EleutherAI/gpt-neox){target=_blank} - 20 billion parameter model trained on The Pile dataset, Apache 2.0 license

[EleutherAI Pythia](https://github.com/EleutherAI/pythia){target=_blank} - family of models designed for research transparency and reproducibility

[BLOOM](https://huggingface.co/bigscience/bloom){target=_blank} - BigScience Large Open-science Open-access Multilingual language model with 176B parameters

[Falcon](https://huggingface.co/tiiuae/falcon-180B){target=_blank} - Technology Innovation Institute's open-source LLM family including Falcon-180B

[DeepSeek](https://github.com/deepseek-ai/DeepSeek-LLM){target=_blank} - DeepSeek-Coder and DeepSeek-Math models with strong reasoning for engineering and research

[Qwen](https://github.com/QwenLM/Qwen){target=_blank} - Alibaba Cloud's multilingual LLMs with strong performance across languages and coding

### Scientific & Research-Focused LLMs

[BioGPT](https://github.com/microsoft/BioGPT){target=_blank} - Microsoft's pre-trained language model for biomedical text generation and mining

[Galactica](https://github.com/paperswithcode/galai){target=_blank} - Meta AI's scientific knowledge model trained on 48 million papers, textbooks, and knowledge bases

[PubMedGPT](https://huggingface.co/stanford-crfm/BioMedLM){target=_blank} - Stanford CRFM's biomedical language model trained on PubMed abstracts

## :material-server: LLM Inference & Deployment

### Inference Engines

[vLLM](https://github.com/vllm-project/vllm){target=_blank} - high-throughput, memory-efficient inference engine with PagedAttention, 120-160 req/sec throughput with continuous batching

[Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference){target=_blank} - Hugging Face's production-ready inference container (maintenance mode as of Dec 2025, consider vLLM or SGLang)

[Ollama](https://ollama.com/){target=_blank} - easy-to-use local LLM deployment with simple CLI, ideal for development and prototyping

[llama.cpp](https://github.com/ggerganov/llama.cpp){target=_blank} - C++ implementation enabling LLM inference on CPU and edge devices with quantization support

[LM Studio](https://lmstudio.ai/){target=_blank} - desktop application for running LLMs locally with user-friendly GUI

[SGLang](https://github.com/sgl-project/sglang){target=_blank} - high-performance serving with strong caching and scheduler optimizations

[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM){target=_blank} - NVIDIA's optimized inference library for maximum performance on NVIDIA GPUs

### Model Serving Platforms

[Ray Serve](https://docs.ray.io/en/latest/serve/index.html){target=_blank} - scalable model serving built on Ray for distributed Python applications

[TorchServe](https://pytorch.org/serve/){target=_blank} - PyTorch's official model serving framework for production ML models

[NVIDIA Triton Inference Server](https://github.com/triton-inference-server/server){target=_blank} - high-performance inference serving for multiple frameworks (TensorFlow, PyTorch, ONNX)

## :material-robot-outline: Agentic AI Frameworks

[LangChain](https://github.com/langchain-ai/langchain){target=_blank} - comprehensive ecosystem for building LLM-powered applications with extensive integrations, chains, agents, and memory

[LlamaIndex](https://github.com/run-llama/llama_index){target=_blank} - data framework for LLM applications with sophisticated RAG capabilities and knowledge base integration

[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT){target=_blank} - pioneering autonomous AI agents that independently pursue goals through iterative planning (167k+ GitHub stars)

[CrewAI](https://github.com/joaomdmoura/crewAI){target=_blank} - framework for orchestrating role-based AI agents working as collaborative teams

[Microsoft AutoGen](https://github.com/microsoft/autogen){target=_blank} - framework enabling next-gen LLM applications with multi-agent conversation

[MetaGPT](https://github.com/geekan/MetaGPT){target=_blank} - multi-agent framework simulating software company with roles like Product Manager, Architect, Engineer

[ChatDev](https://github.com/OpenBMB/ChatDev){target=_blank} - collaborative AI agents creating software through multi-agent conversation

[BabyAGI](https://github.com/yoheinakajima/babyagi){target=_blank} - simple autonomous task-driven AI agent using OpenAI and vector databases

[AgentGPT](https://github.com/reworkd/AgentGPT){target=_blank} - browser-based autonomous AI agents for achieving user-defined goals

## :material-database-search: RAG (Retrieval Augmented Generation)

### RAG Frameworks

[LangChain RAG](https://python.langchain.com/docs/use_cases/question_answering/){target=_blank} - comprehensive RAG implementation with document loaders, text splitters, and retrievers

[LlamaIndex (GPT Index)](https://github.com/run-llama/llama_index){target=_blank} - leading data framework for RAG with advanced indexing, chunking, and retrieval

[Haystack](https://github.com/deepset-ai/haystack){target=_blank} - open source NLP framework by deepset for building RAG pipelines and semantic search

[txtai](https://github.com/neuml/txtai){target=_blank} - all-in-one embeddings database for semantic search, RAG, and LLM orchestration

### Vector Databases

[Chroma](https://www.trychroma.com/){target=_blank} - open-source embedding database for AI applications, ideal for local development and prototyping

[Weaviate](https://weaviate.io/){target=_blank} - open-source vector database with hybrid search (vector + keyword), multi-modal support

[Qdrant](https://qdrant.tech/){target=_blank} - high-performance vector similarity search engine written in Rust

[Milvus](https://milvus.io/){target=_blank} - cloud-native vector database built for scalable similarity search

[pgvector](https://github.com/pgvector/pgvector){target=_blank} - PostgreSQL extension for vector similarity search, integrates with existing PostgreSQL databases

[FAISS](https://github.com/facebookresearch/faiss){target=_blank} - Facebook AI Similarity Search library for efficient similarity search of dense vectors

[Pinecone](https://www.pinecone.io/){target=_blank} - managed vector database service (commercial with free tier)

## :material-cog-outline: MLOps Platforms

### Experiment Tracking & Model Management

[MLflow](https://mlflow.org/){target=_blank} - open-source platform for ML lifecycle including experiment tracking, model registry, and deployment

[Weights & Biases (W&B)](https://wandb.ai/){target=_blank} - AI developer platform for experiment tracking, visualization, and collaboration (free tier available)

[Neptune.ai](https://neptune.ai/){target=_blank} - metadata store for MLOps with experiment tracking and model registry

[DVC (Data Version Control)](https://dvc.org/){target=_blank} - Git-like version control for machine learning projects including data and models

[ClearML](https://clear.ml/){target=_blank} - open-source MLOps platform for experiment management and orchestration

[Comet ML](https://www.comet.com/){target=_blank} - platform for tracking, comparing, and optimizing ML experiments

### Pipeline Orchestration

[Kubeflow](https://www.kubeflow.org/){target=_blank} - Kubernetes-native ML platform for deploying, monitoring, and managing ML workflows at scale

[Apache Airflow](https://airflow.apache.org/){target=_blank} - platform for programmatically authoring, scheduling, and monitoring workflows

[Prefect](https://www.prefect.io/){target=_blank} - workflow orchestration tool for building, observing, and reacting to data pipelines

[ZenML](https://zenml.io/){target=_blank} - extensible open-source MLOps framework for production-ready ML pipelines

[Metaflow](https://metaflow.org/){target=_blank} - Netflix's framework for building and managing real-life data science projects

## :material-dna: Scientific AI Applications

### Computational Biology & Drug Discovery

[AlphaFold 3](https://alphafold.ebi.ac.uk/){target=_blank} - DeepMind's AI system for protein structure prediction, 2024 Nobel Prize in Chemistry (200M+ predictions)

[ESMFold](https://github.com/facebookresearch/esm){target=_blank} - Meta AI's protein structure prediction using language models (600M+ metagenomic proteins)

[RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold){target=_blank} - University of Washington's protein structure prediction network

[OpenFold](https://github.com/aqlaboratory/openfold){target=_blank} - open-source reproduction of AlphaFold2 and foundation for community development

[ChemBERTa](https://github.com/seyonechithrananda/bert-loves-chemistry){target=_blank} - transformer models for molecular property prediction

[DeepChem](https://deepchem.io/){target=_blank} - democratizing deep learning for drug discovery, materials science, and quantum chemistry

### Climate & Earth Science

[ClimateLearn](https://github.com/aditya-grover/climate-learn){target=_blank} - benchmark dataset and library for ML in climate science

[Microsoft AI for Earth](https://www.microsoft.com/en-us/ai/ai-for-earth){target=_blank} - AI tools and grants for environmental research and conservation

[FourCastNet](https://github.com/NVlabs/FourCastNet){target=_blank} - NVIDIA's global data-driven weather forecasting using neural networks

## :material-scale-balance: AI Ethics & Responsible AI

### Fairness & Bias Detection

[AI Fairness 360 (AIF360)](https://aif360.res.ibm.com/){target=_blank} - IBM's comprehensive toolkit with 70+ fairness metrics and 10+ bias mitigation algorithms

[Fairlearn](https://fairlearn.org/){target=_blank} - Microsoft's open-source toolkit for assessing and improving fairness of AI systems

[Aequitas](https://github.com/dssg/aequitas){target=_blank} - bias and fairness audit toolkit by Center for Data Science and Public Policy

### Explainability & Interpretability

[SHAP (SHapley Additive exPlanations)](https://github.com/slundberg/shap){target=_blank} - game-theoretic approach to explain ML model predictions

[LIME (Local Interpretable Model-agnostic Explanations)](https://github.com/marcotcr/lime){target=_blank} - explaining predictions of any machine learning classifier

[InterpretML](https://interpret.ml/){target=_blank} - Microsoft's toolkit for training interpretable models and explaining blackbox systems

[Captum](https://captum.ai/){target=_blank} - PyTorch library for model interpretability and understanding

[What-If Tool](https://pair-code.github.io/what-if-tool/){target=_blank} - Google's visual interface for probing ML model behavior

### Responsible AI Frameworks

[IBM AI Fairness 360 Toolkit](https://github.com/Trusted-AI/AIF360){target=_blank} - comprehensive fairness metrics and bias mitigation algorithms

[Google Responsible AI Practices](https://ai.google/responsibilities/responsible-ai-practices/){target=_blank} - principles and practices for responsible AI development

[Model Cards Toolkit](https://github.com/tensorflow/model-card-toolkit){target=_blank} - standardized documentation for ML models following model cards framework

## :material-tag-multiple: Data Annotation & Labeling

[Label Studio](https://labelstud.io/){target=_blank} - open-source data labeling tool for text, images, audio, video, and time series

[CVAT (Computer Vision Annotation Tool)](https://github.com/opencv/cvat){target=_blank} - free online interactive video and image annotation tool

[Labelbox](https://labelbox.com/){target=_blank} - training data platform for building AI applications (commercial with free tier)

[VGG Image Annotator (VIA)](https://www.robots.ox.ac.uk/~vgg/software/via/){target=_blank} - lightweight standalone image/video/audio annotation tool from Oxford

[Prodigy](https://prodi.gy/){target=_blank} - scriptable annotation tool for creating training and evaluation data

[Doccano](https://github.com/doccano/doccano){target=_blank} - open-source text annotation tool for classification, sequence labeling, and sequence to sequence

## :material-cloud-upload: Model Hubs & Repositories

[Hugging Face Hub](https://huggingface.co/models){target=_blank} - largest repository with 1M+ models across all modalities (NLP, vision, audio, multimodal)

[PyTorch Hub](https://pytorch.org/hub/){target=_blank} - pre-trained model repository for research reproducibility, integrated with Papers with Code

[TensorFlow Hub](https://www.tensorflow.org/hub){target=_blank} - library for publishing, discovering, and reusing ML modules in TensorFlow

[ONNX Model Zoo](https://github.com/onnx/models){target=_blank} - collection of pre-trained ONNX models for various tasks

[Papers with Code](https://paperswithcode.com/){target=_blank} - free resource linking academic papers with code implementations and leaderboards

[Model Zoo](https://modelzoo.co/){target=_blank} - discover open-source deep learning models and projects

## :material-chip: Foundation Model Training

### Training Frameworks

[DeepSpeed](https://github.com/microsoft/DeepSpeed){target=_blank} - Microsoft's deep learning optimization library for training massive models with ZeRO optimizer

[Megatron-LM](https://github.com/NVIDIA/Megatron-LM){target=_blank} - NVIDIA's framework for training multi-billion parameter language models

[Colossal-AI](https://github.com/hpcaitech/ColossalAI){target=_blank} - unified deep learning system for large-scale model training with parallelism

[Alpa](https://github.com/alpa-projects/alpa){target=_blank} - system for training and serving large-scale neural networks

### Distributed Training

[Horovod](https://github.com/horovod/horovod){target=_blank} - distributed deep learning training framework for TensorFlow, Keras, PyTorch, and MXNet

[Ray Train](https://docs.ray.io/en/latest/train/train.html){target=_blank} - scalable machine learning library for distributed training

[PyTorch Distributed](https://pytorch.org/tutorials/beginner/dist_overview.html){target=_blank} - PyTorch's native distributed training with various backends (DDP, FSDP)

[TensorFlow Distributed](https://www.tensorflow.org/guide/distributed_training){target=_blank} - TensorFlow's APIs for distributing training across multiple devices

## :material-cloud: GPU Computing & Cloud Resources

### GPU Computing Libraries

[CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit){target=_blank} - NVIDIA's parallel computing platform and programming model

[cuDNN](https://developer.nvidia.com/cudnn){target=_blank} - GPU-accelerated library for deep neural networks

[TensorRT](https://developer.nvidia.com/tensorrt){target=_blank} - NVIDIA's SDK for high-performance deep learning inference

[ROCm](https://www.amd.com/en/products/software/rocm.html){target=_blank} - AMD's open-source platform for GPU computing

[OpenCL](https://www.khronos.org/opencl/){target=_blank} - open standard for parallel programming of heterogeneous systems

### Free/Academic GPU Resources

[Google Colab](https://colab.research.google.com/){target=_blank} - free Jupyter notebooks with GPU/TPU access

[Kaggle Kernels](https://www.kaggle.com/code){target=_blank} - free notebooks with GPU acceleration for data science competitions

[Lightning AI](https://lightning.ai/){target=_blank} - cloud platform for building AI products (free tier available)

[Paperspace Gradient](https://www.paperspace.com/gradient){target=_blank} - ML development platform with free GPU instances

## :material-package-variant: ML Frameworks & Libraries

### Deep Learning Frameworks

[PyTorch](https://pytorch.org/){target=_blank} - open-source machine learning library developed by Meta AI

[TensorFlow](https://www.tensorflow.org/){target=_blank} - end-to-end open-source platform for machine learning by Google

[JAX](https://github.com/google/jax){target=_blank} - Google's composable transformations of Python+NumPy programs

[Keras](https://keras.io/){target=_blank} - high-level neural networks API running on top of TensorFlow

[MXNet](https://mxnet.apache.org/){target=_blank} - Apache's flexible and efficient deep learning library

### Classic ML Libraries

[scikit-learn](https://scikit-learn.org/){target=_blank} - comprehensive ML library for Python with classification, regression, clustering

[XGBoost](https://xgboost.readthedocs.io/){target=_blank} - optimized gradient boosting library for supervised learning

[LightGBM](https://lightgbm.readthedocs.io/){target=_blank} - Microsoft's fast, distributed, high-performance gradient boosting framework

[CatBoost](https://catboost.ai/){target=_blank} - gradient boosting library with categorical features support

## :material-api: LLM APIs & Prompt Engineering

[OpenAI API](https://platform.openai.com/){target=_blank} - access to GPT-4, GPT-3.5, DALL-E, and other OpenAI models (commercial)

[Anthropic Claude API](https://www.anthropic.com/api){target=_blank} - API access to Claude models including Claude Opus, Sonnet, and Haiku (commercial)

[Cohere API](https://cohere.com/){target=_blank} - NLP platform with embeddings, generation, and classification APIs (commercial)

[Together AI](https://www.together.ai/){target=_blank} - fastest cloud platform for building and running generative AI

[OpenRouter](https://openrouter.ai/){target=_blank} - unified API for multiple LLM providers with single integration

[PromptLayer](https://promptlayer.com/){target=_blank} - platform for prompt engineering and LLM observability

## Additional Resources

[Awesome LLM](https://github.com/Hannibal046/Awesome-LLM){target=_blank} - curated list of Large Language Model resources

[Awesome MLOps](https://github.com/visenger/awesome-mlops){target=_blank} - curated list of MLOps tools and practices

[Awesome Production Machine Learning](https://github.com/EthicalML/awesome-production-machine-learning){target=_blank} - curated list of production-level ML tools

[State of AI Report](https://www.stateof.ai/){target=_blank} - annual comprehensive report on AI progress and trends
