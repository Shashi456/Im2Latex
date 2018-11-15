# Im2Latex
- Solving the Open-AI Request for Research
- The dataset has to be downloaded from [here](https://zenodo.org/record/56198#.V2p0KTXT6eA)
- The dataset has to be preprocessed to generate vocabulary and tokenize the labels. 
- Preprocessing scripts have been taken from HarvardNLP's [solution](https://github.com/harvardnlp/im2markup) and all credit for these scripts are due to them.

## Preprocessing 
- The following instructions were run to generate the files :

```python preprocessing/preprocess_images.py --input-dir formula_images --output-dir images_processed```

```python preprocessing/preprocess_filter.py --filter --image-dir images_processed --label-path formulas.token.lst --data-path im2latex_train.lst --output-path train_filter.lst ```

```python preprocessing/preprocess_formulas.py --mode tokenize --input-file im2latex_formulas.lst --output-file formulas.token.lst```

```python scripts/preprocessing/generate_latex_vocab.py --data-path train_filter.lst --label-path formulas.token.lst --output-file latex_vocab.txt```


## Methodology

- We will be using the Top-down Bottom-up Attention Model Paper and adopting the architecture to this model.

