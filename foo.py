from pametric import PosteriorAgreementBase, LogitsDataset

pa_metric = PosteriorAgreementBase(pa_epochs, beta_0)
results = pa_metric(
    LogitsDataset([logits0, logits1], y)
)

logPA, beta = results["logPA"], results["beta"]



