from tkinter import Tk
from tkinter import *
from tkinter import ttk
import tkinter as tk

class System:
    def __init__(self, root):
        self.root = root
        self.root.title("System Info")
        self.root.geometry("502x629")
        self.root.resizable(width=False, height=False)
        
    def system_info_interface(self):
        
        notebook = ttk.Notebook(self.root)
        
        os_tab = Frame(notebook)
        cpu_tab = Frame(notebook)
        mem_tab = Frame(notebook)
        disk_tab = Frame(notebook)
        
        notebook.add(os_tab, text="OS Info")
        notebook.add(cpu_tab, text="CPU Info")
        notebook.add(mem_tab, text="Mem Info")
        notebook.add(disk_tab, text="Disk Info")
        notebook.pack(expand=True, fill="both")
        
        def os_info():
            # OS System Info
            import system
            
            s = 5
            x = 10

            os_name = Label(os_tab, text="OS Name:        " + system.os_name)
            os_name.place(x=x, y=0+s)
            
            system1 = Label(os_tab, text="System:           " + system.system)
            system1.place(x=x, y=21+s*2)
            
            node = Label(os_tab, text="Node:               " + system.node)
            node.place(x=x, y=42+s*3)
            
            machine = Label(os_tab, text="Machine:          " + system.machine)
            machine.place(x=x, y=63+s*4)
        
            os_platform = Label(os_tab, text="Platform:          " + system.os_platform)
            os_platform.place(x=x, y=84+s*5)
            
            os_version = Label(os_tab, text="Version Time:  " + system.os_version)
            os_version.place(x=x, y=105+s*6)
            
            architecture = Label(os_tab, text='Architecture:    ' + system.architecture)
            architecture.place(x=x, y=126+s*7)
            
            os_version_local = Label(os_tab, text="OS Version:      " + system.os_version_local)
            os_version_local.place(x=x, y=147+s*8)
            
            os_base = Label(os_tab, text="OS BASE:         " + system.os_base)
            os_base.place(x=x, y=168+s*9)
            
            os_support = Label(os_tab, text="Support:           " + system.os_support)
            os_support.place(x=x, y=189+s*10)
        
        os_info()
        
        def cpu_info():
            # CPU Info
            import cpu

            x = 10
            s = 5
            
            cpu_name = Label(cpu_tab, text="CPU:                        " + cpu.cpu_name()[0])
            cpu_name.place(x=x, y=0+s)
            
            cpu_use_text = Label(cpu_tab, text="CPU Use:                 %")
            cpu_use_text.place(x=x, y=21+s*2)
            cpu_use = Label(cpu_tab, text=int(cpu.cpu_use_top()), fg="black")
            cpu_use.place(x=(x*9)+62, y=21+s*2)
            
            cpu_core = Label(cpu_tab, text="CPU Core:                " + str(cpu.cpu_info_core))
            cpu_core.place(x=x, y=42+s*3)
            
            cpu_thread = Label(cpu_tab, text="CPU Thread:            " + str(cpu.cpu_info_thread))
            cpu_thread.place(x=x, y=63+s*4)
            
            cpu_freq_top_text = Label(cpu_tab, text="CPU Freq(Mhz): ")
            cpu_freq_top_text.place(x=x, y=84+s*5)
            cpu_freq_top = Label(cpu_tab, text=int(cpu.cpu_core_freq_top()[0]))
            cpu_freq_top.place(x=(x*11)+30, y=84+s*5)
            
            cpu_max_freq = Label(cpu_tab, text="CPU max. Freq:       "+ str(cpu.cpu_core_freq_top()[2]))
            cpu_max_freq.place(x=x, y=105+s*6)
            
            cpu_max_freq = Label(cpu_tab, text="CPU min. Freq:        "+ str(cpu.cpu_core_freq_top()[1]))
            cpu_max_freq.place(x=x, y=126+s*7)
            
            cpu_clock_text = Label(cpu_tab, text="CPU Clock(Second): ")
            cpu_clock_text.place(x=x, y=147+s*8)
            cpu_clock = Label(cpu_tab, text=int(cpu.cpu_time()))
            cpu_clock.place(x=(x*14), y=147+s*8)
            
            core = Label(cpu_tab, text="Cores: ", font="Helvetica 17")
            core.place(x=x, y=230)
            
            cpu_list = cpu.cpu_name()[1]
            list = Listbox(cpu_tab, width=53, height=18, font="Helvetica 12")
            for i in cpu_list:
                index = cpu_list.index(i)
                list.insert(index, i[0] + " @ " + i[1])
                
            list.place(x=x, y=260)
            
                
            def update():
                cpu_use['text'] = cpu.cpu_use_top()
                if cpu.cpu_use_top() < 50:
                    cpu_use['fg'] = "green"
                elif cpu.cpu_use_top() >= 50:
                    cpu_use['fg'] = "red"
                    
                cpu_freq_top['text'] = int(cpu.cpu_core_freq_top()[0])
                    
                cpu_clock['text'] = cpu.cpu_time()
                self.root.after(1000, update) # run itself again after 1000 ms
            
            update()
            
        
        cpu_info()
        
        
        def mem_info():
            #Mem Info
            import mem
            
            x = 10
            s = 5
            g = 50
            
            Label(mem_tab, text="Memory: ", font="Helvetica 23").place(x=5, y=12)
            
            total_ram = Label(mem_tab, text="Total RAM:         " + str(round(mem.mem_total, 1)) + " GB")
            total_ram.place(x=x, y=0+s+g)
            
            use_ram_text = Label(mem_tab, text="Used Ram:                GB ")
            use_ram_text.place(x=x, y=21+g+s*2)
            use_ram = Label(mem_tab, text=str(round(mem.mem_use(),1)))
            use_ram.place(x=(x*10)+20, y=21+g+s*2)
            
            available_ram_text = Label(mem_tab, text="Available Ram:         GB ")
            available_ram_text.place(x=x, y=42+g+s*3)
            available_ram = Label(mem_tab, text=str(round(mem.mem_available(), 1)))
            available_ram.place(x=x*12, y=42+g+s*3)
            
            mem_percent_text = Label(mem_tab, text="RAM Use:            %")
            mem_percent_text.place(x=x, y=63+g+s*4)
            mem_percent = Label(mem_tab, text=str(round(mem.mem_percent(), 1)), fg="black")
            mem_percent.place(x=(x*13)+5, y=63+g+s*4)
            
            Label(mem_tab, text="Swap: ", font="Helvetica 23").place(x=5, y=200)
            
            total_swap = Label(mem_tab, text="Total Swap Area:      " + str(round(mem.swap_mem_total, 1)) + " GB")
            total_swap.place(x=x, y=245)
            
            total_swap_use = Label(mem_tab, text="Used Swap Area:      " + str(round(mem.swap_mem_used, 1)) + " GB")
            total_swap_use.place(x=x, y=266+s)
            
            total_swap_free = Label(mem_tab, text="Free Swap Area:      " + str(round(mem.swap_mem_free, 1)) + " GB")
            total_swap_free.place(x=x, y=286+(s*2))
            
            total_swap_percent = Label(mem_tab, text="Swap Area Percent:  %" + str(round(mem.swap_mem_percent, 1)))
            total_swap_percent.place(x=x, y=307+(s*3))
            
            
            def update():
                use_ram['text'] = round(mem.mem_use(),1)
                available_ram['text'] = round(mem.mem_available(), 1)
                mem_percent['text'] = round(mem.mem_percent(), 1)-5
                if round(mem.mem_percent(), 1)-5 > 50:
                    mem_percent['fg'] = "red"
                elif round(mem.mem_percent(), 1)-5 <= 50:
                    mem_percent['fg'] = "green"
                
                self.root.after(1000, update) # run itself again after 1000 ms
            
            update()
        
        mem_info()
        
        def disk_info():
            # DISK Info
            import disk
            
            disk_use = disk.disk_usage()
            
            for i in disk_use:
                index = disk_use.index(i)
                temp_disk = disk_use[index]
                
                disk_frame = Frame(disk_tab, highlightbackground="grey", highlightthickness=2, bg="white", width=480, height=100, borderwidth="2")
                disk_frame.pack(pady=10)
                
                disk_fr = Label(disk_frame, bg="white", text="Device: " + temp_disk[0])
                disk_fr.place(x=10, y=5)
                
                disk_type = Label(disk_frame, bg="white", text="File Type: " + temp_disk[2])
                disk_type.place(x=10, y=30)
            
                disk_path = Label(disk_frame, bg="white", text="Path: " + temp_disk[1])
                disk_path.place(x=10, y=55)
                
                disk_capacity = Label(disk_frame, bg="white", text="Storage Capacity: " + temp_disk[3] + "GB")
                disk_capacity.place(x=200, y=5)
                
                disk_free = Label(disk_frame, bg="white", text="Free: " + temp_disk[5] + "GB")
                disk_free.place(x=200, y=30)
                
                disk_free = Label(disk_frame, bg="white", text="Storage Percent: %" + str(temp_disk[6]))
                disk_free.place(x=310, y=30)
            
        disk_info()
        

def main():
    root = Tk()
    ui = System(root).system_info_interface()
    root.mainloop()
    

if __name__ == "__main__":
    main()
