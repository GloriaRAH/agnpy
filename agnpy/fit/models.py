from .gammapy_wrapper import SynchrotronSelfComptonSpectralModel
from .sherpa_wrapper import SynchrotronSelfComptonRegriddableModel1D


class SynchrotronSelfComptonModel:
    """Model for synchrotron self-Compton scenario."""

    def __new__(cls, n_e, ssa=False, backend="gammapy"):
        if backend == "gammapy":
            return SynchrotronSelfComptonSpectralModel(n_e, ssa)
        elif backend == "sherpa":
            return SynchrotronSelfComptonRegriddableModel1D(n_e, ssa)
