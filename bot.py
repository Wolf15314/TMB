
from config import TOKEN
#import logging
#import os
#import sys
#import time
import operator
from datetime import datetime
import psutil
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    now = datetime.now()
    await bot.send_message(message.from_user.id, str(now) + "\n"  + "Привет, что будем делать?" )

@dp.message_handler(commands=['help'])
async def process_help (message: types.Message):
    await bot.send_message(message.from_user.id, 'Доступные команды:\n'
                                                 'cpuload - загрузка процессора в % \n'
                                                 'cpucount - количество процессоров в системе\n'
                                                 'totalmemory - всего памяти в системе\n'
                                                 'memavail - памяти свободно\n'
                                                 'memused - памяти занято\n'
                                                 'diskused - исползовано дискового пространства\n'
                                                 'boottime - время старта\n'
                                                 'online - время работы\n'
                                                 'allmem - список процесоов + статистика\n'
                                                          )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "cpuload":
        cpuload = psutil.cpu_percent(interval=1)
        await message.answer("Загрузка процессора " + str(cpuload) + " %")
    elif message.text == "cpucount":
        cpucount = psutil.cpu_count()
        await message.answer("Процессоров " + str(cpucount)  + " шт" )
    elif message.text == "totalmemory":
        memory = psutil.virtual_memory()
        memtotal = "Всего памяти: %.2f GB " % (memory.total / 1000000000)
        await message.answer(str(memtotal))

    elif message.text == "memavail":
        memory = psutil.virtual_memory()
        memavail = "Свободно памяти: %.2f GB" % (memory.available / 1000000000)
        await message.answer(str(memavail))
    elif message.text == "memused":
        memory = psutil.virtual_memory()
        memusep = "Использовано памяти: " + str(memory.percent) + " %"
        await message.answer(str(memusep))
    elif message.text == "diskused":
        disk = psutil.disk_usage('/')
        diskused = "Диска использовано: " + str(disk.percent) + " %"
        await message.answer(str(diskused))
    #elif message.text == "disk":
    #    disk = psutil.disk_usage('/')
    #   await message.answer(str(disk))
    elif message.text == "boottime":
        boottime = datetime.fromtimestamp(psutil.boot_time())
        await message.answer("Время  запуска:  \n" + str(boottime))
    elif message.text == "online":
        now = datetime.now()
        boottime = datetime.fromtimestamp(psutil.boot_time())
        timedif = "Время работы : %.1f Часов" % (((now - boottime).total_seconds()) / 3600)
        await message.answer(str(timedif))
    elif message.text == "allmem":
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        boottime = datetime.fromtimestamp(psutil.boot_time())
        now = datetime.now()
        timedif = "Время работы : %.1f Часов" % (((now - boottime).total_seconds()) / 3600)
        memtotal = "Всего памяти: %.2f GB " % (memory.total / 1000000000)
        memavail = "Свободно памяти: %.2f GB" % (memory.available / 1000000000)
        memuseperc = "Использовано памяти: " + str(memory.percent) + " %"
        diskused = "Диска использовано: " + str(disk.percent) + " %"

        pids = psutil.pids()
        pidsreply = ''
        procs = {}
        for pid in pids:
            p = psutil.Process(pid)
            try:
                pmem = p.memory_percent()
                if pmem > 0.5:
                    if p.name() in procs:
                        procs[p.name()] += pmem
                    else:
                        procs[p.name()] = pmem
            except:
                print("Hm")
        sortedprocs = sorted(procs.items(), key=operator.itemgetter(1), reverse=True)
        for proc in sortedprocs:
            pidsreply += proc[0] + " " + ("%.2f" % proc[1]) + " %\n"
        reply = timedif + "\n" + \
                memtotal + "\n" + \
                memavail + "\n" + \
                memuseperc + "\n" + \
                diskused + "\n\n" + \
                pidsreply
        await message.answer(reply)
    else:
        await message.answer ("Нет такой команды: " + message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)