# In-silico protocols for ML models
<div align="justify">

This project builds on top of [SMART Protocols](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0160-y) for wet-lab experiments to adapt them and extend them to cover Machine Learning experiments. 

Lab-protocols often accompany wet-lab experiments as text-based documents describing the sequence of tasks and operations executed, including, e.g., references to equipment, reagents troubleshooting and tips. [SMART Protocols](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0160-y) provides a semantic layer for lab-protocols so, for instance, reagents are linked to (semantic) chemical databases such as ChEMBL. 

Similarly to wet-lab experiments, Machine Learning (ML) experiments are also composed of inputs, steps and outputs and would benefit from semantically enriched in-silico protocols. We aim at providing a semantic layer, namely in-silico protocol, for ML experiments supporting FAIRness for ML, transparency and reproducible outcomes.

## Documentation of ML experiments

Efforts to standardize reports and documentation describing ML models include [ML Model Cards](https://huggingface.co/blog/model-cards), [DOME recommendations](https://www.nature.com/articles/s41592-021-01205-4), and [AIMe registry](https://www.nature.com/articles/s41592-021-01241-0), while [Dataset Cards](https://huggingface.co/docs/hub/en/datasets-cards) are used to document those datasets used in ML experiments. 

DOME recommendations stands for Data, Optimization, Model and Evaluation in the general ML pipeline. DOME comprises an extensive array of community-centered guidelines, recommendations, and checklists that cover these four domains, aimed at facilitating standardized methodologies for supervised machine learning validation within the biological sciences.

Model cards are documents that come with the models and offer valuable insights. At their core, model cards are straightforward Markdown documents enriched with extra metadata. They play a crucial role in enhancing discoverability, ensuring reproducibility, and facilitating sharing. Model cards contain the information of the model, intended uses, biases and legal considerations, limitations, used datasets, training parameters, performance evaluation.
Dataset cards can be described in detail through the README.md file located in the repository. This document is referred to as a dataset card, and the Hugging Face Hub will display its information on the main page of the dataset. To guide users on the responsible usage of the data, it is advisable to include details regarding any possible biases present in the dataset. Typically, dataset cards assist users in grasping the details of the dataset and provide context on how it should be utilized.

## Semantic approaches for ML experiments

Semantic representations for ML experiments are still new. Recent efforts by [ML Commons](https://mlcommons.org/) provide a representation based on schema.org for datasets used in ML experiments, namely [Croissant ML](https://github.com/mlcommons/croissant). 

On its side, the [RDA FAIR4ML Interest Group](https://www.rd-alliance.org/groups/fair-machine-learning-fair4ml-ig/) has been working on an extension of schema.org to present ML models, vr 0.0.1 was released in 2024-06-04 and is available at [FAIR4ML for ML models](https://w3id.org/fair4ml). This version was created based on [crosswalks](https://github.com/RDA-FAIR4ML/FAIR4ML-crosswalks), mostly done during an NFDI4DS hackathon at ZB MED in November 2023. This group is also working on FAIRness for ML and FAIR elements associated with the ML life cycle.  

</div>

## Acknowledgements
I would like to express my gratitude to Dr. Olga Ximena Giraldo for her invaluable contributions and guidance in developing the project's outline.


## Funding

This work is partially funded by the[ German Research Foundation (DFG)](https://www.dfg.de/en) under the [grant No. 460234259](https://gepris.dfg.de/gepris/projekt/460234259) corresponding to [NFDI4DataScience consortium](https://www.nfdi4datascience.de/).

</div>

