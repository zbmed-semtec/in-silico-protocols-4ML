
In-silico protocols for Machine Learning Reproducibility
===============================================

<table>
  <tr>
    <th><img src="../images/nfdi4ds_logo_badge.png" alt="NFDI4DataScience"></th>
    <th>An <a href="https://www.nfdi4datascience.de/" target="_blank">NFDI4DataScience</a> metadata service</th>
  </tr>
</table>

_Note: Our in-silico protocols aim to support machine and deep learning, here we use ML meaning both of them_

<div align="justify">

This project builds on top of [SMART Protocols](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0160-y) for wet-lab experiments. We aim to learn from them so we can build an equivalent version convering Machine Learning and Deep Learning (abbreviated as ML from now own)experiments. 

Lab-protocols often accompany wet-lab experiments as text-based documents describing the sequence of tasks and operations executed, including, e.g., references to equipment, reagents troubleshooting and tips. [SMART Protocols](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0160-y) provides a semantic layer for lab-protocols so, for instance, reagents are linked to (semantic) chemical databases such as ChEMBL. 

Similarly to wet-lab experiments, ML experiments are also composed of inputs, steps, and outputs, so they would benefit from a semantically enriched qpproqch, i.e., in-silico protocols. We aim at providing this semantic layer for ML experiments supporting FAIRness, transparency and better reproducibility for ML.

## Documentation of ML experiments

Efforts to standardize reports and documentation describing ML models include [ML Model Cards](https://huggingface.co/blog/model-cards), [ML schema](https://ml-schema.github.io/documentation/ML%20Schema.html), [DOME recommendations](https://www.nature.com/articles/s41592-021-01205-4), and [AIMe registry](https://www.nature.com/articles/s41592-021-01241-0), among others. Similarly, [Dataset Cards](https://huggingface.co/docs/hub/en/datasets-cards) are used to document those datasets used in ML experiments. 

Model cards are documents that come with the models and offer valuable insights. At their core, model cards are straightforward Markdown documents enriched with extra metadata. They play a crucial role in enhancing discoverability, ensuring reproducibility, and facilitating sharing. Model cards contain the information of the model, intended uses, biases and legal considerations, limitations, used datasets, training parameters, performance evaluation.

Dataset cards can be described in detail through the README.md file located in the repository. This document is referred to as a dataset card, and the Hugging Face Hub will display its information on the main page of the dataset. To guide users on the responsible usage of the data, it is advisable to include details regarding any possible biases present in the dataset. Typically, dataset cards assist users in grasping the details of the dataset and provide context on how it should be utilized.

In the Life Sciences domain, the DOME recommendations (Data, Optimization, Model and Evaluation) provide community-centered guidelines, recommendations, and checklists that cover these four aspects, aiming at facilitating standardized methodologies for supervised machine learning validation for computational biology. AIMe is a similar effort providing an easy way to create a report similar to Model Cards but focusing on biomedical research. 

## Acknowledgements
We would like to acknowledge our gratitude to Dr. Olga Ximena Giraldo for her contributions and guidance in developing the project's outline.

## Funding

This work is partially funded by the[ German Research Foundation (DFG)](https://www.dfg.de/en) under the [grant No. 460234259](https://gepris.dfg.de/gepris/projekt/460234259) corresponding to [NFDI4DataScience consortium](https://www.nfdi4datascience.de/).





```{toctree}
:hidden:            # keeps links out of the page body but in the sidebar
:maxdepth: 2
:caption: Contents  # header text in the sidebar

# optional: shows a “Home” button pointing to index

Semantic approaches for ML experiments <Initial_schema>

ML metadata schema <ML_metadata>

Cite us <citation>

```


