[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://zbmed-semtec.github.io/in-silico-protocols-4ML/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17048004.svg)](https://doi.org/10.5281/zenodo.17048004)

# In-silico protocols for ML reproducibility
_Note: Our in-silico protocols work for machine and deep learning, here we use ML meaning both ML and DL_

<div align="justify">

This project builds on top of [SMART Protocols](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0160-y) for wet-lab experiments. We aim to learn from them so we can build an equivalent version convering Machine Learning and Deep Learning (abbreviated as ML from now own)experiments. 

Lab-protocols often accompany wet-lab experiments as text-based documents describing the sequence of tasks and operations executed, including, e.g., references to equipment, reagents troubleshooting and tips. [SMART Protocols](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0160-y) provides a semantic layer for lab-protocols so, for instance, reagents are linked to (semantic) chemical databases such as ChEMBL. 

Similarly to wet-lab experiments, ML experiments are also composed of inputs, steps, and outputs, so they would benefit from a semantically enriched qpproqch, i.e., in-silico protocols. We aim at providing this semantic layer for ML experiments supporting FAIRness, transparency and better reproducibility for ML.

## Documentation of ML experiments

Efforts to standardize reports and documentation describing ML models include [ML Model Cards](https://huggingface.co/blog/model-cards), [ML schema](https://ml-schema.github.io/documentation/ML%20Schema.html), [DOME recommendations](https://www.nature.com/articles/s41592-021-01205-4), and [AIMe registry](https://www.nature.com/articles/s41592-021-01241-0), among others. Similarly, [Dataset Cards](https://huggingface.co/docs/hub/en/datasets-cards) are used to document those datasets used in ML experiments. 

Model cards are documents that come with the models and offer valuable insights. At their core, model cards are straightforward Markdown documents enriched with extra metadata. They play a crucial role in enhancing discoverability, ensuring reproducibility, and facilitating sharing. Model cards contain the information of the model, intended uses, biases and legal considerations, limitations, used datasets, training parameters, performance evaluation.

Dataset cards can be described in detail through the README.md file located in the repository. This document is referred to as a dataset card, and the Hugging Face Hub will display its information on the main page of the dataset. To guide users on the responsible usage of the data, it is advisable to include details regarding any possible biases present in the dataset. Typically, dataset cards assist users in grasping the details of the dataset and provide context on how it should be utilized.

In the Life Sciences domain, the DOME recommendations (Data, Optimization, Model and Evaluation) provide community-centered guidelines, recommendations, and checklists that cover these four aspects, aiming at facilitating standardized methodologies for supervised machine learning validation for computational biology. AIMe is a similar effort providing an easy way to create a report similar to Model Cards but focusing on biomedical research. 

## Semantic approaches for ML experiments

Semantic representations for ML experiments are still new. Recent efforts by [ML Commons](https://mlcommons.org/) provide a representation based on schema.org for datasets used in ML experiments, namely [Croissant ML](https://github.com/mlcommons/croissant). 

On its side, the [RDA FAIR4ML Interest Group](https://www.rd-alliance.org/groups/fair-machine-learning-fair4ml-ig/) has been working on an extension of schema.org to present ML models, vr 0.0.1 was released in 2024-06-04 and is available at [FAIR4ML for ML models](https://w3id.org/fair4ml). This version was created based on [crosswalks](https://github.com/RDA-FAIR4ML/FAIR4ML-crosswalks), mostly done during a hackathon organized at [ZB MED](https://zbmed.de/en/) in November 2023, as part of the activities of the [NFDI4DataScience consortium](https://www.nfdi4datascience.de/). This RDA group is also working on FAIRness for ML and FAIR elements associated with the ML life cycle.  

</div>

## Acknowledgements
We would like to acknowledge our gratitude to Dr. Olga Ximena Giraldo for her contributions and guidance in developing the project's outline.


## Funding

This work is partially funded by the[ German Research Foundation (DFG)](https://www.dfg.de/en) under the [grant No. 460234259](https://gepris.dfg.de/gepris/projekt/460234259) corresponding to [NFDI4DataScience consortium](https://www.nfdi4datascience.de/).

</div>

