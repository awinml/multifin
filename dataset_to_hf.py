from datasets import load_dataset
from getpass import getpass

hf_repo_path = "awinml/MultiFin"
token = getpass(prompt="Enter your HF token: ")

# All languages

all_lang_high_lvl_train = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/0-all-languages-highlevel/train.json",
    split="train",
)
all_lang_high_lvl_train.push_to_hub(hf_repo_path, token=token, split="train", config_name="all_languages_highlevel")

all_lang_high_lvl_val = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/0-all-languages-highlevel/val.json",
    split="train",  # Only train is available, when loading from a file. Does not create a DatasetDict
)
all_lang_high_lvl_val.push_to_hub(hf_repo_path, token=token, split="validation", config_name="all_languages_highlevel")

all_lang_low_lvl_train = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/0-all-languages-lowlevel/train.json",
    split="train",
)
all_lang_low_lvl_train.push_to_hub(hf_repo_path, token=token, split="train", config_name="all_languages_lowlevel")

all_lang_low_lvl_val = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/0-all-languages-lowlevel/val.json",
    split="train",
)
all_lang_low_lvl_val.push_to_hub(hf_repo_path, token=token, split="validation", config_name="all_languages_lowlevel")

# Only English Subset


only_eng_high_lvl_train = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/1-only-english-highlevel/train.json",
    split="train",
)
only_eng_high_lvl_train.push_to_hub(hf_repo_path, token=token, split="train", config_name="only_english_highlevel")

only_eng_high_lvl_val = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/1-only-english-highlevel/val.json",
    split="train",
)
only_eng_high_lvl_val.push_to_hub(hf_repo_path, token=token, split="validation", config_name="only_english_highlevel")

only_eng_low_lvl_train = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/1-only-english-lowlevel/train.json",
    split="train",
)
only_eng_low_lvl_train.push_to_hub(hf_repo_path, token=token, split="train", config_name="only_english_lowlevel")

only_eng_low_lvl_val = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/1-only-english-lowlevel/val.json",
    split="train",
)
only_eng_low_lvl_val.push_to_hub(hf_repo_path, token=token, split="validation", config_name="only_english_lowlevel")


# High Resources Subset

high_resources_high_lvl_train = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/2-high-resources-highlevel/train.json",
    split="train",
)
high_resources_high_lvl_train.push_to_hub(
    hf_repo_path, token=token, split="train", config_name="high_resources_highlevel"
)

high_resources_high_lvl_val = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/2-high-resources-highlevel/val.json",
    split="train",
)
high_resources_high_lvl_val.push_to_hub(
    hf_repo_path, token=token, split="validation", config_name="high_resources_highlevel"
)

high_resources_low_lvl_train = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/2-high-resources-lowlevel/train.json",
    split="train",
)
high_resources_low_lvl_train.push_to_hub(
    hf_repo_path, token=token, split="train", config_name="high_resources_lowlevel"
)

high_resources_low_lvl_val = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/2-high-resources-lowlevel/val.json",
    split="train",
)
high_resources_low_lvl_val.push_to_hub(
    hf_repo_path, token=token, split="validation", config_name="high_resources_lowlevel"
)


# Add fixed test sets

high_lvl_test = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/fixed-test-highlevel/test.json",
    split="train",
)
high_lvl_test.push_to_hub(hf_repo_path, token=token, split="test", config_name="all_languages_highlevel")


low_lvl_test = load_dataset(
    path="json",
    data_files="MultiFinDataset_EACL_2023/fixed-test-lowlevel/test.json",
    split="train",
)
low_lvl_test.push_to_hub(hf_repo_path, token=token, split="test", config_name="all_languages_lowlevel")
