import hydra
from omegaconf import DictConfig, OmegaConf

def main() -> None:


    # 1. 从字典创建配置
    dict_cfg = OmegaConf.create(
        {"name": "yyf", 
         "lr": 0.001, 
         "tags": ["exp1", "debug"],
         "model": {
            "name": "resnet18",
            "num_classes": 1000
         }
         })
    print("\n[1] dict_cfg:")
    print(type(dict_cfg))
    print(dict_cfg)
    print(OmegaConf.to_yaml(dict_cfg))

    # 2. 从列表创建配置
    list_cfg = OmegaConf.create([1, 2, 3, {"a": 10}])
    print("\n[2] list_cfg:")
    print(type(list_cfg))
    print(list_cfg)

    # 3. 访问与修改字段
    print("\n[3] 访问与修改字段:")
    print("原 lr:", dict_cfg.lr)
    dict_cfg.lr = 999
    print("修改后 lr:", dict_cfg.lr)

    # 新增字段
    dict_cfg.new_field = "hello"
    print("新增字段 new_field:", dict_cfg.new_field)

    # 4. 插值：一个字段引用另一个字段
    interp_cfg = OmegaConf.create({
        "base_lr": 0.001,
        "warmup_lr": "${base_lr}",
        "desc": "lr is ${base_lr}"
    })
    print("\n[4] 插值 interpolation:")
    print(OmegaConf.to_yaml(interp_cfg))

    # 5. 合并配置
    cfg1 = OmegaConf.create({"a": 1, "b": 2})
    cfg2 = OmegaConf.create({"b": 3, "c": 4})
    merged = OmegaConf.merge(cfg1, cfg2)
    print("\n[5] 合并配置 merge:")
    print("cfg1:", OmegaConf.to_yaml(cfg1))
    print("cfg2:", OmegaConf.to_yaml(cfg2))
    print("merged:", OmegaConf.to_yaml(merged))

    # 6. 转为普通 Python 对象
    print("\n[6] 转为普通 Python 对象:")
    py_dict = OmegaConf.to_container(dict_cfg, resolve=True)
    print(py_dict, type(py_dict))

    # 7. register_new_resolver
    OmegaConf.register_new_resolver("eval", eval, replace=True)
    print("\n[7] register_new_resolver:")
    print("1 + 2")
    print(eval("1 + 2"))

    # 8. resolve
    print("\n[8] resolve:")
    print(OmegaConf.resolve(dict_cfg))

if __name__ == "__main__":
    main()