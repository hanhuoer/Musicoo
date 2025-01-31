# Musicoo

[![license](https://img.shields.io/github/license/hanhuoer/Musicoo?style=flat-square)](https://github.com/hanhuoer/Musicoo)
[![python](https://img.shields.io/badge/python-3.6-green?style=flat-square&logo=appveyor)](https://github.com/hanhuoer/Musicoo)
[![stars](https://img.shields.io/github/stars/hanhuoer/Musicoo?style=flat-square)](https://github.com/hanhuoer/Musicoo)
[![issues](https://img.shields.io/github/issues/hanhuoer/Musicoo?style=flat-square)](https://github.com/hanhuoer/Musicoo)
[![forks](https://img.shields.io/github/forks/hanhuoer/Musicoo?style=flat-square)](https://github.com/hanhuoer/Musicoo)

```
                                                                                                           
              ____                                                                                         
            ,'  , `.                                                                                       
         ,-+-,.' _ |                            ,--,                               .--,  .--,  .--,        
      ,-+-. ;   , ||         ,--,             ,--.'|               ,---.     ,---. |\  \ |\  \ |\  \       
     ,--.'|'   |  ;|       ,'_ /|   .--.--.   |  |,               '   ,'\   '   ,'\` \  `` \  `` \  `      
    |   |  ,', |  ':  .--. |  | :  /  /    '  `--'_       ,---.  /   /   | /   /   |\ \  \\ \  \\ \  \     
    |   | /  | |  ||,'_ /| :  . | |  :  /`./  ,' ,'|     /     \.   ; ,. :.   ; ,. : , \  \, \  \, \  \    
    '   | :  | :  |,|  ' | |  . . |  :  ;_    '  | |    /    / ''   | |: :'   | |: : / /` // /` // /` /    
    ;   . |  ; |--' |  | ' |  | |  \  \    `. |  | :   .    ' / '   | .; :'   | .; :` /  /` /  /` /  /     
    |   : |  | ,    :  | : ;  ; |   `----.   \'  : |__ '   ; :__|   :    ||   :    | .  /| .  /| .  /      
    |   : '  |/     '  :  `--'   \ /  /`--'  /|  | '.'|'   | '.'|\   \  /  \   \  /./__/ ./__/ ./__/       
    ;   | |`-'      :  ,      .-./'--'.     / ;  :    ;|   :    : `----'    `----'                         
    |   ;/           `--`----'      `--'---'  |  ,   /  \   \  /                                           
    '---'                                      ---`-'    `----'                                            
```

开放接口信息请查看 [Wiki](https://github.com/hanhuoer/Musicoo/wiki/Web-%E5%BC%80%E6%94%BE%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3)

## 安装

1.**克隆项目**

```
> git clone https://github.com/hanhuoer/Musicoo.git
```

2.**安装依赖**

```
> pip install -r requirements.txt
```

## 使用

1.**修改配置  `config.Setting`**

```
# config/Setting.py

# 配置 Web 服务
WEB_SERVER = {
    "HOST": "127.0.0.1",
    "PORT": 8888
}

# 以上配置在项目启动后的访问地址为 http://127.0.0.1:8888
```

2.**启动项目**

进入项目 `start` 目录

```
# 启动项目之前确保项目依赖全部安装

# 启动服务
> python Musicoo.py run
# 启动时指定 host, port 将使用 setting 中的配置
> python Musicoo.py run --host 0.0.0.0
# 启动时指定 port, host 将使用 setting 中的配置
> python Musicoo.py run --port 8888
# 启动时指定 host port
> python Musicoo.py run --host 0.0.0.0 --port 8888
```

## 更新日志

2019-12-02 版本 1.0.1 添加日志、异常处理和项目启动可选参数

2019-12-02 版本 1.0.0 首次发布

## 开源协议

[GPL](https://github.com/hanhuoer/Musicoo/blob/master/LICENSE) © hanhuoer
