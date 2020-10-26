from phoenix_datasets import PhoenixVideoTextDataset

from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence

dtrain = PhoenixVideoTextDataset(
    "data/phoenix-2014-multisigner",
    "train",
    p_drop=0.5,
    random_drop=True,
)

vocab = dtrain.vocab

print("Vocab", vocab)

dl = DataLoader(dtrain, collate_fn=dtrain.collate_fn)

for batch in dl:
    video = batch["video"]
    text = batch["text"]

    # augment data (e.g. normalization, cropping) here if needed.
    # kornia will be a good tool for this
    # video = augment(video)

    assert len(video) == len(text)
    print(len(video))
    print(video[0].shape)
    print(text[0].shape)

    break