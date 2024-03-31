from colorama import Fore, Back, Style
import wmi 
def neofetch():
      computer = wmi.WMI()
      computer_info = computer.Win32_ComputerSystem()[0]
      os_info = computer.Win32_OperatingSystem()[0]
      proc_info = computer.Win32_Processor()[0]
      gpu_info = computer.Win32_VideoController()[0]


      os_name = (os_info.Caption)
      os_version = os_info.Version
      proc_name = proc_info.Name
      clock_speed = proc_info.CurrentClockSpeed
      system_ram = round(float(os_info.TotalVisibleMemorySize) / 1048576, 1)
      gpu_name = gpu_info.Name
      resolution = (f"{gpu_info.CurrentHorizontalResolution} X {gpu_info.CurrentVerticalResolution}")
      model = computer_info.Model
      name = computer_info.Name
      primary_owner_name = computer_info.PrimaryOwnerName
      system_type = computer_info.SystemType


      win10 =(f"""
      \033[1;34m                    ....,,:;+ccllll\033[0m         \033[1;34mOS:\033[0m \033[1;33m{ os_name}\033[0m
      \033[1;34m      ...,,+:;  cllllllllllllllllll\033[0m         \033[1;34mOS Version:\033[0m \033[1;33m{os_version}\033[0m
      \033[1;34m,cclllllllllll  lllllllllllllllllll\033[0m         \033[1;34mCPU:\033[0m \033[1;33m{proc_name}\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mClock Speed:\033[0m \033[1;33m{clock_speed}\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mRAM:\033[0m \033[1;33m{system_ram} GB\033[0m               
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mGPU:\033[0m \033[1;33m{gpu_name}\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mResolution:\033[0m \033[1;33m{resolution}\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mModel:\033[0m \033[1;33m{model}\033[0m
      \033[1;34m                                   \033[0m         \033[1;34mName:\033[0m \033[1;33m{name}\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mPrimary Owner Name:\033[0m \033[1;33m{primary_owner_name}\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         \033[1;34mSystem Type:\033[0m \033[1;33m{system_type}\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m         
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m
      \033[1;34mllllllllllllll  lllllllllllllllllll\033[0m
      \033[1;34m`'ccllllllllll  lllllllllllllllllll\033[0m
      \033[1;34m       `'`*:::  :ccllllllllllllllll\033[0m
      \033[1;34m                       ````''*::cll\033[0m
      \033[1;34m                                 ``\033[0m
      """)

      win10_no_ansi = (f"""
                        ....,,:;+ccllll           OS: {os_name}
            ...,,+:;  cllllllllllllllllll         OS Version: {os_version}
      ,cclllllllllll  lllllllllllllllllll         CPU: {proc_name}
      llllllllllllll  lllllllllllllllllll         Clock Speed: {clock_speed}
      llllllllllllll  lllllllllllllllllll         RAM: {system_ram} GB              
      llllllllllllll  lllllllllllllllllll         GPU: {gpu_name}
      llllllllllllll  lllllllllllllllllll         Resolutio: {resolution}
      llllllllllllll  lllllllllllllllllll         Model: {model}
                                                  Name: {name}
      llllllllllllll  lllllllllllllllllll         Primary Owner Name: {primary_owner_name}
      llllllllllllll  lllllllllllllllllll         System Type: {system_type}
      llllllllllllll  lllllllllllllllllll         
      llllllllllllll  lllllllllllllllllll
      llllllllllllll  lllllllllllllllllll
      `'ccllllllllll  lllllllllllllllllll
            `'`*:::  :ccllllllllllllllll
                        ````''*::cll
                                    ``
      """)
      
      print(win10_no_ansi)
     

if __name__ == '__main__':
      neofetch()



