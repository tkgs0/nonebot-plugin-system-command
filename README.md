<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-system-command

_✨ Call the system command-line in NoneBot2 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/tkgs0/nonebot-plugin-system-command.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-system-command">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-system-command.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
</a>
<a href="https://nonebot.dev">
    <img src="https://img.shields.io/badge/nonebot-2.3.1+-red.svg" alt="nonebot">
</a>

</div>

- 以发送消息的方式操作Bot所在环境的系统命令行
- 甚至可以通过此插件 `rm` 整个服务器
- 限超级用户使用

## 💿 安装

**nb-cli安装, 包管理器安装  二选一**

<details>
<summary>使用 nb-cli 安装</summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-system-command

</details>

<details>
<summary>使用包管理器安装</summary>

在 nonebot2 项目的插件目录下, 打开命令行,

**根据你使用的包管理器, 输入相应的安装命令**

<details>
<summary>pip</summary>

    pip install nonebot-plugin-system-command

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-system-command

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-system-command

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-system-command

</details>

打开 bot项目下的 `pyproject.toml` 文件,

在其 `plugins` 里加入 `nonebot_plugin_system_command`

    plugins = ["nonebot_plugin_system_command"]

</details>
</details>

## 🎉 使用

- 可在 Bot项目的 `.env*` 中自定义调用命令行的指令,
  默认值为 `/sh` 和 `/cmd`

- 如果 `.env*` 中 `COMMAND_START` 变量值为 `["/"]`
  那么指令应该为 `//sh` `//cmd`

```env
SYS_CMD_SH="/sh"
SYS_CMD_CMD="/cmd"
```

### 指令表

<table> 
  <tr align="center">
    <th> 指令 </th>
    <th> 权限 </th>
    <th> 需要@ </th>
    <th> 范围 </th>
    <th> 特性 </th>
    <th> 说明 </th>
  </tr>
  <tr align="center">
    <td> /sh </td>
    <td> 主人 </td>
    <td> 否 </td>
    <td> 私聊 | 群聊 </td>
    <td> 异步管道 </td>
    <td> Windows环境无法正常使用 </td>
  </tr>
  <tr align="center">
    <td> /cmd </td>
    <td> 主人 </td>
    <td> 否 </td>
    <td> 私聊 | 群聊 </td>
    <td> 同步管道 </td>
    <td> 通用 </td>
  </tr>
</table>

### 语法

命令行语法与Bot运行环境相关, 与插件指令无关

- `bash` 运行即使用 `bash` 语法
- `zsh` 运行即使用 `zsh` 语法
- `powershell` 运行即使用 `powershell` 语法
- `cmd` 运行即使用 `cmd` 语法

其他shell同理

### ⚠️ ATTENTION

- 当您使用本插件时, 我们默认您了解命令行的基本使用, 以及在 `根环境` 运行命令的危险性;
- 在使用本插件前请先确认没有其他插件与本插件的指令发生冲突, 如有, 请在Bot项目下的 `.env*` 文件里自定义本插件的响应指令;
- 如有因为此插件响应了不相干的消息, 导致设备遭到损坏, 将由使用者自己承担相关责任.

注: 此处的 `根环境` 是指以 `root` 或者 `管理员(Administrator)` 或者其他高权限运行的终端环境

### 示例

```
/sh echo "hello world"
```

```
/cmd echo "hello world"
```

### 效果图

![01.png](https://github.com/tkgs0/nonebot-plugin-system-command/raw/resource/01.png)

## TODO

- [x] 使用异步管道
- [ ] 命令行交互

## ⚠️ ATTENTION

**Don't drink and root! 🍻**
