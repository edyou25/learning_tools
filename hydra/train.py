import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf


class Optimizer:
    def __init__(self, name: str, lr: float, **kwargs):
        self.name = name
        self.lr = lr
        self.params = kwargs
        print(f"初始化 Optimizer: {self.name}, lr={self.lr}, params={self.params}")
    
    def __repr__(self):
        return f"Optimizer(name={self.name}, lr={self.lr}, params={self.params})"


class Dataset:
    def __init__(self, name: str, batch_size: int, shuffle: bool = True):
        self.name = name
        self.batch_size = batch_size
        self.shuffle = shuffle
        print(f"初始化 Dataset: {self.name}, batch_size={self.batch_size}, shuffle={self.shuffle}")
    
    def __repr__(self):
        return f"Dataset(name={self.name}, batch_size={self.batch_size}, shuffle={self.shuffle})"


class Model:
    def __init__(self, name: str, num_classes: int = 10):
        self.name = name
        self.num_classes = num_classes
        print(f"初始化 Model: {self.name}, num_classes={self.num_classes}")
    
    def __repr__(self):
        return f"Model(name={self.name}, num_classes={self.num_classes})"


@hydra.main(
    config_path=".", 
    config_name="config", 
    version_base=None
)
def main(cfg: DictConfig) -> None:
    print("OmegaConf.to_yaml(cfg):")
    print(OmegaConf.to_yaml(cfg))
    
    print("\n" + "=" * 60)
    print("Instantiate 练习:")
    print("=" * 60)
    
    # 1. 基本 instantiate：从配置实例化对象
    if 'optimizer' in cfg and '_target_' in cfg.optimizer:
        print("\n[1] 实例化 Optimizer:")
        optimizer = instantiate(cfg.optimizer)
        print(f"结果: {optimizer}")
        print(f"类型: {type(optimizer)}")
    
    # 2. 实例化 Dataset
    if 'dataset' in cfg and '_target_' in cfg.dataset:
        print("\n[2] 实例化 Dataset:")
        dataset = instantiate(cfg.dataset)
        print(f"结果: {dataset}")
        print(f"类型: {type(dataset)}")
    
    # 3. 实例化 Model
    if 'model' in cfg and '_target_' in cfg.model:
        print("\n[3] 实例化 Model:")
        model = instantiate(cfg.model)
        print(f"结果: {model}")
        print(f"类型: {type(model)}")
    
    # 4. 部分实例化（只传递部分参数）
    if 'optimizer' in cfg:
        print("\n[4] 部分实例化（使用 _partial_=True）:")
        if '_target_' in cfg.optimizer:
            partial_optimizer = instantiate(cfg.optimizer, _partial_=True)
            print(f"结果: {partial_optimizer}")
            print(f"类型: {type(partial_optimizer)}")
            # 调用部分实例化的函数/类
            full_optimizer = partial_optimizer(name="custom_adam", lr=999)
            print(f"完整实例化后: {full_optimizer}")
    
    # 5. 使用 _convert_ 参数
    print("\n[5] 使用 _convert_=all 自动转换类型:")
    if 'optimizer' in cfg and '_target_' in cfg.optimizer:
        optimizer_all = instantiate(cfg.optimizer, _convert_="all")
        print(f"结果: {optimizer_all}")
    


if __name__ == "__main__":
    main()