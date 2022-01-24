"""
dirty_cat: Learning on dirty categories.
"""
import os

version_file = os.path.join(os.path.dirname(__file__), 'VERSION.txt')
with open(version_file) as fh:
    __version__ = fh.read().strip()

from .similarity_encoder import SimilarityEncoder
from .target_encoder import TargetEncoder
from .minhash_encoder import MinHashEncoder
from .gamma_poisson_factorization import OnlineGammaPoissonFactorization
from .pretrained_fastText import PretrainedFastText

__all__ = ['SimilarityEncoder', 'TargetEncoder', 'MinHashEncoder', 'OnlineGammaPoissonFactorization',
          'PretrainedFastText']
