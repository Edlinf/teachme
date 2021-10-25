# teachme
基于HoshinoBotV2的maimaidx和Arcaea教教表情包生成器

需要安装[maimaiDX](https://github.com/Yuri-YuzuChaN/maimaiDX)和[Arcaea](https://github.com/Yuri-YuzuChaN/Arcaea)模块，若未安装则需要修改对应的资源文件目录

## 使用方法
1. 将该项目放在Hoshinobot插件目录`modules`下，或者clone本项目
2. 修改`teachme.py`中的资源文件目录
3. 在`config/__bot__.py`模块列表中添加 `teachme`
4. 重启Hoshinobot

## 指令
| 命令             | 示例       | 功能       |
|------------------|-----------|-----------|
| 教教id<歌曲编号>  | 教教id786  | maimai歌曲 |
| 教教<歌曲名>      | 教教altale | arcaea歌曲 |
