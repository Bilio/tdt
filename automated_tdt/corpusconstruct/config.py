import os

CUR_PATH = os.path.normpath(os.path.dirname(__file__))
RAW_DATA_DIR = os.path.abspath(os.path.join(CUR_PATH, "..", "data", "raw"))
CORPUS_DATA_DIR = os.path.abspath(os.path.join(CUR_PATH, "..", "data", "corpus"))
TDT_CORPUS_DIR = os.path.abspath(os.path.join(CUR_PATH, "..", "data", "tdt_corpus"))