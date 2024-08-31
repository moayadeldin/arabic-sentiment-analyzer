# arabic-sentiment-analyzer
Arabic Sentiment Analyzer: Integrating State-of-the-Art Pre-trained Sentiment Models (AraBERT, and AraNet) in a Single Tool.

AraBERT was fine-tuned on ASTD-Unbalanced dataset and AraNet model was utilized as the authors provided.

## Demo

https://github.com/user-attachments/assets/43e2493c-8a55-455a-b73e-710c9a2f837e


## How to Use

1. Clone the repo and navigate to the project:
   ```bash
   git clone https://github.com/moayadeldin/AraNet
   cd arabic-sentiment-analyzer
   ```
2. In order to use AraNet, you may need to install the forked version of the original repo that addressed the dependencies issues and install it.
   ```bash
   git clone https://github.com/moayadeldin/AraNet
   pip install -e .
   ```
3. Start using the app
      ``` bash
      python -m streamlit run app.py
      ```

## Download the Models
[AraBERT ASTD-Unbalanced](https://drive.google.com/drive/folders/1QU6y5aoJIMWyf_vhNVB1aRwqcgxMFXxB?usp=drive_link)

[AraNet](https://drive.google.com/drive/folders/1gIXFEiF2Thh8bg-Xn2XHrEDMvlNORies?usp=drive_link)

## References
[AraBERT: Transformer-based Model for Arabic Language Understanding](https://aclanthology.org/2020.osact-1.2) (Antoun et al., OSACT 2020)
[Abdul-Mageed, M., Zhang, C., Hashemi, A., & Nagoudi, E. M. B. (2020). *AraNet: A Deep Learning Toolkit for Arabic Social Media*. arXiv.](https://arxiv.org/abs/1912.13072)


