from platform import system
from subprocess import Popen, PIPE
from asyncio import create_subprocess_shell
from asyncio.subprocess import PIPE as AsyncPIPE
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.params import CommandArg
from nonebot.adapters import Message

from html import unescape



cmd_help: str = (
    '调用系统命令行\n'
    '⚠危险操作, 谨慎使用!\n\n'
    '/cmd {命令}\n'
    'For example:\n'
    '/cmd echo "Hello World"'
)


shell_help: str = (
    '调用系统命令行\n'
    '(不支持Windows)\n'
    '⚠危险操作, 谨慎使用!\n\n'
    '/shell {命令}\n'
    'For example:\n'
    '/shell echo "Hello World"'
)


_win: tuple = ('windows', 'win32', 'win16')



sys_shell = on_command(
    '/shell',
    permission=SUPERUSER,
    priority=1,
    block=True
)

@sys_shell.handle()
async def _(args: Message = CommandArg()):
    for i in _win:
        if system() and (system().lower() in i or i in system().lower()):
            await sys_shell.finish('暂不支持Windows,\n请使用 `/cmd`')
    opt: str = args.extract_plain_text()

    if not opt:
        await sys_shell.finish('发送 /shell.help 以获取帮助')

    if opt == '.help':
        await sys_shell.finish(shell_help)

    content: tuple = await (await create_subprocess_shell(
        unescape(opt),
        stdin=AsyncPIPE,
        stdout=AsyncPIPE,
        stderr=AsyncPIPE
    )).communicate()
    
    if content == (b'', b''):
        msg: str = '\n执行完毕, 没有任何输出呢~'
    elif content[1] == b'':
        msg: str = f'\nstdout:\n{content[0].decode()}\n>执行完毕'
    elif content[0] == b'':
        msg: str = f'\nstderr:\n{content[1].decode()}'
    else :
        msg: str = (f'\nstdout:\n{content[0].decode()}'
               f'\nstderr:\n{content[1].decode()}'
               '\n>执行完毕')
    await sys_shell.finish(msg, at_sender=True)


sys_cmd = on_command(
    '/cmd',
    priority=1,
    block=True,
    permission=SUPERUSER
)


@sys_cmd.handle()
async def _(args: Message = CommandArg()):
    opt: str = args.extract_plain_text()

    if not opt:
        await sys_cmd.finish('发送 /cmd.help 以获取帮助')

    if opt == '.help':
        await sys_cmd.finish(cmd_help)

    content: tuple = Popen(
        unescape(opt),
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        shell=True,
        universal_newlines=True
    ).communicate()

    if content == ('',''):
        msg: str = '\n执行完毕, 没有任何输出呢~'
    elif content[1] == '':
        msg: str = f'\nstdout:\n{content[0]}\n>执行完毕'
    elif content[0] == '':
        msg: str = f'\nstderr:\n{content[1]}'
    else :
        msg: str = f'\nstdout:\n{content[0]}\nstderr:\n{content[1]}\n>执行完毕'
    await sys_cmd.finish(msg, at_sender=True)
