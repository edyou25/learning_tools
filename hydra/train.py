import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(
    config_path=".", 
    config_name="config", 
    version_base=None
)
def main(cfg: DictConfig) -> None:

    print(OmegaConf.to_yaml(cfg))
    

if __name__ == "__main__":
    main()