import wmi
import psutil


def neofetch():
    computer = wmi.WMI()
    computer_info = computer.Win32_ComputerSystem()[0]
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]
    gpu_info = computer.Win32_VideoController()[0]

    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)

    os_name = os_info.Caption
    os_version = os_info.Version
    proc_name = proc_info.Name
    clock_speed = proc_info.CurrentClockSpeed
    system_ram = round(float(os_info.TotalVisibleMemorySize) / 1048576, 1)
    gpu_name = gpu_info.Name
    resolution = (
        f"{gpu_info.CurrentHorizontalResolution} X {gpu_info.CurrentVerticalResolution}"
    )
    model = computer_info.Model
    name = computer_info.Name
    primary_owner_name = computer_info.PrimaryOwnerName
    system_type = computer_info.SystemType

    win10 = f"""
\033[1;34m                    ....,,:;+ccllll\033[0m         \033[1;34mOS:\033[0m \033[1;33m{ os_name}\033[0m
\033[1;34m      ...,,+:;  cllllllllllllllllll\033[0m         \033[1;34mOS Version:\033[0m \033[1;33m{os_version}\033[0m
\033[1;34m,cclllllllllll  lllllllllllllllllll\033[0m         \033[1;34mCPU:\033[0m \033[1;33m{proc_name}\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mClock Speed:\033[0m \033[1;33m{clock_speed}\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mCPU Cores:\033[0m \033[1;33m{cpu_cores}\033[0m      
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mCPU Threads:\033[0m \033[1;33m{cpu_threads}\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mCPU Usage:\033[0m \033[1;33m{cpu_usage}%\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mGPU:\033[0m \033[1;33m{gpu_name}\033[0m
\033[1;34m                                   \033[0m         \033[1;34mRAM:\033[0m \033[1;33m{system_ram} GB\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mResolution:\033[0m \033[1;33m{resolution}\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mSystem Type:\033[0m \033[1;33m{system_type}\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mModel:\033[0m \033[1;33m{model}\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mName:\033[0m \033[1;33m{name}\033[0m
\033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mPrimary Owner Name:\033[0m \033[1;33m{primary_owner_name}\033[0m
\033[1;34m`'ccllllllllll  lllllllllllllllllll\033[0m         
\033[1;34m       `'`*:::  :ccllllllllllllllll\033[0m
\033[1;34m                       ````''*::cll\033[0m
\033[1;34m                                 ``\033[0m
"""

    print(win10)


if __name__ == "__main__":
    neofetch()
