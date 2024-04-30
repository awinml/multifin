# MultiFin: A Dataset for Multilingual Financial NLP

MultiFin is a publicly available financial dataset consisting of real-world article headlines covering 15 languages across different writing systems and language families. The dataset consists of a hierarchical label structure providing two classification tasks: multi-label and multi-class.

## Dataset Sources

- **Repository:** <https://github.com/RasmusKaer/MultiFin>
- **Paper:** <https://aclanthology.org/2023.findings-eacl.66/>
- **HuggingFace:** <https://huggingface.co/datasets/awinml/MultiFin> 


## Dataset Description

The MULTIFIN dataset is a multilingual corpus, consisting of real-world article headlines covering 15
languages. The corpus is annotated using hierarchical label structure, providing two classification tasks:
multi-class and multi-label classification.

- **Curated by:** Rasmus Jørgensen, Oliver Brandt, Mareike Hartmann, Xiang Dai, Christian Igel, and Desmond Elliott.
- **Language(s) (NLP):** English, Spanish, Polish, Hungarian, Greek, Danish, Turkish, Japanese, Swedish, Finnish, Norwegian, Russian, Italian, Hebrew, Icelandic.
- **License:** [More Information Needed]

## Dataset Structure

The dataset consists of 10,048 headlines in 15 languages annotated with 23 topic labels for LOW-LEVEL and 6 HIGH-LEVEL topics for multi-class.

The dataset has been further stratified into two subsets:

1. **only_english**: that contains only English training data.
2. **high_resources:** a subset that contains 5 high-resource languages (i.e., English, Turkish, Danish, Spanish, Poland).

## Citation

**BibTeX:**

```
@inproceedings{jorgensen-etal-2023-multifin,
    title = "{M}ulti{F}in: A Dataset for Multilingual Financial {NLP}",
    author = "J{\o}rgensen, Rasmus  and
      Brandt, Oliver  and
      Hartmann, Mareike  and
      Dai, Xiang  and
      Igel, Christian  and
      Elliott, Desmond",
    editor = "Vlachos, Andreas  and
      Augenstein, Isabelle",
    booktitle = "Findings of the Association for Computational Linguistics: EACL 2023",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-eacl.66",
    doi = "10.18653/v1/2023.findings-eacl.66",
    pages = "894--909",
    abstract = "Financial information is generated and distributed across the world, resulting in a vast amount of domain-specific multilingual data. Multilingual models adapted to the financial domain would ease deployment when an organization needs to work with multiple languages on a regular basis. For the development and evaluation of such models, there is a need for multilingual financial language processing datasets. We describe MultiFin {--} a publicly available financial dataset consisting of real-world article headlines covering 15 languages across different writing systems and language families. The dataset consists of hierarchical label structure providing two classification tasks: multi-label and multi-class. We develop our annotation schema based on a real-world application and annotate our dataset using both {`}label by native-speaker{'} and {`}translate-then-label{'} approaches. The evaluation of several popular multilingual models, e.g., mBERT, XLM-R, and mT5, show that although decent accuracy can be achieved in high-resource languages, there is substantial room for improvement in low-resource languages.",
}
```
